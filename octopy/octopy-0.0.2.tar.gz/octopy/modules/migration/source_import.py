from octopy import request, model


class SourceImport:

    """
    Official GITHUB documentation: https://developer.github.com/v3/migrations/source_imports/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/MigrationSourceImport.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.barred-rock-preview"

    def create(self, owner, repo, **kwargs):
        """
        Starts a source import to a GITHUB repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg vcs_url: [required] url of the original repository
        :kwarg vcs: vcs type
        :kwarg vcs_username: If authentication is required, 
            the username to provide to vcs_url.
        :kwarg vcs_password: If authentication is required, 
            the password to provide to vcs_url.
        :kwarg tfvc_project: For a tfvc import, 
            the name of the project that is being imported.
        """
        url = f"{self._url}/repos/{owner}/{repo}/import"
        return model.create_class(
            "SourceImport", request.put(url, headers=self._headers, params=kwargs)
        )

    def progress(self, owner, repo):
        """
        Returns import's progress.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/import"
        return model.create_class(
            "SourceImport", request.get(url, headers=self._headers)
        )

    def update(self, owner, repo, **kwargs):
        """
        Updates an existing report.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg vcs_username: The username to provide to the originating repository.
        :kwarg vcs_password: The password to provide to the originating repository.
        """
        url = f"{self._url}/repos/{owner}/{repo}/import"
        return model.create_class(
            "SourceImport", request.patch(url, headers=self._headers, params=kwargs)
        )

    def authors(self, owner, repo, **kwargs):
        """
        Returns all commit authors.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg since: Only authors found after this id 
            are returned. Provide the highest 
            author ID you've seen so far. 
            New authors may be added to the 
            list at any point while the 
            importer is performing the raw step.
        """
        url = f"{self._url}/repos/{owner}/{repo}/import/authors"
        items = [
            model.create_class("Author", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def map(self, owner, repo, author_id, **kwargs):
        """
        Updates an author's identity for the import.

        :param owner: owner's name
        :param repo: repo's name
        :param author_id: author's id
        :kwarg email: author's email
        :kwarg name: author's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/import/authors/{author_id}"
        return model.create_class(
            "Author", request.patch(url, headers=self._headers, params=kwargs)
        )

    def lfs_preference(self, owner, repo, **kwargs):
        """
        Sets lfs preference.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg use_lfs: [required] Can be one of opt_in 
            (large files will be stored using Git LFS) 
            or opt_out (large files will be removed during the import).
        """
        url = f"{self._url}/repos/{owner}/{repo}/import/lfs"
        return model.create_class(
            "LFSPreference", request.patch(url, headers=self._headers, params=kwargs)
        )

    def large_files(self, owner, repo):
        """
        Returns all large files larger than 100MB found during the import.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/import/large_files"
        items = [
            model.create_class("LargeFile", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def cancel(self, owner, repo):
        """
        Stops import for a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/import"
        return model.create_class("Status", request.delete(url, headers=self._headers))
