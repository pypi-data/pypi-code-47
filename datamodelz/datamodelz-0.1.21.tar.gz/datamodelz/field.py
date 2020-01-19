import copy
from datetime import timedelta
import logging
from dateutil.relativedelta import relativedelta
from dateutil import parser
from .consts import daily_string, weekly_string, monthly_string, quarterly_string, \
    annually_string, frequency_to_delta
from . import rule
import datetime
import pytz

utc = pytz.UTC
max_value = 1000 * 1000 * 1000 * 1000
max_delay = 1000 * 1000 * 1000 * 1000 * 1000 * 1000
value_default = None


class Field:
    def __init__(self):
        self.name = ""
        self.valid = False
        self.value = value_default
        self.rules = []
        self.errors = []
        self.fields = []

    def set(self, value):
        self.value = value
        return  # returns any errors

    def set_field(self, field, value):
        # for objects with field objects inside of them
        # bubbles up the errors
        field.set(value)
        return

    def set_fields(self, fields):
        # if using this then can run validate early bc field validation included
        # if not necessarily calling ste field on every field then must validate explicitly
        for field in fields:
            found_value = self.find_field(field)
            if found_value is not None:  # found_value may equal False
                self.set_field(field, found_value)
        return

    def get_field(self, name: str):
        for field in self.fields:
            if field.name == name:
                return field
        return

    def get_fields(self, names: list):
        fields = []
        for field in self.fields:
            if field.name in names:
                fields.append(field)
        return fields

    def find_field(self, field):
        if field.name in self.value:
            return self.value[field.name]
        else:
            self.error("field {} not found in object {}".format(field.name, self.name))
        return ""

    def run_rules(self):
        for rule in self.rules:
            ok = rule.run(self.value)
            if not ok:
                if self.value is None:
                    self.error("{} does not exist".format(self.name))
                if type(self.value) == str and self.value == '':
                    self.error("{} is empty".format(self.name))
                elif type(self.value) in [str, int, bool]:
                    self.error("{}='{}' {}".format(self.name, self.value, rule.error))
                else:
                    self.error("{} {}".format(self.name, rule.error))
                return
        return

    def validate(self) -> list:
        """
        :param:
        :return: errors: list
        """
        self.run_rules()
        if self.errors:
            return self.errors
        self.validate_fields(self.fields)
        if not self.errors:
            self.valid = True
        return self.errors

    def validate_field(self, field) -> list:
        """
        :param: field: the actual field in the object
        :return: errors: list
        """
        error = field.validate()
        self.error_many(error)
        return error

    def validate_fields(self, fields):
        for field in fields:
            self.validate_field(field)
        return

    def error(self, msg: str):
        if msg not in self.errors:
            logging.error(msg)  # ERROR:root:error message
            self.errors.append(msg)
        return

    def error_many(self, msgs: list):
        if msgs:
            self.errors += msgs
        return

    def copy(self):
        return copy.deepcopy(self)

class BaseTypeField(Field):
    def __init__(self):
        super().__init__()
        self.value = value_default
        self.rules = []
        self.errors = []

    def __lt__(self, other):
        if isinstance(other, BaseTypeField):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, BaseTypeField):
            return self.value <= other.value
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BaseTypeField):
            return self.value == other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, BaseTypeField):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, BaseTypeField):
            return self.value >= other.value
        return NotImplemented

class PosIntField(BaseTypeField):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = int
        self.value = value_default
        self.rules = [rule.not_none, rule.type_int, rule.gte(0), rule.lte(max_value)]


class IntField(BaseTypeField):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = int
        self.value = value_default
        self.rules = [rule.not_none, rule.type_int, rule.gte(-max_value), rule.lte(max_value)]


class FloatField(BaseTypeField):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = float
        self.value = value_default
        self.rules = [rule.not_none, rule.type_float, rule.gte(-max_value), rule.lte(max_value)]

    def __add__(self, other):
        # polymorphic
        if isinstance(other, self.__class__):
            self.value + other.value
            return self
        if type(other) is int:
            self.value + other
            return self
        if type(other) is float:
            self.value + other
            return self
        return NotImplemented

    def __sub__(self, other):
        # polymorphic
        if isinstance(other, self.__class__):
            self.value - other.value
            return self
        if type(other) is int:
            self.value - other
            return self
        if type(other) is float:
            self.value - other
            return self
        return NotImplemented


class BigIntField(IntField):
    def __init__(self, name):
        super().__init__(name)
        self.rules = [rule.not_none, rule.type_int, rule.gte(0), rule.lte(max_delay)]

    def set(self, value):
        try:
            num = int(value)
            self.value = num
        except:
            self.error("cannot parse value {} as int".format(value))


class BoolField(BaseTypeField):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = bool
        self.value = value_default
        self.rules = [rule.not_none, rule.type_bool]


