from typing import List, Union, Tuple, Callable, Any
from .expression_parser import ExpressionParser
from .sql_parser import SqlParser
from .types import TermTuple


def expression(domain: List[Union[str, TermTuple]]) -> Callable:
    parser = ExpressionParser()
    return parser.parse(domain)


def sql(domain: List[Union[str, TermTuple]],
        placeholder='numeric') -> Tuple:
    parser = SqlParser(placeholder=placeholder)
    return parser.parse(domain)
