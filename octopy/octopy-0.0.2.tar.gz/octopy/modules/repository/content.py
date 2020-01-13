from octopy import request, model


class Content:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/contents/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Content
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def readme(self, owner, repo, **kwargs):
        """
        Gets the readme of a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg ref: name of the commit/branch/tag
        """
        url = f"{self._url}/repos/{owner}/{repo}/readme"
        return model.create_class("README", request.get(url, headers=self._headers))

    def content(self, owner, repo, path, **kwargs):
        """
        Returns the content of a file, or directory in a repository.

        :param owner: owner's name
        :param repo: repo's name
        :param path: file or directory path
        :kwarg ref: commit/branch/tag
        """
        url = f"{self._url}/repos/{owner}/{repo}/contents/{path}"
        return model.create_class(
            "Content", request.get(url, headers=self._headers, params=kwargs)
        )

    def create(self, owner, repo, path, **kwargs):
        """
        Creates a file.

        :param owner: owner's name
        :param repo: repo's name
        :param path: file/directiory path
        :kwarg message: [required] commit message
        :kwarg content:[required] new file content
        :kwarg sha: blob SHA of the file
        :kwarg branch: branch name
        :kwarg commiter: name of the commiter
        :kwarg author: 
            :kwarg name: [required] name of the author/commiter
            :kwarg email: [required] email of the author/commiter
        """
        url = f"{self._url}/repos/{owner}/{repo}/contents/{path}"
        return model.create_class(
            "File", request.put(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, path, **kwargs):
        """
        Updates a file.

        :param owner: owner's name
        :param repo: repo's name
        :param path: file/directiory path
        :kwarg message: [required] commit message
        :kwarg content:[required] new file content
        :kwarg sha: [required] blob SHA of the file
        :kwarg branch: branch name
        :kwarg commiter: name of the commiter
        :kwarg author: 
            :kwarg name: [required] name of the author/commiter
            :kwarg email: [required] email of the author/commiter
        """
        url = f"{self._url}/repos/{owner}/{repo}/contents/{path}"
        return model.create_class(
            "File", request.put(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, **kwargs):
        """
        Deletes a file.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg message: [required] commit's message
        :kwarg sha: [required] blob SHA of the file
        :kwarg branch: branch name
        """
        url = f"{self._url}/repos/{owner}/{repo}/contents/{path}"
        return model.create_class(
            "Response", request.delete(url, headers=self._headers, params=kwargs)
        )

    def archive(self, owner, repo, archive_format, ref):
        """
        Returns an archive link.

        :param owner: owner's name
        :param repo: repo's name
        :param acrhive_format: archive's format
        :param ref: commit's ref
        """
        url = f"{self._url}/repos/{owner}/{repo}/{archive_format}/{ref}"
        return model.create_class("Status", request.get(url, headers=self._headers))
