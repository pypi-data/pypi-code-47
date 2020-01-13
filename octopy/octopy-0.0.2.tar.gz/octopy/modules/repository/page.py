from octopy import request, model


class Page:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/pages/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Page
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def site(self, owner, repo):
        """
        Returns information about pages site.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/pages"
        return model.create_class("Site", request.get(url, headers=self._headers))

    def enable(self, owner, repo, **kwargs):
        """
        Enables a pages site.

        :param owner:
        :param repo:
        :kwarg source[branch]:
        :kwarg source[path]:
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.switcheroo-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pages"
        return model.create_class(
            "Page", request.post(url, headers=headers, params=kwargs)
        )

    def disable(self, owner, repo):
        """
        Disables a pages site.

        :param owner: owner's name
        :param repo: repo's name
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.switcheroo-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pages"
        return model.create_class("Status", request.delete(url, headers=headers))

    def update(self, owner, repo, **kwargs):
        """
        Updates a pages site.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg cname: Specify a custom 
            domain for the repository. 
            Sending a null value will remove 
            the custom domain. For more about custom domains, 
            see "Using a custom domain with GitHub Pages."
        :kwarg source:
            Update the source for the repository. 
            Must include the branch name, 
            and may optionally specify the 
            subdirectory /docs. 
            Possible values are "gh-pages", "master", 
            and "master /docs".
        """
        url = f"{self._url}/repos/{owner}/{repo}/pages"
        return model.create_class(
            "Status", request.put(url, headers=self._headers, params=kwargs)
        )

    def request(self, owner, repo):
        """
        Requests a page build.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/pages/builds"
        return model.create_class("PageBuild", request.post(url, headers=self._headers))

    def builds(self, owner, repo, page=1, latest=False):
        """
        Returns all pages builds.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, builds to be returned; default: 1
        :kwarg latest: if set to true, it will return only latest build
        """
        if latest:
            url = f"{self._url}/repos/{owner}/{repo}/pages/builds/latest"
            return model.create_class("Build", request.get(url, headers=self._headers))

        url = f"{self._url}/repos/{owner}/{repo}/pages/builds?page={page}"
        items = [
            model.create_class("Build", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def build(self, owner, repo, build_id):
        """
        Returns a specific build.

        :param owner: owner's name
        :param repo: repo's name
        :param build_id: build's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/pages/builds/{build_id}"
        return model.create_class("Build", request.get(url, headers=self._headers))
