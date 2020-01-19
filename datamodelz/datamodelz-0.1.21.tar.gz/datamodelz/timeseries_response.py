import logging
from . import rule
from .field import Field
from .timeseries_metadata import TimeseriesMetadataField
from .data_list import DataList


class TimeseriesResponseField(Field):
    def __init__(self):
        super().__init__()
        self.name = "response"
        self.value = {}

        self.metadata = TimeseriesMetadataField()
        self.data = DataList()
        self.fields = [self.metadata, self.data]  # will add fields when needed for use case
        self.rules = [rule.has_field(x.name) for x in self.fields]

    def set(self, value):
        self.value = value
        self.run_rules()
        if self.errors:  # returns any errors
            return self.errors
        self.set_fields(self.fields)  # default is empty
        logging.debug("TimeseriesResponseField: data field is set as {}".format(self.data))
        return self.errors

    def run_checks(self, checks: list) -> list:
        """
        :param check: list(rule.Rule)
        :return: list of errors
        running rules on list of TimeseriesObjectField
        bubble up errors
        """
        for check in checks:
            ok = check.run(self.data.data)
            if not ok:
                self.error("{} failed check {}".format(self.name, check.name))
        return self.errors
