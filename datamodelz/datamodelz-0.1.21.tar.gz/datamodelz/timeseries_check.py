import logging
from . import rule
from .timeseries_metadata import TimeseriesMetadataField
from .data_list import DataList
from .field import Field


class TimeseriesCheck(Field):
    def __init__(self):
        """
        :param metadata_names:
        :param rules: list of Rule objects
        """
        super().__init__()
        self.name = "Timeseries Check"
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
        self.metadata.rules = []  # default
        self.set_fields(self.fields)
        logging.debug("TimeseriesCheck: data field is set as {}".format(self.data))
        return self.errors

    def run_check(self, new_check, metadata_names=[]):
        """
        Returns errors only from that check
        :param new_check:
        :param metadata_names:
        :return:
        """
        self.metadata.rules = [rule.has_field(name) for name in metadata_names]
        errors = self.validate_field(self.metadata)  # automatically adds new errors to self.errors
        if errors:  # new errors from check
            return
        error = new_check.run(self.data.value, self.metadata)
        if error:
            self.error("Failed check {}: {}".format(new_check.name, error))
        return


