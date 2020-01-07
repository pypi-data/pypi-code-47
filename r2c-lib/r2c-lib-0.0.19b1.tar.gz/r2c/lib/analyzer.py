import json
from typing import Any, ClassVar, Dict, NewType, Optional, Set

import attr
import cattr
from mypy_extensions import TypedDict
from semantic_version import Version

from r2c.lib.constants import ECR_URL

AnalyzerName = NewType("AnalyzerName", str)

VersionedAnalyzerJson = TypedDict(
    "VersionedAnalyzerJson", {"name": str, "version": str}
)

# TODO(deifactor): Can we just autogenerate JSON methods for
# serialization/deserialization via cattr? I think the only place that needs
# them is the frontend app.


@attr.s(auto_attribs=True, frozen=True)
class VersionedAnalyzer:
    """
        Class to represent an analyzer and resolved version
    """

    name: AnalyzerName
    version: Version

    FETCHER_ANALYZERS: ClassVar[Set[str]] = {
        "public/source-code",
        "public/git-repo",
        "public/pypi",
        "public/npm",
    }

    def is_fetcher(self) -> bool:
        return self.name in VersionedAnalyzer.FETCHER_ANALYZERS

    @property
    def image_id(self) -> str:
        """
            ECR Tag of a Versioned Analyzer
        """
        return f"{ECR_URL}/massive-{str(self.name)}:{str(self.version)}"

    def to_json(self) -> VersionedAnalyzerJson:
        return {"name": str(self.name), "version": str(self.version)}

    @classmethod
    def from_json_str(cls, json_str: str) -> "VersionedAnalyzer":
        obj = json.loads(json_str)
        return cls.from_json(obj)

    @classmethod
    def from_json(cls, json_obj: VersionedAnalyzerJson) -> "VersionedAnalyzer":
        if "name" not in json_obj or "version" not in json_obj:
            raise Exception(
                f"Can't parse {json_obj} as a versioned analyzer. Need 'name' and 'version' keys."
            )
        return cls(AnalyzerName(json_obj["name"]), Version(json_obj["version"]))

    def __repr__(self):
        return self.name + ":" + str(self.version)


def build_fully_qualified_name(org: str, analyzer_name: str) -> AnalyzerName:
    return AnalyzerName("/".join([org, analyzer_name]))


class SpecifiedAnalyzerJson(TypedDict):
    versionedAnalyzer: VersionedAnalyzerJson
    parameters: Dict[str, Any]


def _initialize_parameters(params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return params or {}


# We have to say `hash=False` so attrs won't 'helpfully' delete our hashing
# implementation.
@attr.s(auto_attribs=True, hash=False)
class SpecifiedAnalyzer:
    """
        Class to represent a specific instance of an analyzer. This includes
        any parameters.

        Contains all necessary information to run an analyzer minus the target of analysis
    """

    name: AnalyzerName
    version: Version
    # We need to use frozen sets because otherwise we can't really hash this,
    # since dicts are unhashable.
    parameters: Dict[str, Any] = attr.ib(converter=_initialize_parameters, factory=dict)

    def is_fetcher(self) -> bool:
        return self.versioned_analyzer.is_fetcher()

    @property
    def versioned_analyzer(self) -> VersionedAnalyzer:
        return VersionedAnalyzer(self.name, self.version)

    @classmethod
    def from_json_str(cls, json_str: str) -> "SpecifiedAnalyzer":
        obj = json.loads(json_str)
        return cls.from_json(obj)

    @classmethod
    def from_json(cls, json_obj: Dict[str, Any]) -> "SpecifiedAnalyzer":
        if "parameters" in json_obj:
            parameters = json_obj["parameters"]
        else:
            parameters = {}
        va = VersionedAnalyzer.from_json(json_obj["versionedAnalyzer"])
        return cls(va.name, va.version, parameters)

    def to_json(self) -> SpecifiedAnalyzerJson:
        return {
            "versionedAnalyzer": self.versioned_analyzer.to_json(),
            "parameters": self.parameters,
        }

    def __hash__(self) -> int:
        return hash(
            (
                "an arbitrary salt",
                self.versioned_analyzer,
                json.dumps(self.parameters, sort_keys=True),
            )
        )


cattr.register_unstructure_hook(Version, str)
cattr.register_structure_hook(Version, lambda version, cl: cl(version))

cattr.register_unstructure_hook(AnalyzerName, str)
cattr.register_structure_hook(AnalyzerName, lambda name, cl: cl(name))
