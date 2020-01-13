from octopy import request, model


class Release:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/releases/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Release
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns all releases for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: page from which results to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases?page={page}"
        items = [
            model.create_class("Release", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, owner, repo, release_id):
        """
        Returns a single release.

        :param owner: owner's name
        :param repo: repo's name
        :param release_id: release's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/{release_id}"
        return model.create_class("Release", request.get(url, headers=self._headers))

    def latest(self, owner, repo):
        """
        Returns latest release.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/latest"
        return model.create_class("Release", request.get(url, headers=self._headers))

    def by_tag_name(self, owner, repo, tag):
        """
        Returns a release by tag name.

        :param owner: owner's name
        :param repo: repo's name
        :param tag: tag
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/tags/{tag}"
        return model.create_class("Release", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a release.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg tag_name: [required] tag's name
        :kwarg target_commitish: Specifies the commitish value 
            that determines where the Git 
            tag is created from. Can be any 
            branch or commit SHA. Unused if the 
            Git tag already exists. 
            Default: the repository's default branch (usually master).
        :kwarg name: name of the release
        :kwarg body: short description for content of the tag
        :kwarg draft: true to create a 
            draft (unpublished) release, false to create a published one. Default: false
        :kwarg prerelease: true to identify the release as a prerelease. 
            false to identify the release as a full release. Default: false
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases"
        return model.create_class(
            "Release", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, release_id, **kwargs):
        """
        Updates a release.

        :param owner: owner's name
        :param repo: repo's name
        :param release_id: release's id
        :kwarg tag_name: tag's name
        :kwarg target_commitish: Specifies the commitish value 
            that determines where the Git 
            tag is created from. Can be any 
            branch or commit SHA. Unused if the 
            Git tag already exists. 
            Default: the repository's default branch (usually master).
        :kwarg name: name of the release
        :kwarg body: short description for content of the tag
        :kwarg draft: true to create a 
            draft (unpublished) release, false to create a published one. Default: false
        :kwarg prerelease: true to identify the release as a prerelease. 
            false to identify the release as a full release. Default: false
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/{release_id}"
        return model.create_class(
            "Release", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, release_id):
        """
        Deletes a release.

        :param owner: owner's name
        :param repo: repo's name
        :param release_id: release's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/{release_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def assets(self, owner, repo, release_id, page=1):
        """
        Returns all assets for a release.

        :param owner: owner's name
        :param repo: repo's name
        :param release_id: release's id
        :kwarg page: from which page assets to be returned; default: 1
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/releases/{release_id}/assets?page={page}"
        )
        items = [
            model.create_class("Asset", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def upload(self, server, owner, repo, release_id, **kwargs):
        """
        
        :param server:
        :param owner:
        :param repo:
        :param release_id:
        :kwarg name:
        :kwarg label:
        """
        url = f"{server}/repos/{owner}/{repo}/releases/{release_id}/assets"
        return model.create_class(
            "Release", request.post(url, headers=self._headers, params=kwargs)
        )

    def asset(self, owner, repo, asset_id):
        """
        Returns a single asset.

        :param owner: owner's name
        :param repo: repo's name
        :param asset_id: asset's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/assets/{asset_id}"
        return model.create_class("Asset", request.get(url, headers=self._headers))

    def update_asset(self, owner, repo, asset_id, **kwargs):
        """
        Updates an asset.

        :param owner: owner's name
        :param repo: repo's name
        :param asset_id: asset's id
        :kwarg name: 
        :kwarg label:
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/assets/{asset_id}"
        return model.create_class(
            "Asset", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove_asset(self, owner, repo, asset_id):
        """
        Deletes an asset.

        :param owner: owner's name
        :param repo: repo's name
        :param asset_id: asset's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/releases/assets/{asset_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
