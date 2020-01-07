import attr

from r2c.lib.analyzer import SpecifiedAnalyzer
from r2c.lib.input import AnalyzerInput


@attr.s(auto_attribs=True, frozen=True)
class CacheKey:
    """Contains the full specification of an analyzer and what its input is.

    This class contains enough information that we can use it as a cache, hence
    the name.
    """

    analyzer: SpecifiedAnalyzer
    input: AnalyzerInput
