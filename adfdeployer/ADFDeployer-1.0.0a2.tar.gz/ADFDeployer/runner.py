from argparse import ArgumentParser

from azure.common.credentials import ServicePrincipalCredentials

from ADFDeployer.deployer import AzureDataFactoryDeployer


def main():
    parser = ArgumentParser(description='Publish an ADF configuration.')
    parser.add_argument(
        '--tenant-id',
        help='Tenant ID of the Azure Data Factory resource.',
        dest='tenant_id',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--subscription-id',
        help='Subscription in which the Azure Data Factory resource resides.',
        dest='subscription_id',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--resource-group-name',
        help='Resource group in which the Azure Data Factory resource resides.',
        dest='resource_group_name',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--client-id',
        help='Client (application) ID of the service principal that publishes the Azure Data Factory resource changes.',
        dest='client_id',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--client-secret',
        help='Client secret of the service principal that publishes the Azure Data Factory resources changes.',
        dest='client_secret',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--name',
        help='Name of the Azure Data Factory resource.',
        dest='name',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--repo-path',
        help='Path to the local version of the Azure Data Factory repository.',
        type=str,
        required=True,
    )

    arguments = parser.parse_args()

    credentials = ServicePrincipalCredentials(
        client_id=arguments.client_id,
        secret=arguments.client_secret,
        tenant=arguments.tenant_id,
    )

    deployer = AzureDataFactoryDeployer(
        credentials=credentials,
        subscription_id=arguments.subscription_id,
        resource_group_name=arguments.resource_group_name,
        name=arguments.name,
        path=arguments.path,
    )
    deployer.deploy()
