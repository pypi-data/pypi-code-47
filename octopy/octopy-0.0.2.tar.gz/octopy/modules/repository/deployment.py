from octopy import request, model


class Deployment:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/deployments/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Deployment
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all deployments.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page results to be returned; default: 1
        :kwarg sha: SHA recorded at creation time
        :kwarg ref: name of the ref
        :kwarg task: name of the task
        :kwarg environment: name of the environment
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.ant-man-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/deployments?page={page}"
        items = [
            model.create_class("Deployment", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def get(self, owner, repo, deployment_id, performed_via_github_app=False):
        """
        Returns a single deployment.

        :param owner: owner's name
        :param repo: repo's name
        :param deployment_id: deployment's id
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.ant-man-preview+json"

        if performed_via_github_app:
            headers["Accept"] = "application/vnd.github.machine-man-preview"

        url = f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}"
        return model.create_class("Deployment", request.get(url, headers=headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a deployment.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg ref: [required] ref to deploy
        :kwarg task: specifies a task to execute
        :kwarg auto_merge: ateemts to automatically merge the default branch.
        :kwarg required_contexts: status contexts to verify agains commit status checks
        :kwarg payload: JSON payloads with extra information about the deployment
        :kwarg environment: name for the target deployment environments
        :kwarg description: short description of the deployment
        :kwarg transient_environment: specifies if the given environment is specific
            to the deployment and will no longer exist at some point in
            the future
        :kwarg production_environment: specifies if the given environment is one that
            end-users directly interact with
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.ant-man-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/deployments"
        return model.create_class(
            "Deployment", request.post(url, headers=headers, params=kwargs)
        )

    def statuses(
        self, owner, repo, deployment_id, page=1, environment=False, inactive=False
    ):
        """
        Returns all statused for a deployment.

        :param owner: owner's name
        :param repo: repo's name
        :param deployment_id: deployment's id
        :kwarg page: from which page results to be returned; default: 1
        :kwarg environment: if set to true, the final result will include
            the new environment parameter
        :kwarg inactive: if set to true, it will include in the final
            result, the variables `inactive`, `log_url`, `environment_url`, and
                `auto_inactive`
        """
        headers = self._headers
        if environment or inactive:
            headers = headers.copy()

        if environment:
            headers["Accept"] = "application/vnd.github.flash-preview+json"
        elif inactive:
            headers["Accept"] = "application/vnd.github.ant-man-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}/statuses?page={page}"
        items = [
            model.create_class("Status", item)
            for item in request.get(url, headers=headers)
        ]
        return items

    def status(
        self,
        owner,
        repo,
        deployment_id,
        status_id,
        performed_via_github_app=False,
        environment=False,
        inactive=False,
    ):
        """
        Returns a single status.

        :param owner: owner's name
        :param repo: repo's name
        :param deployment_id: deployment's id
        :param status_id: status's id
        """
        headers = self._headers
        if performed_via_github_app or environment or inactive:
            headers = headers.copy()
        if performed_via_github_app:
            headers["Accept"] = "application/vnd.github.machine-man-preview"
        elif environment:
            headers["Accept"] = "application/vnd.github.flash-preview+json"
        elif inactive:
            headers["Accept"] = "application/vnd.github.ant-man-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}"
        return model.create_class("Status", request.get(url, headers=headers))

    def create_status(self, owner, repo, deployment_id, inactive=False, **kwargs):
        """
        Creates a status.

        :param owner: owner's name
        :param repo: repo's name
        :param deployment_id: deployment's id
        :kwarg inactive: if set to true, it will include in the final
            result, the variables `inactive`, `log_url`, `environment_url`, and
                `auto_inactive`
        :kwarg state: [required] state of the status.
            Can be one of: `error`, `failure`, `inactive`, `in_progress`,
                `queued`, `pending`, or `success`.

                For `inactive` state, you must set `inactive` to true.
                For `in_progress`, and `queued` you must set `environment` to given value, see below
        :kwarg target_url: target's url with which to associate the new state
        :kwarg log_url: full URL of the deployment's output
        :kwarg description: A short description of the status. The maximum description length is 140 characters. Default: ""
        :kwarg environment: Name for the target deployment environment, which can be changed when setting a deploy status.
            Can be set to a boolean (true, or false) when some of the kwargs need a specific custom media type.
        :kwarg environment_url:     Sets the URL for accessing your environment. Default: ""
            Note: This parameter requires you to set `environment` to some value, or to set `environment` to true.
        :kwarg auto_inactive: Adds a new inactive status to all prior non-transient, non-production environment deployments with the same repository and environment name as the created status's deployment. An inactive status is only added to deployments that had a success state. Default: true
            Note: To add an inactive status to production environments, you must set `environment` to a value, or to true
            Note: This parameter requires you to use set `inactive` to true
        """
        headers = self._headers
        environment = kwargs.get("environment")

        if type(environment) == bool:
            del kwargs["environment"]

        if environment or inactive:
            headers = self._headers.copy()

        if environment:
            headers["Accept"] = "application/vnd.github.flash-preview+json"
        elif inactive:
            headers["Accept"] = "application/vnd.github.ant-man-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
        return model.create_class(
            "Status", request.post(url, headers=headers, params=kwargs)
        )
