"""
Main interface for translate service type definitions.

Usage::

    from mypy_boto3.translate.type_defs import EncryptionKeyTypeDef

    data: EncryptionKeyTypeDef = {...}
"""
from __future__ import annotations

from datetime import datetime
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EncryptionKeyTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyPropertiesTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyResponseTypeDef",
    "ListTerminologiesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TerminologyDataTypeDef",
    "TermTypeDef",
    "AppliedTerminologyTypeDef",
    "TranslateTextResponseTypeDef",
)

EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"Type": Literal["KMS"], "Id": str})

TerminologyDataLocationTypeDef = TypedDict(
    "TerminologyDataLocationTypeDef", {"RepositoryType": str, "Location": str}
)

TerminologyPropertiesTypeDef = TypedDict(
    "TerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": EncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

GetTerminologyResponseTypeDef = TypedDict(
    "GetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": TerminologyPropertiesTypeDef,
        "TerminologyDataLocation": TerminologyDataLocationTypeDef,
    },
    total=False,
)

ImportTerminologyResponseTypeDef = TypedDict(
    "ImportTerminologyResponseTypeDef",
    {"TerminologyProperties": TerminologyPropertiesTypeDef},
    total=False,
)

ListTerminologiesResponseTypeDef = TypedDict(
    "ListTerminologiesResponseTypeDef",
    {"TerminologyPropertiesList": List[TerminologyPropertiesTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TerminologyDataTypeDef = TypedDict(
    "TerminologyDataTypeDef", {"File": Union[bytes, IO], "Format": Literal["CSV", "TMX"]}
)

TermTypeDef = TypedDict("TermTypeDef", {"SourceText": str, "TargetText": str}, total=False)

AppliedTerminologyTypeDef = TypedDict(
    "AppliedTerminologyTypeDef", {"Name": str, "Terms": List[TermTypeDef]}, total=False
)

_RequiredTranslateTextResponseTypeDef = TypedDict(
    "_RequiredTranslateTextResponseTypeDef",
    {"TranslatedText": str, "SourceLanguageCode": str, "TargetLanguageCode": str},
)
_OptionalTranslateTextResponseTypeDef = TypedDict(
    "_OptionalTranslateTextResponseTypeDef",
    {"AppliedTerminologies": List[AppliedTerminologyTypeDef]},
    total=False,
)


class TranslateTextResponseTypeDef(
    _RequiredTranslateTextResponseTypeDef, _OptionalTranslateTextResponseTypeDef
):
    pass
