import abc
import hashlib
import json
from enum import Enum
from inspect import signature
from typing import Any, Dict, List, Optional, Type, Union

import attr
import cattr

INPUT_TYPE_KEY = "input_type"


@attr.s(auto_attribs=True, frozen=True)
class AnalyzerInput(metaclass=abc.ABCMeta):
    @classmethod
    def subclass_from_name(cls, input_type: str) -> Optional[Type["AnalyzerInput"]]:
        for class_obj in cls.__subclasses__():
            if class_obj.__name__ == input_type:
                return class_obj
        return None

    @classmethod
    def _input_keys(cls) -> List[str]:
        """
            Returns a list of string keys that this type of input contains. Uses the subclass's __init__ method to find these keys. This will suffice until we support more flexible json schemas.
            When constructing storage keys, Filestore concatenates the values corresponding to these keys in this order, so this ordering determines storage hierarchy.
        """
        sig = signature(cls.__init__)
        return [param.name for param in sig.parameters.values() if param.name != "self"]

    def to_json(self) -> Dict[str, Any]:
        """
            Returns: the json data representing this analyzer input
        """
        d = {k: v for k, v in self.__dict__.items() if k in self._input_keys()}
        d[INPUT_TYPE_KEY] = self.__class__.__name__
        return d

    def digest(self) -> str:
        """
            One way hash function to use as uuid for an AnalyzerInput

            Uses sha1 hash of sorted json keys
        """
        input_json = self.to_json()
        canonical_string = json.dumps(input_json, sort_keys=True)
        m = hashlib.sha1()
        m.update(canonical_string.encode())
        return m.hexdigest()

    @classmethod
    def from_json(cls, json_obj: Dict[str, Any]) -> "AnalyzerInput":
        if INPUT_TYPE_KEY not in json_obj:
            raise InvalidAnalyzerInputException(
                f"Failed to parse json {json_obj} as an instance of AnalyzerInput."
                f"Couldn't find key {INPUT_TYPE_KEY} to determine input type"
            )
        subclass = cls.subclass_from_name(json_obj[INPUT_TYPE_KEY])
        if subclass is None:
            raise InvalidAnalyzerInputException(
                f"Failed to parse json {json_obj} as an instance of {cls}. "
                f"Input type must be one of {AnalyzerInput.__subclasses__()}"
            )

        # Pass through all fields to the subclass's constructor.
        json_obj = {k: v for k, v in json_obj.items() if k != INPUT_TYPE_KEY}
        try:
            return subclass(**json_obj)  # type: ignore
        except Exception:
            raise InvalidAnalyzerInputException(
                "Failed to parse json {json_obj} as instance of {subclass}"
            )


@attr.s(auto_attribs=True, frozen=True)
class GitRepoCommit(AnalyzerInput):
    repo_url: str
    commit_hash: str


@attr.s(auto_attribs=True, frozen=True)
class GitRepo(AnalyzerInput):
    repo_url: str


class PackageRepository(Enum):
    NPM = "npm"
    PYPI = "pypi"


def _convert_repo(
    repository: Optional[Union[str, PackageRepository]]
) -> Optional[PackageRepository]:
    if repository is None:
        return None
    elif isinstance(repository, str):
        return PackageRepository(repository)
    else:
        return repository


@attr.s(auto_attribs=True, frozen=True)
class PackageVersion(AnalyzerInput):
    package_name: str
    version: str
    repository: Optional[PackageRepository] = attr.ib(
        converter=_convert_repo, default=None
    )

    # Override because of the repository field.
    def to_json(self) -> Dict[str, Any]:
        d = {"package_name": self.package_name, "version": self.version}
        d[INPUT_TYPE_KEY] = self.__class__.__name__
        if self.repository:
            d["repository"] = self.repository.value
        return d


@attr.s(auto_attribs=True, frozen=True)
class HttpUrl(AnalyzerInput):
    url: str


@attr.s(auto_attribs=True, frozen=True)
class AuraInput(AnalyzerInput):
    targets: str
    metadata: str


@attr.s(auto_attribs=True, frozen=True)
class LocalCode(AnalyzerInput):
    """Represents code stored on disk.

    This generally implies that all the 'fetcher' analyzers will have their
    output overridden.
    """

    code_dir: str


class InvalidAnalyzerInputException(Exception):
    pass


class InvalidStorageKeyException(Exception):
    pass


cattr.register_unstructure_hook(AnalyzerInput, lambda inp: inp.to_json())
cattr.register_structure_hook(AnalyzerInput, lambda obj, cl: cl.from_json(obj))
