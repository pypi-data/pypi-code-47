"""Core classes for motto
"""
from typing import Any, Callable, ClassVar, Dict, List, Optional, Tuple, Union
from typing_extensions import Protocol, TypedDict


class Message(object):
    """Reporting message class.

    This object is appended for paragraphes by skills.
    Responsibility is only telling event "what" for user, not "where".
    """

    def __init__(self, body: str):
        self.body: str = body
        """message body"""


class Report(object):
    """Report by skills.
    """

    def __init__(self):
        self._messages: List[Message] = []

    def __repr__(self):
        cnt = len(self)
        if cnt == 0:
            return "[No reports]"
        if cnt == 1:
            return "[1 report]"
        return f"[{cnt} reports]"

    def __len__(self) -> int:
        return len(self._messages)

    def add(self, msg: Message):
        self._messages.append(msg)


class Token(Protocol):
    """Token interface for tokenize engine.

    Based from Janome.
    """

    surface: ClassVar[str]


class TokenRepository(object):
    """Token dataset and accessor.
    """

    def __init__(self, tokens: Union[Tuple[Token, ...], List[Token]]):
        self._tokens: Tuple[Token, ...] = tuple(tokens) if isinstance(
            tokens, list
        ) else tokens

    def __repr__(self) -> str:
        cnt = len(self)
        if cnt == 0:
            return "[no tokens]"
        if cnt == 1:
            return "[1 token]"
        return f"[{cnt} tokens]"

    def __len__(self) -> int:
        return len(self._tokens)

    def __getitem__(self, key) -> Token:
        return self._tokens[key]


SkillParams = Dict[str, Any]

SkillProc = Callable[[TokenRepository, SkillParams], Optional[Message]]

Config = Dict[str, Any]
