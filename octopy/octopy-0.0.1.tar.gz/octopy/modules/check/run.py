from octopy import request, model


class Run:

    """
    Official GITHUB documentation: https://developer.github.com/v3/checks/runs/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/CheckRun.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.antiope-preview+json"

    def create(self, owner, repo, **kwargs):
        """
        Creates a new check run for a specific commit in a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg name: [required] name of the check
        :kwarg head_sha: [required] sha of the commit
        :kwarg details_url: url of the integrator's site having the full
            details of the check
        :kwarg external_id: reference for the run on the integrator's system
        :kwarg status: current status
        :kwarg started_at: time that the check run began
        :kwarg conclusion: [required if completed_at or status of completed is set].
            represtens the final conclusion of the check
        :kwarg completed_at: time at which the check completed
        :kwarg output:
            An object, which can contain the following fields:
            :kwarg title: [required] title of the check run
            :kwarg summary: [required] summary of the check run
            :kwarg text: details of the check run
            :kwarg annotations: array of the following objects
                An object, which can contain the following fields:
                :kwarg path: [required] path of the file to which annotation to be added
                :kwarg start_line: [required] start line of the annotation
                :kwarg end_line: [required] end line of the annotation
                :kwarg start_column: start column of the annotaion
                :kwarg end_column: end column of the annotation
                :kwarg annotation_level: [required] level of the annotation
                :kwarg message: [required] short description of the feedback
                :kwarg title: title of the annotation
                :kwarg raw_details: details about the annotation
            :kwarg images:
                An object, which can contain the following fields:
                    :kwarg alt: [required] alternative text for the image
                    :kwarg image_url: [required] full url image
                    :kwarg caption: short image description
        :kwarg actions:
            An object, which can contain the following fields:
            :kwarg label: [required] text to be displayed on a button in the web UI.
            :kwarg description: [required] short explanation of what this action would do
            :kwarg identifier: [required] reference for the action
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-runs"
        return model.create_class(
            "CheckRun", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, check_run_id, **kwargs):
        """
        Updates a check run for a specific commit in a repository.

        :param owner: owner's name
        :param repo: repo's name
        :param check_run_id: check run's id
        :kwarg name: [required] name of the check
        :kwarg head_sha: [required] sha of the commit
        :kwarg details_url: url of the integrator's site having the full
            details of the check
        :kwarg external_id: reference for the run on the integrator's system
        :kwarg status: current status
        :kwarg started_at: time that the check run began
        :kwarg conclusion: [required if completed_at or status of completed is set].
            represtens the final conclusion of the check
        :kwarg completed_at: time at which the check completed
        :kwarg output:
            An object, which can contain the following fields:
            :kwarg title: [required] title of the check run
            :kwarg summary: [required] summary of the check run
            :kwarg text: details of the check run
            :kwarg annotations: array of the following objects
                An object, which can contain the following fields:
                :kwarg path: [required] path of the file to which annotation to be added
                :kwarg start_line: [required] start line of the annotation
                :kwarg end_line: [required] end line of the annotation
                :kwarg start_column: start column of the annotaion
                :kwarg end_column: end column of the annotation
                :kwarg annotation_level: [required] level of the annotation
                :kwarg message: [required] short description of the feedback
                :kwarg title: title of the annotation
                :kwarg raw_details: details about the annotation
            :kwarg images:
                An object, which can contain the following fields:
                    :kwarg alt: [required] alternative text for the image
                    :kwarg image_url: [required] full url image
                    :kwarg caption: short image description
        :kwarg actions:
            An object, which can contain the following fields:
            :kwarg label: [required] text to be displayed on a button in the web UI.
            :kwarg description: [required] short explanation of what this action would do
            :kwarg identifier: [required] reference for the action
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}"
        return model.create_class(
            "CheckRun", request.patch(url, headers=self._headers, params=kwargs)
        )

    def check_runs(self, owner, repo, ref, page=1, **kwargs):
        """
        Returns all check runs for a commit ref.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: ref
        :kwarg page: number of the page, from which results to be returned.
        :kwarg check_name: returns check runs with specified name
        :kwarg status: returns check runs with specified status
        :kwarg filter: filters check runs by their completed_at timestamp.
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{ref}/check-runs?page={page}"
        items = [
            model.create_class("CheckRun", item)
            for item in request.get(url, headers=self._headers, params=kwargs)[
                "check_runs"
            ]
        ]

        return items

    def check_suite(self, owner, repo, check_suite_id, page=1, **kwargs):
        """
        Returns check runs for a specific check suite.

        :param owner: owner's name
        :param repo: repo's name
        :param check_suite_id: check suite's id
        :kwarg page: number of the page from which results to be returned,
            by default is set to 1.
        :kwarg check_name: returns check runs by specified name.
        :kwarg status: returns check runs by specified status.
        :kwarg filter: filters check runs by their completed_at timestamp.
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs?page={page}"
        items = [
            model.create_class("CheckRun", item)
            for item in request.get(url, headers=self._headers, params=kwargs)[
                "check_runs"
            ]
        ]

        return items

    def get(self, owner, repo, check_run_id):
        """
        Returns a single check run.

        :param owner: owner's name
        :param repo: repo's name
        :param check_run_id: check run's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}"

        return model.create_class("CheckSuite", request.get(url, headers=self._headers))

    def annotations(self, owner, repo, check_run_id, page=1):
        """
        Returns annotations for a check run.

        :param owner: owner's name 
        :param repo: repo's name
        :param check_run_id: check run's id
        :kwarg page: number of the page, from which results to be returned
        """
        url = f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations?page={page}"
        items = [
            model.create_class("CheckRun", item)
            for item in request.get(url, headers=self._headers)
        ]

        return items
