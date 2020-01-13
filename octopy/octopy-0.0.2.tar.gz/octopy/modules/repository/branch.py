from octopy import request, model


class Branch:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/branches/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Branch
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
        :kwarg required_status_checks: [required] require status checks
            to pass before merging. Set to `null` to disable.
            :kwarg strict: [required] require branches to be up to date
                before merging
            :kwarg contexts: [required] list of status checks to require
                in order to merge this branch
        :kwarg enforce_admins: [required] enforce all configured
            restrictions for administrators. Set to true to 
                enforce required status checks for 
                repository administrators.
                Set to null to disable.
        :kwarg required_pull_request_reviews: [required] 
            Require at least one approving review 
            on a pull request, before merging. Set to null to disable.
            :kwarg dismissal_rescrictions:
                :kwarg users:
                :kwarg teams:
            :kwarg dismiss_stale_reviews:
            :kwarg require_code_owner_reviews:
            :kwarg required_approving_review_count:
        :kwarg restrictions: [required] Restrict who can push 
            to the protected branch. 
            User, app, and team restrictions 
            are only available for organization-owned 
            repositories. Set to null to disable.
            :kwarg users:
            :kwarg teams:
            :kwarg apps:
        :kwarg required_linear_history: Enforces a linear commit Git history, 
            which prevents anyone from pushing merge commits 
            to a branch. Set to true to enforce a linear 
            commit history. Set to false to disable a linear 
            commit Git history. Your repository must allow 
            squash merging or rebase merging before you can 
            enable a linear commit history. Default: false.
             For more information, see "Requiring a linear commit history" 
             in the GitHub Help documentation.
        :kwarg allow_force_pushes: Permits force pushes to 
            the protected branch by anyone with 
            write access to the repository. 
            Set to true to allow force pushes. 
            Set to false or null to block force pushes.
             Default: false. For more information, 
             see "Enabling force pushes to a protected branch" 
             in the GitHub Help documentation.
        :kwarg allow_deletions:
            Allows deletion of the protected branch 
            by anyone with write access to the repository. 
            Set to false to prevent deletion of the protected 
            branch. 
            Default: false. For more information, 
            see "Enabling force pushes to a protected branch" 
            in the GitHub Help documentation.

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

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: type of action to be made, can be `update`, `remove`,
            or not specified, where in the last case will perform
            a get action
        
        if action == update
        :kwarg strict: require branches to be up to date before merging
        :kwarg context: list of status checks to require in order to merge
            into this branch
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        if action.lower() == "update":
            return model.create_class(
                "RequiredStatusCheck",
                request.patch(url, headers=self._headers, params=kwargs),
            )
        elif action.lower() == "remove":
            return model.create_class(
                "Status", request.delete(url, headers=self._headers)
            )
        return model.create_class(
            "RequiredStatusCheck", request.get(url, headers=self._headers)
        )

    def required_status_checks_contexts(self, owner, repo, branch, action=None, *args):
        """
        Returns all required status checks contexts for a branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: can be `replace`, `

        If action == replace/create
        :kwarg args: list with status checks
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

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: type of action to be made, it can be `update`,
            `remove`, or not set, where a get query will be made
        
        If action == update
        :kwarg dismissal_restrictions:
            :kwarg users:
            :kwarg teams:
        :kwarg dismiss_stale_reviews:
        :kwarg require_code_owner_reviews:
        :kwarg required_approving_review_count:
        """
        headers = self._headers().copy()
        headers["Accept"] = "application/vnd.github.luke-cage-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"

        if action.lower() == "update":
            return model.create_class(
                "PullRequestReview", request.put(url, headers=headers, params=kwargs),
            )
        elif action.lower() == "remove":
            return model.create_class(
                "Status", request.delete(url, headers=self._headers)
            )

        return model.create_class(
            "PullRequestReview", request.get(url, headers=headers)
        )

    def required_signatures(self, owner, repo, branch, action=None):
        """
        When authenticated with admin or owner 
        permissions to the repository, you can use 
        this endpoint to check whether a branch requires signed commits.
        
        :param owner:
        :param repo:
        :param branch:
        :kwarg action:
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.zzzax-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"

        if action.lower() == "create":
            return model.create_class(
                "RequiredSignature", request.post(url, headers=self._headers)
            )
        elif action.lower() == "remove":
            return model.create_class(
                "Status", request.delete(url, headers=self._headers)
            )

        return model.create_class(
            "RequiredSignature", request.get(url, headers=self._headers)
        )

    def admin_enforcement(self, owner, repo, branch, action=None):
        """
        Returns/Modifies the admin enforcment of a protected branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: type of action to be made; can be `create`, `remove`,
            or left unchanged, which triggers a get query.
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        if action.lower() == "create":
            return model.create_class(
                "AdminEnforcement", request.post(url, headers=self._headers)
            )
        elif action.lower() == "remove":
            return model.create_class(
                "Status", request.delete(url, headers=self._headers)
            )

        return model.create_class(
            "AdminEnforcement", request.get(url, headers=self._headers)
        )

    def restrictions(self, owner, repo, branch, action=None):
        """
        Lists who has access to this protected branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: can be `remove`, or not set
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        if action.lower() == "remove":
            return model.create_class(
                "Status", request.delete(url, headers=self._headers)
            )

        return model.create_class(
            "Restrictions", request.get(url, headers=self._headers)
        )

    def teams(self, owner, repo, branch, action=None, *args):
        """
        Lists the teams who have push access to this branch. The list includes child teams.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: can be `replace`, `create`, `remove`, or not set, where
            the last means a get query will be made.
        :args: list with strings
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        if action.lower() == "replace":
            response = request.put(url, headers=self._headers, params=args)
        elif action.lower() == "create":
            response = request.post(url, headers=self._headers, params=args)
        elif action.lower() == "remove":
            response = request.delete(url, headers=self._headers, params=args)
        else:
            response = request.get(url, headers=self._headers)
        items = [model.create_class("Team", item) for team in response]
        return items

    def users(self, owner, repo, branch, action=None, *args):
        """
        Lists/Modifies the people who have push access to a given branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: can be `replace`, 'create', `remove`, or not set
        
        :args:
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"

        if action.lower() == "replace":
            response = request.put(url, headers=self._headers, params=args)
        elif action.lower() == "create":
            response = request.post(url, headers=self._headers, params=args)
        elif action.lower() == "remove":
            response = request.delete(url, headers=self._headers, params=args)
        else:
            request.get(url, headers=self._headers)
        items = [model.create_class("User", item) for item in response]
        return items

    def apps(self, owner, repo, branch, action=None, *args):
        """
        Lists the GitHub Apps that have push access to this branch.

        :param owner: owner's name
        :param repo: repo's name
        :param branch: branch's name
        :kwarg action: type of action to be made; can be `replace`,
            `create`, `remove`, or not set, where the last action
            means a get query will be made
        
        :args: list of strings
        """
        url = f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        if action.lower() == "replace":
            response = request.put(url, headers=self._headers, params=args)
        elif action.lower() == "create":
            response = request.post(url, headers=self._headers, params=args)
        elif action.lower() == "remove":
            response = request.delete(url, headers=self._headers, params=args)
        else:
            response = request.get(url, headers=self._headers)

        items = [model.create_class("App", item) for item in response]
        return items
