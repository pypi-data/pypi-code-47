"""Concise checker definition for Pylint."""

import collections
import hashlib
import typing as t

import astroid
import attr
import pylint.checkers.utils
import pylint.interfaces
from public import public


@attr.s(auto_attribs=True, frozen=True, order=False)
class ProblemID:
    prefix: str
    base: int
    number: int

    def __str__(self):
        return f"{self.prefix}{self.base:02d}{self.number:02d}"


class FormattingString(collections.UserString):
    def __mod__(self, other):

        try:
            return str(self) % other
        except TypeError:
            return NotImplemented


class FormattableDict:
    def __init__(self, *args, **kwargs):
        self.data = dict(*args, **kwargs)

    def __rmod__(self, string: str):
        return string.format_map(self.data)


@attr.s(auto_attribs=True, frozen=True, order=False)
class Problem:
    name: str
    text: FormattingString = attr.ib(converter=FormattingString)
    explanation: str
    id: ProblemID


ProblemT = t.TypeVar("ProblemT", bound=Problem)


@attr.s(auto_attribs=True, frozen=True, order=False)
class Message(t.Generic[ProblemT]):
    problem: ProblemT
    node: astroid.node_classes.NodeNG
    data: t.Dict[str, t.Any]

    def to_pylint(self):
        return str(self.problem.id) + " " + self.node


CheckerFunction = t.Callable[
    [pylint.checkers.BaseChecker, astroid.node_classes.NodeNG],
    t.Iterable[Message[ProblemT]],
]


@attr.s(auto_attribs=True, frozen=True, order=False)
class Checker:
    node_type: t.Type[astroid.node_classes.NodeNG]
    function: CheckerFunction
    problems: t.Iterable[Problem]


def make_checker(
    node_type: t.Type[astroid.node_classes.NodeNG], problems: t.Sequence[Problem]
) -> t.Callable:
    def wrapper(function: CheckerFunction) -> Checker:
        return Checker(node_type, function, tuple(problems))

    return wrapper


def short_hash(name: str, length: int = 2) -> int:
    integer = int.from_bytes(hashlib.md5(name.encode()).digest(), "big")
    return int(str(integer)[:length])


@public
@attr.s(auto_attribs=True, order=False)
class CheckerGroup:
    name: str
    checkers: t.List[Checker] = attr.ib(factory=list)
    problems: t.Dict[str, Problem] = attr.ib(factory=dict)

    id_prefix: str = "E"

    def problem(self, name: str, text: str, explanation: str):
        problem_id = ProblemID(self.id_prefix, short_hash(self.name), short_hash(name))
        problem = Problem(name, text, explanation, problem_id)
        # pylint: disable=unsupported-assignment-operation
        self.problems[problem.name] = problem
        return problem

    def check_for_problems(
        self,
        node_type: t.Type[astroid.node_classes.NodeNG],
        problems: t.Sequence[Problem],
    ):
        def wrapper(function):
            checker = make_checker(node_type, problems)(function)
            self.checkers.append(checker)
            return checker.function

        return wrapper

    def standalone_check(
        self, node_type: t.Type[astroid.node_classes.NodeNG], text: str
    ):
        def wrapper(function):
            problem = self.problem(
                name=function.__name__.replace("_", "-"),
                text=text,
                explanation=function.__doc__ or "",
            )

            checker = make_checker(node_type, [problem])(
                _add_problem_to_emitted_messages(function, problem)
            )
            self.checkers.append(checker)
            return checker.function

        return wrapper


def _add_problem_to_emitted_messages(function, problem):
    def wrap(*args, **kwargs):
        for msg in function(*args, **kwargs):
            yield attr.evolve(msg, problem=problem)

    return wrap


def _make_multicaller(checkers: t.Iterable[Checker]):
    @pylint.checkers.utils.check_messages(
        *[problem.name for checker_ in checkers for problem in checker_.problems]
    )
    def _call_each(
        self: pylint.checkers.BaseChecker, node: astroid.node_classes.NodeNG
    ) -> None:
        # XXX Ideally multicaller wouldn't be necessary, each checker could separately
        # register its own message types.

        for checker in checkers:

            for message in checker.function(self, node):
                self.add_message(
                    message.problem.name, node=node, args=FormattableDict(message.data)
                )

    return _call_each


def _make_visitors(group):

    node_type_checkers = {}
    for checker in group.checkers:
        node_type_checkers.setdefault(checker.node_type, set()).add(checker)

    visitors = {}
    for node_type, checkers in node_type_checkers.items():
        # XXX This is a hack. Visiting should use a better dispatch system than just type
        # name.
        visitor_method_name = "visit_" + node_type.__name__.split(".")[0].lower()
        visitors[visitor_method_name] = _make_multicaller(checkers)

    return visitors


@public
def make_pylint_checker(group: CheckerGroup) -> pylint.checkers.BaseChecker:
    data: t.Dict[str, t.Any] = {}
    data["__implements__"] = (pylint.interfaces.IAstroidChecker,)
    data["name"] = group.name

    data["msgs"] = {}
    for problem in group.problems.values():
        data["msgs"][str(problem.id)] = (
            problem.text,
            problem.name,
            problem.explanation,
        )

    data.update(_make_visitors(group))

    return type(group.name, (pylint.checkers.BaseChecker,), data)


@public
def message(
    node: astroid.node_classes.NodeNG, problem: Problem = None, **data
) -> Message:
    return Message(problem, node, data)
