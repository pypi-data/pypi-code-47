from enum import Enum
from json import load as json_load
from os import listdir
from time import sleep

from requests.sessions import Session


class ADFObjectType(Enum):
    """
    Set of  object types in Azure Data Factory that can be deployed.
    """
    LinkedService = 'linkedService'
    Dataset = 'dataset'
    Pipeline = 'pipeline'
    Trigger = 'trigger'

    def __str__(self):
        return self.value


class AzureDataFactoryDeployer(object):
    """
    Deployment tool for Azure Data Factories.
    """
    API_VERSION = '2018-06-01'

    def __init__(
            self,
            credentials,
            subscription_id,
            resource_group_name,
            name,
            path,
    ):
        """
        AzureDataFactoryDeployer class constructor.

        The main (and only) way to create an AzureDataFactoryDeployer instance.

        Parameters
        ----------
        credentials
            A valid form of Azure credentials. In most cases this will be a
            valid instance the class of `ServicePrincipalCredentials`. This
            class is imported from the `azure.common.credentials` module.
        subscription_id
            Identifier of the subscription in which the Azure Data Factory
            instance is located.
        resource_group_name
            Name of the resource group in which the Azure Data Factory instance
            is located.
        name
            Name of the data factory instance to create or update.
        path
            Path to folder containing the Azure Data Factory resources. This
            must be the root folder that contains the folders called "dataset",
            "linkedService", "pipeline", and "trigger".
        """
        self._path = path

        self._adf_url = 'https://management.azure.com/{}/{}'.format(
            'subscriptions/{}/resourceGroups/{}'.format(
                subscription_id,
                resource_group_name,
            ),
            'providers/Microsoft.DataFactory/factories/{}'.format(name),
        )

        self.session = Session()
        self.session.headers.update({
            'Authorization': 'bearer {}'.format(
                credentials.token['access_token'],
            ),
        })

    def deploy(self):
        print('Starting deployment...')
        for object_type in ADFObjectType:
            self._deploy(object_type)

        print('Completed deployment.')

    def _deploy(self, object_type):
        old_objects = self._get(object_type)
        old_objects = {o['name']: o for o in old_objects}

        # Get updated list of objects according to the current state of the
        # repository.
        new_objects = self._get_objects_from_repo(object_type)
        new_objects = {o['name']: o for o in new_objects}

        # The objects that were in the existing list but not in the list of
        # updated objects are up for deletion. Note that there is a possibility
        # that they were renamed, but in this case a new object will be made
        # with the new name instead.
        objects_to_be_deleted = [
            o for o in old_objects
            if o not in new_objects
        ]

        # All objects that have their names in both the old and updated list of
        # objects are to be updated, but only if their contents are no longer
        # the same.
        objects_to_be_updated = [
            o for o in new_objects
            if o in old_objects
            and new_objects[o]['properties'] != old_objects[o]['properties']
        ]

        # The only objects that are new, are the ones that do not appear in the
        # existing list of objects. Note that some of these might be renamed
        # versions of existing objects, but it does little harm to create a new
        # one as the previous name will then be up for deletion.
        objects_to_be_created = [
            o for o in new_objects
            if o not in old_objects
        ]

        if object_type is ADFObjectType.LinkedService:
            objects_to_be_created = self.get_deploy_order([
                new_objects[ls] for ls in objects_to_be_created
            ])
            objects_to_be_updated = self.get_deploy_order([
                new_objects[ls] for ls in objects_to_be_updated
            ])

        for o in objects_to_be_deleted:
            print('Deleting {}: {}...'.format(object_type, o))
            self._delete(object_type, o)
            print('Deleted {}: {}.'.format(object_type, o))

        for o in objects_to_be_created:
            print('Creating {}: {}'.format(object_type, o))
            self._create(object_type, o, new_objects[o])
            print('Created {}: {}'.format(object_type, o))

        for o in objects_to_be_updated:
            print('Updating {}: {}'.format(object_type, o))
            self._update(object_type, o, new_objects[o], old_objects[o]['etag'])
            print('Updated {}: {}'.format(object_type, o))

        if object_type is ADFObjectType.Trigger:
            # Wait for triggers to be processed before starting them.
            sleep(5)

            for o in objects_to_be_created + objects_to_be_updated:
                self._start_trigger(o)

    def _create(self, object_type, name, data):
        response = self.session.put(
            '{}/{}s/{}?api-version={}'.format(
                self._adf_url,
                object_type,
                name,
                self.API_VERSION,
            ),
            json=data,
        )

        return response.status_code

    def _get(self, object_type):
        response = self.session.get(
            '{}/{}s?api-version={}'.format(
                self._adf_url,
                object_type,
                self.API_VERSION,
            ),
        )

        return response.json()['value']

    def _update(self, object_type, name, data, etag):
        response = self.session.put(
            '{}/{}s/{}?api-version={}'.format(
                self._adf_url,
                object_type,
                name,
                self.API_VERSION,
            ),
            json=data,
            headers={
                'If-Match': etag,
            },
        )

        return response.status_code

    def _delete(self, object_type, name):
        response = self.session.delete(
            '{}/{}s/{}?api-version={}'.format(
                self._adf_url,
                object_type,
                name,
                self.API_VERSION,
            ),
        )

        return response.status_code

    def _start_trigger(self, trigger_name):
        print('Starting trigger: {}'.format(trigger_name))
        response = self.session.post(
            '{}/triggers/{}/start?api-version={}'.format(
                self._adf_url,
                trigger_name,
                self.API_VERSION,
            ),
        )
        print('Started trigger: {}'.format(trigger_name))

        return response.status_code

    def _get_objects_from_repo(self, object_type):
        object_dir_path = '{}/{}'.format(self._path, object_type)
        objects = []

        for object_file_name in listdir(object_dir_path):
            object_file_path = '{}/{}'.format(object_dir_path, object_file_name)

            with open(object_file_path, 'r') as object_file:

                object_json = json_load(object_file)
                objects.append(object_json)

        return objects

    @classmethod
    def get_reference_name(cls, linked_service):
        if 'referenceName' in linked_service:
            return linked_service['referenceName']

        for value in linked_service.values():
            if isinstance(value, dict):
                reference_name = cls.get_reference_name(value)

                if reference_name:
                    return reference_name

    @classmethod
    def get_deploy_order(cls, linked_services):
        references = [cls.get_reference_name(ls) for ls in linked_services]
        references = [ref for ref in references if ref is not None]

        dependents = [
            ls['name'] for ls in linked_services
            if ls['name'] not in references
        ]

        return references + dependents
