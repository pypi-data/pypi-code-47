from octopy import request, model


class Tree:

    """
    Official GITHUB documentation: https://developer.github.com/v3/git/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GitData-Tree.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self, owner, repo, tree_sha, recursive=False):
        """
        Returns a single tree.

        :param owner: owner's name
        :param repo: repo's name
        :param tree_sha: tree's sha
        :kwarg recurcive: if set to true, it will return the tree recursively. default: false
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/trees/{tree_sha}{'?recursive=1' if recursive else ''}"
        return model.create_class("Tree", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a tree.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg tree: [required]
            Array of the following objects:
            :kwarg path: file references in this tree
            :kwarg mode: file mode
            :kwarg type: blob, tree, commit
            :kwarg sha: SHA1 checksum ID of the object in the tree
            :kwarg content: content of the file
        :kwarg base_tree: SHA1 of the tree you want to update
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/trees"
        return model.create_class(
            "Tree", request.post(url, headers=self._headers, params=kwargs)
        )
