from octopy import request, model


class Organization:

    """
    Official GITHUB documentation: https://developer.github.com/v3/migrations/orgs/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/MigrationOrg.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.wyandotte-preview+json"

    def create(self, org, **kwargs):
        """
        Generates a migration archive.

        :param org: org's name
        :kwarg repositories: [required] list with repository names
        :kwarg lock_repositories: Indicates whether repositories should be locked 
        (to prevent manipulation) while migrating data. Default: false.
        :kwarg exclude_attachments: Indicates whether attachments 
            should be excluded from the migration 
            (to reduce migration archive file size). Default: false.
        """
        url = f"{self._url}/orgs/{org}/migrations"
        return model.create_class(
            "Migration", request.post(url, headers=self._headers, params=kwargs)
        )

    def all(self, org, page=1):
        """
        Returns all migrations of an organization.

        :param org: org's name
        :kwarg page: from which page migrations to be returned, default: 1
        """
        url = f"{self._url}/orgs/{org}/migrations?page={page}"
        items = [
            model.create_class("Migration", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def status(self, org, migration_id):
        """
        Gets the status of a migration.

        :param org: org's name
        :param migration_id: migration's id
        """
        url = f"{self._url}/orgs/{org}/migrations/{migration_id}"
        return model.create_class("Migration", request.get(url, headers=self._headers))

    def download(self, org, migration_id):
        """
        Gets a url for a migration archive.

        :param org: org's name
        :param migration_id: migration's id
        """
        url = f"{self._url}/orgs/{org}/migrations/{migration_id}/archive"
        return request.get(url, headers=self._headers)

    def remove(self, org, migration_id):
        """
        Deletes a migration archive.

        :param org: org's name
        :param migration_id: migration's id
        """
        url = f"{self._url}/orgs/{org}/migrations/{migration_id}/archive"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def unlock(self, org, migration_id, repo_name):
        """
        Unlocks a repository, which has been locked for a migration.

        :param org: org's name
        :param migration_id: migration's id
        :param repo_name: repo's name
        """
        url = f"{self._url}/orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock"
        return model.create_class("Status", request.delete(url, headers=self._headers))