class StringField(BaseTypeField):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = str
        self.value = ""
        self.rules = [rule.not_none, rule.type_str, rule.len_gt(0), rule.len_lt(200)]


class EnumField(StringField):
    def __init__(self, name: str, names: list):
        super().__init__(name)
        self.rules = [rule.in_field(names)]


class URLField(StringField):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.rules = [rule.not_none, rule.type_str, rule.type_url]


class HttpsField(StringField):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.rules = [rule.not_none, rule.type_str, rule.type_https]


class DomainField(StringField):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.rules = [rule.not_none, rule.type_str, rule.type_domain]  # TODO: add normalizer rules


class TickerField(StringField):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.rules = [rule.not_none, rule.type_str, rule.type_ticker]


class DateField(BaseTypeField):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.value = datetime.datetime(1000, 1, 1)
        self.rules = []

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value.replace(tzinfo=utc) < other.value.replace(tzinfo=utc)
        if type(other) == datetime.datetime:
            return self.value.replace(tzinfo=utc) < other.replace(tzinfo=utc)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.value.replace(tzinfo=utc) <= other.value.replace(tzinfo=utc)
        if type(other) == datetime.datetime:
            return self.value.replace(tzinfo=utc) <= other.replace(tzinfo=utc)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value.replace(tzinfo=utc) == other.value.replace(tzinfo=utc)
        if type(other) == datetime.datetime:
            return self.value.replace(tzinfo=utc) == other.replace(tzinfo=utc)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.value.replace(tzinfo=utc) > other.value.replace(tzinfo=utc)
        if type(other) == datetime.datetime:
            return self.value.replace(tzinfo=utc) > other.replace(tzinfo=utc)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.value.replace(tzinfo=utc) >= other.value.replace(tzinfo=utc)
        if type(other) == datetime.datetime:
            return self.value.replace(tzinfo=utc) >= other.replace(tzinfo=utc)
        return NotImplemented

    def __add__(self, other):
        # polymorphic
        new = self.copy()
        if isinstance(other, self.__class__):
            new.value = self.value.replace(tzinfo=utc) + other.value.replace(tzinfo=utc)
            return new
        if type(other) == datetime.datetime:
            new.value = self.value.replace(tzinfo=utc) + other.replace(tzinfo=utc)
            return new
        if type(other) == timedelta:
            new.value = self.value.replace(tzinfo=utc) + other
            return new
        if type(other) == relativedelta:
            new.value = self.value.replace(tzinfo=utc) + other
            return new
        if type(other) is str and other in frequency_to_delta:
            new.value = self.value.replace(tzinfo=utc) + self.convert_frequency(other)
            return new
        return NotImplemented

    def __sub__(self, other):
        # polymorphic
        new = self.copy()
        if isinstance(other, self.__class__):
            new.value = self.value.replace(tzinfo=utc) - other.value.replace(tzinfo=utc)
            return new
        if type(other) == datetime.datetime:
            new.value = self.value.replace(tzinfo=utc) - other.replace(tzinfo=utc)
            return new
        if type(other) == timedelta:
            new.value = self.value.replace(tzinfo=utc) - other
            return new
        if type(other) == relativedelta:
            new.value = self.value.replace(tzinfo=utc) - other
            return new
        if type(other) is str and other in frequency_to_delta:
            new.value = self.value.replace(tzinfo=utc) - self.convert_frequency(other)
            return new

    def get_date(self):
        return self.value.date()

    def set(self, value):
        try:
            date = parser.parse(value)  # 2016-05-15T00:00:00Z
            # date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.Z') # 2019-03-22T14:20:58.003Z
        except ValueError as err:
            self.error("Cannot parse date {}".format(value))
            return
        self.value = date
        self.run_rules()
        return self.errors

    def after(self, other_date):
        # self.value > other.value
        val1 = self.value.replace(tzinfo=utc)
        val2 = other_date.value.replace(tzinfo=utc)
        return val1 > val2

    def before(self, other_date):
        # self.value < other.value
        val1 = self.value.replace(tzinfo=utc)
        val2 = other_date.value.replace(tzinfo=utc)
        return val1 < val2

    @staticmethod
    def convert_frequency(frequency) -> datetime.timedelta:
        if type(frequency) == EnumField:
            frequency = frequency.value
        if frequency in frequency_to_delta:
            return frequency_to_delta[frequency]
        return relativedelta(days=0)

    def add_frequency(self, frequency: str):
        # Shallow Add. Returns a copy. Does not affect the original.
        new = self.copy()
        new.value = self.value.replace(tzinfo=utc) + self.convert_frequency(frequency)
        return new

    def subtract_frequency(self, frequency: str):
        # Shallow Add. Returns a copy. Does not affect the original.
        new = self.copy()
        new.value = self.value.replace(tzinfo=utc) - self.convert_frequency(frequency)
        return new

