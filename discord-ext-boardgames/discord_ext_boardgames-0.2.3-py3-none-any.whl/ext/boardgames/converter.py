import re

from typing import Tuple

from discord.ext import commands

__all__ = ('Cell', 'Column', 'Row')


class Column(commands.Converter):
    """Returns the index of a column."""

    @classmethod
    def from_char(cls, argument: str) -> int:
        return ord(argument.upper()) - ord('A')

    @classmethod
    async def convert(cls, ctx: commands.Context, argument: str) -> int:
        if re.match(r'[A-z]', argument):
            return cls.from_char(argument)


class Row(commands.Converter):
    """Returns the index of a row."""

    @classmethod
    def from_char(cls, argument: str) -> int:
        return int(argument) - 1

    @classmethod
    async def convert(cls, ctx: commands.Context, argument: str) -> int:
        if re.match(r'\d+', argument):
            return cls.from_char(argument)


class Cell(commands.Converter):
    """Returns the index of a row and column."""

    @classmethod
    async def convert(self, ctx: commands.Context, argument: str) -> Tuple[int, int]:
        if re.match(r'[A-z]\d+', argument):
            return (Row.from_char(argument[1:]), Column.from_char(argument[0]))

        raise commands.BadArgument('Could not determine cell!')
