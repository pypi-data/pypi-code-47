import re
import json
import random

from faker import Faker

from jdog.node import PropertyNode, ScalarNode, PlaceholderNode, ObjectNode, ArrayNode, RangeNode
from jdog.placeholder.name import NamePlaceholder, NamePlaceholderOption
from jdog.placeholder.option import OptionPlaceholder
from jdog.placeholder.placeholder import FuncPlaceholder, FuncStrPlaceholder
from jdog.placeholder.range import RangePlaceholder


class NoMatchingPlaceholder(Exception):
    """Raised when no matching placeholder was found."""

    def __init__(self, token):
        super().__init__(f'No matching placeholder for {token} found.')
        self.token = token


class SchemeParser:
    """
        Parsing provided scheme and construct node structure for later data generation.
        Defines predefined placeholders.

        :var faker faker: Faker instance with provided language
        :var boolean strict: If parser should raise :class:`.NoMatchingPlaceholder`
    """

    NAME = 'name'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    CITY = 'city'
    STREET_ADDRESS = 'street_address'
    AGE = 'age'
    NUMBER = 'number'
    LOREM = 'lorem'
    OPTION = 'option'
    EMPTY = 'empty'
    RANGE = 'range'
    BOOL = 'bool'

    def __init__(self, lang='en-US', strict=False):
        self.faker = Faker(lang)
        self.strict = strict
        self.compiled_matchers = {
            SchemeParser.NAME: re.compile(r'^{{name\(?([f,m]?)\)?}}$'),
            SchemeParser.FIRST_NAME: re.compile(r'^{{first_name\(?([f,m]?)\)?}}$'),
            SchemeParser.LAST_NAME: re.compile(r'^{{last_name\(?([f,m]?)\)?}}$'),
            SchemeParser.CITY: re.compile('^{{city}}$'),
            SchemeParser.STREET_ADDRESS: re.compile('^{{street_address}}$'),
            SchemeParser.AGE: re.compile('^{{age}}$'),
            SchemeParser.NUMBER: re.compile(r'^{{number\((.*)\)}}$'),
            SchemeParser.LOREM: re.compile(r'^{{lorem\((.*)\)}}$'),
            SchemeParser.OPTION: re.compile(r'^{{option\((.*)\)}}$'),
            SchemeParser.EMPTY: re.compile(r'^{{empty}}$'),
            SchemeParser.RANGE: re.compile(r'^{{range\((.*)\)}}$'),
            SchemeParser.BOOL: re.compile(r'^{{bool}}$')
        }
        self.matchers = {
            SchemeParser.NAME: lambda token: self.compiled_matchers[SchemeParser.NAME].match(token),
            SchemeParser.FIRST_NAME: lambda token: self.compiled_matchers[SchemeParser.FIRST_NAME].match(token),
            SchemeParser.LAST_NAME: lambda token: self.compiled_matchers[SchemeParser.LAST_NAME].match(token),
            SchemeParser.CITY: lambda token: self.compiled_matchers[SchemeParser.CITY].match(token),
            SchemeParser.STREET_ADDRESS: lambda token: self.compiled_matchers[SchemeParser.STREET_ADDRESS].match(token),
            SchemeParser.AGE: lambda token: self.compiled_matchers[SchemeParser.AGE].match(token),
            SchemeParser.NUMBER: lambda token: self.compiled_matchers[SchemeParser.NUMBER].match(token),
            SchemeParser.LOREM: lambda token: self.compiled_matchers[SchemeParser.LOREM].match(token),
            SchemeParser.OPTION: lambda token: self.compiled_matchers[SchemeParser.OPTION].match(token),
            SchemeParser.EMPTY: lambda token: self.compiled_matchers[SchemeParser.EMPTY].match(token),
            SchemeParser.RANGE: lambda token: self.compiled_matchers[SchemeParser.RANGE].match(token),
            SchemeParser.BOOL: lambda token: self.compiled_matchers[SchemeParser.BOOL].match(token),
        }
        self.placeholders = {
            SchemeParser.NAME:
                lambda token, args: self._placeholder_name(token, args),
            SchemeParser.FIRST_NAME:
                lambda token, args: self._placeholder_first_name(token, args),
            SchemeParser.LAST_NAME:
                lambda token, args: self._placeholder_last_name(token, args),
            SchemeParser.CITY:
                lambda token, _: FuncStrPlaceholder(token, _, lambda __: self.faker.city()),
            SchemeParser.STREET_ADDRESS:
                lambda token, _: FuncStrPlaceholder(token, _, lambda __: self.faker.street_address()),
            SchemeParser.AGE:
                lambda token, _: FuncPlaceholder(token, _, lambda __: random.randint(1, 99)),
            SchemeParser.NUMBER:
                lambda token, args: FuncPlaceholder(token, args, lambda xargs: random.randint(int(xargs[0]), int(xargs[1]) - 1)),
            SchemeParser.LOREM:
                lambda token, args: FuncStrPlaceholder(token, args, lambda xargs: self.faker.sentence(nb_words=int(xargs[0]))),
            SchemeParser.OPTION:
                lambda token, args: OptionPlaceholder(token, args),
            SchemeParser.EMPTY:
                lambda token, _: FuncStrPlaceholder(token, _, lambda __: ''),
            SchemeParser.RANGE:
                lambda token, args: RangePlaceholder(token, args),
            SchemeParser.BOOL:
                lambda token, _: FuncStrPlaceholder(token, _, lambda __: str(random.random() > 0.5).lower())
        }

    def _placeholder_name(self, token, args):
        if args and args[0] == 'm':
            return NamePlaceholder(token, self.faker, NamePlaceholderOption.GENDER_MALE)
        elif args and args[0] == 'f':
            return NamePlaceholder(token, self.faker, NamePlaceholderOption.GENDER_FEMALE)

        return NamePlaceholder(token, self.faker)

    def _placeholder_first_name(self, token, args):
        if args and args[0] == 'm':
            return NamePlaceholder(token, self.faker,
                                   option=NamePlaceholderOption.FIRST_NAME | NamePlaceholderOption.GENDER_MALE)
        elif args and args[0] == 'f':
            return NamePlaceholder(token, self.faker,
                                   option=NamePlaceholderOption.FIRST_NAME | NamePlaceholderOption.GENDER_FEMALE)
        return NamePlaceholder(token, self.faker, option=NamePlaceholderOption.FIRST_NAME)

    def _placeholder_last_name(self, token, args):
        if args and args[0] == 'm':
            return NamePlaceholder(token, self.faker,
                                   option=NamePlaceholderOption.LAST_NAME | NamePlaceholderOption.GENDER_MALE)
        elif args and args[0] == 'f':
            return NamePlaceholder(token, self.faker,
                                   option=NamePlaceholderOption.LAST_NAME | NamePlaceholderOption.GENDER_FEMALE)
        return NamePlaceholder(token, self.faker, option=NamePlaceholderOption.LAST_NAME)

    @staticmethod
    def _parse_arguments(p):
        pattern = r'([^,]+\(.+?\)}})|([^,]+)'
        matches = re.findall(pattern, p)

        return [x[0] if x[0] != '' else x[1] for x in matches]

    @staticmethod
    def _is_like_token(arg):
        return re.match(r'^{{?.*}?}$', arg)

    def _match_token(self, token):
        for key in self.matchers:
            m = self.matchers[key](str(token))

            if m is None:
                continue

            args = []
            if len(m.groups()) > 0:
                parsed_args = self._parse_arguments(m.group(1))
                # parse args to placeholders
                for arg in parsed_args:
                    if self._is_like_token(arg):
                        args.append(self._sub_parse(arg))
                    else:
                        args.append(arg)

            return self.placeholders[key](token, args)

        if self.strict and self._is_like_token(token):
            raise NoMatchingPlaceholder(token)
        else:
            return None

    def add_matcher(self, key, f_matcher, f_placeholder):
        """
            Add new matcher for returning new placeholder

        :param key: Unique matcher key. If provided existing one, old behavior is replaced.
        :param f_matcher: Function which takes one str argument.
            Should return re.Match object or None if no match found.
        :param f_placeholder: Function which takes accepted token and its parsed arguments - if present.
            Should return one of :class:`~jdog.placeholder.placeholder.Placeholder` object.
        """

        self.matchers[key] = f_matcher
        self.placeholders[key] = f_placeholder

    def placeholder_keys(self):
        """
            Defined placeholder keys

        :return: Defined placeholder keys
        :rtype: list
        """
        return self.placeholders.keys()

    def _sub_parse(self, sub):
        if isinstance(sub, list):
            array = []
            for x in sub:
                array.append(self._sub_parse(x))
            return ArrayNode(array)
        elif isinstance(sub, dict):
            props = []
            for key in sub:
                # Key could be token
                placeholder = self._match_token(key)
                if placeholder is None:
                    props.append(PropertyNode(ScalarNode(key), self._sub_parse(sub[key])))
                else:
                    # special case for RangePlaceholder
                    if isinstance(placeholder, RangePlaceholder):
                        props.append(RangeNode(placeholder.prop, placeholder.low, self._sub_parse(sub[key]),
                                               placeholder.high if hasattr(placeholder, 'high') else None))
                    else:
                        props.append(PropertyNode(PlaceholderNode(placeholder), self._sub_parse(sub[key])))
            return ObjectNode(props)
        else:
            placeholder = self._match_token(sub)
            if placeholder is None:
                return ScalarNode(sub)
            else:
                return PlaceholderNode(placeholder)

    def parse(self, scheme):
        """
            Parse given scheme and return node structure representation of the scheme.

        :param str scheme: Scheme to parse
        :return: Node structure representing current scheme
        """
        js = json.loads(scheme)
        return self._sub_parse(js)

