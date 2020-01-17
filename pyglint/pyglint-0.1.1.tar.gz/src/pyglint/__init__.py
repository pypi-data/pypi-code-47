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
    """A problem found by a checker.

    Args:

        name: The name of the problem. Usually 2-4 words, hyphenated.

        text: The message text for display to the user. :func:`str.format` syntax is
        supported. Usually one short sentence.

        explanation: Prose description of the problem. Usually a few sentences.

    """

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
    """The main object for defining linters with Pyglint."""

    name: str
    checkers: t.List[Checker] = attr.ib(factory=list)
    problems: t.Dict[str, Problem] = attr.ib(factory=dict)

    id_prefix: str = "E"

    def problem(self, name: str, text: str, explanation: str):
        """Define a reusable :class:`Problem`."""
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
        """Check for one or more pre-defined :class:`Problem` s.

        Args:

            node_type: The checker will be invoked with each instance of the given node
                type that pylint finds.

            problems: The :class:`Problem`s that this checker might find. Useful for
                allowing users to disable checks for specific problems.

        """

        def wrapper(function):
            checker = make_checker(node_type, problems)(function)
            self.checkers.append(checker)
            return checker.function

        return wrapper

    def standalone_check(
        self, node_type: t.Type[astroid.node_classes.NodeNG], text: str
    ):
        """Check for a :class:`Problem` generated on the fly from this function.

        Args:

            node_type: The checker will be invoked with each instance of the given node
                object type that pylint finds.

            text: The text of the message that will be displayed to the user.
                :func:`str.format` syntax is supported.

        """

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
        # pylint: disable=fixme
        # XXX Ideally multicaller wouldn't be necessary, each checker could separately
        # register its own message types.

        for checker in checkers:
            for msg in checker.function(self, node):
                self.add_message(
                    msg.problem.name, node=node, args=FormattableDict(msg.data)
                )

    return _call_each


def _make_visitors(group):

    node_type_checkers = {}
    for checker in group.checkers:
        node_type_checkers.setdefault(checker.node_type, set()).add(checker)

    visitors = {}
    for node_type, checkers in node_type_checkers.items():
        # pylint: disable=fixme
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
