import slack
import logging
from prefect import Task
from datetime import date, timedelta, datetime
from prefect.utilities.tasks import defaults_from_attrs


def get_field(dct: dict, name):
    """
    Will check & get field via name
    :param dct: dict
    :param name: any key stored in a dictionary
    :return: any value stored in a dictionary
    """
    if type(dct) == dict and name in dct:
        return dct[name]
    return


def get_errors(errors, i) -> list:
    error_list = get_field(errors[i], "error")
    if type(error_list) == str:
        return [error_list]
    return error_list


def get_service_id(service_ids, i) -> str:
    service_id = ""
    if len(service_ids) > i and "error" not in service_ids[i]:
        service_id = service_ids[i]
    return service_id


class MakeErrorTask(Task):
    def __init__(self, token, titles=None, max_retries=3, retry_delay=timedelta(minutes=1)):
        """
        :param titles:
        :param key: Slack Token to be used in slack.WebClient()
        """
        super().__init__(max_retries, retry_delay)
        self.name = "Make Error"
        self.titles = titles
        self.slack_client = slack.WebClient(token=token)

        # set automatically
        self.problems = []
        self.date = str(date.today())
        self.time = str(datetime.now().time())
        self.file = "results.csv"
        self.file_header = "Central Authority ID, Service ID, Errors"
        self.length = 0

    def make_file_name(self, titles: list) -> None:
        """
        Creates file name ex: datasys_kelvin_set_20190803.csv
        :param titles: list of strings
        :return: None
        """
        if titles:
            self.titles = titles
        title = "_".join(self.titles).lower().replace(" ", "_")
        self.file = "{}_{}.csv".format(title, self.date.replace("-", ""))
        return

    def make_list(self, errors: list, ca_ids: list, service_ids=[]) -> None:
        """
        :param errors: list of strings
        :param ca_ids: list of strings
        :param service_ids: list of strings (optional)
        :return: None
        """
        self.length = len(errors)  # so we how out of how many
        for i in range(0, len(errors)):
            error_list = get_errors(errors, i)
            if not error_list:
                continue
            service_id = get_service_id(service_ids, i)
            lst = [ca_ids[i], service_id] + error_list
            self.problems.append(lst)
        return

    def make_file(self) -> None:
        """
        requires: self.file, self.file_header, self.problems
        :return: None
        """
        if not self.problems:
            return
        with open(self.file, "w+") as csv:
            csv.write("Date, Time, Set Description\n")
            csv.write(','.join([self.date, self.time, ' '.join(self.titles), "\n\n"]))
            csv.write(self.file_header)
            for lst in self.problems:
                try:
                    csv.write("\n")
                    csv.write(",".join(lst))
                except:
                    logging.error("cannot print problems list {}".format(lst))
                    continue
        return

    def success_alert(self) -> bool:
        """
        :return: bool: ran ok
        """
        response = self.slack_client.chat_postMessage(
            channel='#prefect-data-alerts',
            text=":smile: New Alert from `{}` there are {} errors (out of {})"
                .format(" ".join(self.titles), len(self.problems), self.length),
        )
        return response["ok"]

    def failure_alert(self) -> bool:
        """
        :return: bool: ran ok
        """
        response = self.slack_client.files_upload(
            channels='#prefect-data-alerts',
            file=self.file,
            filename=self.file,
            filetype="csv",
            initial_comment=":frowning: New Alert from `{}` there are {} errors (out of {})"
                .format(" ".join(self.titles), len(self.problems), self.length),
            title=self.file
        )
        return response["ok"]

    @defaults_from_attrs('titles')
    def run(self, titles=None, errors=[], ca_ids=[], service_ids=[]) -> bool:
        """
        :param key: slack key
        :param titles:
        :param errors: list of strings
        :param ca_ids: list of strings
        :param service_ids: list of strings (optional)
        :return: bool: the run was successful & no errors
        """
        self.make_file_name(titles)
        self.make_list(errors, ca_ids, service_ids)
        if self.problems:
            self.make_file()
            self.failure_alert()
            return False
        else:
            self.success_alert()
            return True


class MakeGenericErrorTask(MakeErrorTask):
    def __init__(self, token, titles=None, max_retries=3, retry_delay=timedelta(minutes=1)):
        """
        :param titles: list of strings describing the check
        :param key: slack key
        """
        super().__init__(token, titles, max_retries, retry_delay)
        self.name = "Make Generic Error"
        self.titles = titles
        self.slack_client = slack.WebClient(token=token)

        # set automatically
        self.problems = []
        self.date = str(date.today())
        self.time = str(datetime.now().time())
        self.file = "results.csv"
        self.file_header = "Service ID, Errors"

    def make_list(self, errors: list, service_ids=[]) -> None:
        """
        :param errors: list of strings
        :param service_ids: list of strings
        :return: None
        """
        self.length = len(errors)  # so we how out of how many
        for i in range(0, len(errors)):
            error_list = get_errors(errors, i)
            if not error_list:
                continue
            service_id = get_service_id(service_ids, i)
            lst = [service_id] + error_list
            self.problems.append(lst)
        return

    @defaults_from_attrs('titles')
    def run(self, titles=None, errors=[], service_ids=[]) -> bool:
        """
        :param titles:
        :param headers:
        :param errors: list of strings
        :param service_ids: list of strings (optional)
        :return: bool
        """
        self.make_file_name(titles)
        self.make_list(errors, service_ids)
        if self.problems:
            self.make_file()
            self.failure_alert()
            return False
        self.success_alert()
        return True
