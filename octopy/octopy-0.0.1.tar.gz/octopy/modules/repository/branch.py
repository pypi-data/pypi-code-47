from octopy import request, model


class Branch:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all branches on a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, branches to be returned; default: 1
        :kwarg protected: if set to true, returns only protected branches;
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches?page={page}"
        items = [
            model.create_class("Branch", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, owner, repo, branch):
        """
        Returns a single branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}"
        return model.create_class("Branch", request.get(url, headers=self._headers))

    def protection(self, owner, repo, branch, action=None, **kwargs):
        """
        Gets/Modifies a protection of a branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: specifies the type of action to be made to the given protection.
            If not set, it will return the protection.
            Can be one of `update`, or `remove`; default: None
        If action is update:
        :kwarg required_status_checks:
            :kwarg strict:
            :kwarg contexts:
        :kwarg enforce_admins:
        :kwarg required_pull_request_reviews:
            :kwarg dismissal_rescrictions:
                :kwarg users:
                :kwarg teams:
            :kwarg dismiss_stale_reviews:
            :kwarg require_code_owner_reviews:
            :kwarg required_approving_review_count:
        :kwarg restrictions:
            :kwarg users:
            :kwarg teams:
            :kwarg apps:
        :kwarg required_linear_history:
        :kwarg allow_force_pushes:
        :kwarg allow_deletions:

        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.luke-cage-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection"
        if action == "update":
            return model.create_class(
                "Branch", request.put(url, headers=headers, params=kwargs)
            )
        elif action == "remove":
            return request.delete(url, headers=headers)
        return model.create_class("Branch", request.get(url, headers=headers))

    def required_status_checks(self, owner, repo, branch, action=None, **kwargs):
        """
        Returns/Modifies all required status checks for a branch.

        :param owner:
        :param repo:
        :param branch:
        :kwarg action:

        :kwarg strict:
        :kwarg context: 
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        if action in ["edit", "update"]:
            return model.create_class(
                "RequiredStatusCheck",
                request.patch(url, headers=self._headers, params=kwargs),
            )
        elif action in ["remove", "delete"]:
            return request.delete(url, headers=self._headers)
        return model.create_class(
            "RequiredStatusCheck", request.get(url, headers=self._headers)
        )

    def required_status_checks_contexts(self, owner, repo, branch, action=None, *args):
        """
        Returns all required status checks contexts for a branch.

        :param owner:
        :param repo:
        :param branch:
        :kwarg action:

        :kwarg args:
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        if action == "replace":
            return request.put(url, headers=self._headers, params=args)
        elif action == "create":
            return request.post(url, headers=self._headers, params=args)
        elif action == "remove":
            return request.delete(url, headers=self._headers, params=args)
        return request.get(url, headers=self._headers)

    def pull_request_review(self, owner, repo, branch, action=None, **kwargs):
        """
        Returns/Modifies a pull request review for a protected branch.

        :param owner:
        :param repo:
        :param branch:
        :kwarg action:
        
        If action == update
        :kwarg dismissal_restrictions:
            :kwarg users:
            :kwarg teams:
        :kwarg dismiss_stale_reviews:
        :kwarg require_code_owner_reviews:
        :kwarg required_approving_review_count:
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"

        if action.lower() == "update":
            return model.create_class(
                "PullRequestReview",
                request.put(url, headers=self._headers, params=kwargs),
            )
        elif action.lower() == "remove":
            return request.delete(url, headers=self._headers)

        return model.create_class(
            "PullRequestReview", request.get(url, headers=self._headers)
        )

    def required_signatures(self, owner, repo, branch, action=None):
        """

        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"

        if action in ["add", "create"]:
            return model.create_class(
                "RequiredSignature", request.post(url, headers=self._headers)
            )
        elif action in ["remove", "delete"]:
            return request.delete(url, headers=self._headers)

        return model.create_class(
            "RequiredSignature", request.get(url, headers=self._headers)
        )

    def admin_enforcement(self, owner, repo, branch, action=None):
        """

        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        if action in ["add", "create"]:
            return model.create_class(
                "AdminEnforcement", request.post(url, headers=self._headers)
            )
        elif action in ["remove", "delete"]:
            return request.delete(url, headers=self._headers)

        return model.create_class(
            "AdminEnforcement", request.get(url, headers=self._headers)
        )

    def restrictions(self, owner, repo, branch, action=None):
        """

        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        if action in ["remove", "delete"]:
            return request.delete(url, headers=self._headers)

        return model.create_class(
            "Restrictions", request.get(url, headers=self._headers)
        )

    def teams(self, owner, repo, branch, action=None, **kwargs):
        """

        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        if action in ["replace"]:
            return model.create_class(
                "Teams", request.put(url, headers=self._headers, params=kwargs)
            )
        elif action in ["add", "create"]:
            return model.create_class(
                "Teams", request.post(url, headers=self._headers, params=kwargs)
            )
        elif action in ["remove", "delete"]:
            return model.create_class(
                "Teams", request.delete(url, headers=self._headers, params=kwargs)
            )
        return model.create_class("Teams", request.get(url, headers=self._headers)[0])

    def users(self, owner, repo, branch, action=None, **kwargs):
        """

        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"

        if action == "replace":
            return model.create_class(
                "Users", request.put(url, headers=self._headers, params=kwargs)
            )
        elif action in ["add", "create"]:
            return model.create_class(
                "Users", request.post(url, headers=self._headers, params=kwargs)
            )
        elif action in ["remove", "delete"]:
            return model.create_class(
                "Users", request.delete(url, headers=self._headers, params=kwargs)
            )
        return model.create_class("Users", request.get(url, headers=self._headers))

    def apps(self, owner, repo, branch, action=None, **kwargs):
        """

        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        if action == "replace":
            return model.create_class(
                "Apps", request.put(url, headers=self._headers, params=kwargs)
            )
        elif action in ["add", "create"]:
            return model.create_class(
                "Apps", request.post(url, headers=self._headers, params=kwargs)
            )
        elif action in ["remove", "delete"]:
            return model.create_class(
                "Apps", request.delete(url, headers=self._headers, params=kwargs)
            )
        return model.create_class("Apps", request.get(url, headers=self._headers))
