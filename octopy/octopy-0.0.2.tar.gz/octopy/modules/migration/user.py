from octopy import request, model


class User:

    """
    Official GITHUB documentation: https://developer.github.com/v3/migrations/users/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/MigrationUser.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.wyandotte-preview+json"

    def create(self, **kwargs):
        """
        Starts a generation of a user migration archive.

        :kwarg repositories: [required] list with repository 
            names which to include in the migration
        :kwarg lock_repositories: Locks the repositories to 
            prevent changes during the migration 
            when set to true. Default: false
        :kwarg exclude_attachments: Does not include 
            attachments uploaded to GitHub.com 
            in the migration data when set to true. 
            Excluding attachments will reduce the 
            migration archive file size. Default: false
        """
        url = f"{self._url}/user/migrations"
        return model.create_class(
            "UserMigration", request.post(url, headers=self._headers, params=kwargs)
        )

    def all(self, page=1):
        """
        Returns all user migrations.

        :kwarg page: from which page, migrations to be returned
        """
        url = f"{self._url}/user/migrations?page={page}"
        items = [
            model.create_class("UserMigration", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def status(self, migration_id):
        """
        Returns a status of a user's migration.

        :param migration_id: migration's id
        """
        url = f"{self._url}/user/migrations/{migration_id}"
        return model.create_class(
            "MigrationStatus", request.get(url, headers=self._headers)
        )

    def download(self, migration_id):
        """
        Returns a link of a user's migration archive.

        :param migration_id: migration's id
        """
        url = f"{self._url}/user/migrations/{migration_id}/archive"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def remove(self, migration_id):
        """
        Stops a migration import.

        :param migration_id: migration's id
        """
        url = f"{self._url}/user/migrations/{migration_id}/archive"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def unlock(self, migration_id, repo_name):
        """
        Unlocks a repository which was locked during the migration period.

        :param migration_id: migration's id
        :param repo_name: repo's name
        """
        url = f"{self._url}/user/migrations/{migration_id}/repos/{repo_name}/lock"
        return model.create_class("Status", request.delete(url, headers=self._headers))
