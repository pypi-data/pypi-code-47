import sqlparse
import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML
from typing import List, Dict

# A SELECT,Identifier,FROM => OK
# B SELECT,identifierList,FROM => OK
# SOMETHING, A or B, SOMETHING => NOK


def is_select(item) -> bool:
    return item.ttype is DML and item.value.upper() == 'SELECT'


def is_identifier(item) -> bool:
    return isinstance(item, sqlparse.sql.Identifier)


def is_identifierList(item) -> bool:
    return isinstance(item, sqlparse.sql.IdentifierList)


def get_tokens(sql: str) -> list:
    parsed = sqlparse.parse(sql.strip())
    return [token for token in list(parsed[0]) if not token.is_whitespace]


def get_alias(field) -> dict:
    try:
        return {'realname': field.get_real_name(), 'alias': field.get_alias()}
    except AttributeError:
        return {'realname': str(field), 'alias': None}


def parse(sql: str) -> List[Dict]:
    """Extract realname & alias of a SELECT

    It cover scenario where SELECT is followed 
    by a unique id or multiple

    Parameters
    ----------
    sql:
        the raw expression (should begin with SELECT)

    Return
    ------
    parsed:
        each element have keys 'realname','alias'
    """
    tokens = get_tokens(sql)
    # SELECT,Identifier
    if is_select(tokens[0]):
        if is_identifier(tokens[1]):
            field = tokens[1]
            return [{'realname': field.get_real_name(), 'alias': field.get_alias()}]
        # SELECT,identifierList
        elif is_identifierList(tokens[1]):
            fields = tokens[1]
            return [get_alias(field) for field in fields.get_identifiers()]
        else:
            return []
    else:
        return []
