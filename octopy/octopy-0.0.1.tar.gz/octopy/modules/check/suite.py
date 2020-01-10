from octopy import request as rq, model


class Suite:

    """
    Official GITHUB documentation: https://developer.github.com/v3/checks/suites/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/CheckSuite.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.antiope-preview+json"

    def get(self, owner, repo, check_suite_id):
        """
        Returns a single check suite.

        :param owner: owner's name
        :param repo: repo's name
        :param check_suite_id: check suite's id
        :param ref: ref
        :kwarg page: number of the page from which results to be returned
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-suites/{check_suite_id}"
        return model.create_class("CheckSuite", rq.get(url, headers=self._headers))

    def check_suites(self, owner, repo, check_suite_id, ref, page=1, **kwargs):
        """
        Returns a list of  check suites for a given ref.

        :param owner: owner's name
        :param repo: repo's name
        :param check_suite_id: check suite's id
        :param ref: ref
        :kwarg page: number of the page from which results to be returned
        :kwarg app_id:
        :kwarg check_name:
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{ref}/check-suites?page={page}"
        items = [
            model.create_class("CheckSuite", item)
            for item in rq.get(url, headers=headers, params=kwargs)["check_suites"]
        ]

        return items

    def preferences(self, owner, repo, **kwargs):
        """
        Changes the default automatic flow when creating check suites.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg auto_trigger_checks:
            :kwarg app_id: [required] id of the github app
            :kwarg setting: [required] Set to true 
                to enable automatic creation of 
                CheckSuite events upon pushes to the repository, 
                or false to disable them. Default: true
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-suites/preferences"
        return model.create_class(
            "Preference", rq.patch(url, headers=self._headers, params=kwargs)
        )

    def create(self, owner, repo, **kwargs):
        """
        Creates a check suite.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg head_sha: head's sha
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-suites"
        return model.create_class(
            "CheckSuite", rq.post(url, headers=self._headers, params=kwargs)
        )

    def request(self, owner, repo, check_suite_id):
        """
        Triggers GitHub to rerequest an existing check suite, 
        without pushing new code to a repository.

        :param owner: owner's name
        :param repo: repo's name
        :param check_suite_id: check suite's id
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"
        )
        return model.create_class("Status", rq.post(url, headers=self._headers))
