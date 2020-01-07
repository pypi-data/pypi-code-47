from typing import Any, Dict, List, Optional, Tuple, Union

import attr

from r2c.lib.analyzer import AnalyzerName, SpecifiedAnalyzer
from r2c.lib.input import (
    AnalyzerInput,
    GitRepo,
    GitRepoCommit,
    LocalCode,
    PackageRepository,
    PackageVersion,
)
from r2c.lib.registry import RegistryData


@attr.s(auto_attribs=True)
class ExecutionEntry:
    """Indicates which analyzer should be executed."""

    analyzer: SpecifiedAnalyzer
    # If true, this should be run in 'interactive' mode.
    interactive: bool = False


@attr.s(auto_attribs=True)
class ExecutionOrder:
    fetch_phase: List[ExecutionEntry]
    analysis_phase: List[ExecutionEntry]
    # This analyzer is the one that the AnalysisRunner should assume has the
    # actual code to analyze as its output. If the input is LocalCode, this
    # will be set to None since we just get the output directly off disk.
    code_fetcher: Optional[SpecifiedAnalyzer]

    def all_phases(self) -> List[ExecutionEntry]:
        return self.fetch_phase + self.analysis_phase

    @classmethod
    def compute(
        cls,
        registry_data: RegistryData,
        analyzer: SpecifiedAnalyzer,
        analyzer_input: AnalyzerInput,
        interactive: Optional[Union[str, int]] = None,
    ) -> "ExecutionOrder":
        """Resolves which analyzers should be executed, and in which order.

        `interactive` specifies whether to run an analyzer interactively. If it's a
        string, analyzers whose name contains that string are interactive. If an
        int, then it's used as an offset into the list of execution entries.
        (Negative numbers are OK.)

        Raises an Exception if interactive is not None, but no analyzers matched
        it.
        """
        code_fetcher = cls._fetcher_for(registry_data, analyzer_input)
        fetcher_deps = registry_data.sorted_deps(code_fetcher) if code_fetcher else []
        # We never run fetcher analyzers in the analysis phase, since we can't
        # know which fetcher to use until we know the input type. Eventually,
        # analyzers will stop depending directly on fetchers and we can just
        # drop this filter.
        analyzer_deps = [
            dep for dep in registry_data.sorted_deps(analyzer) if not dep.is_fetcher()
        ]
        all_deps = analyzer_deps + fetcher_deps

        if isinstance(interactive, int) and interactive < 0:
            # Deal with negative offsets.
            interactive += len(all_deps)

        def is_interactive(index: int, dep: SpecifiedAnalyzer) -> bool:
            if isinstance(interactive, str):
                return interactive in dep.versioned_analyzer.name
            elif isinstance(interactive, int):
                return interactive == index
            else:
                return False

        fetch_phase = [
            ExecutionEntry(dep, interactive=is_interactive(index, dep))
            for index, dep in enumerate(fetcher_deps)
        ]
        analysis_phase = [
            ExecutionEntry(
                dep, interactive=is_interactive(index + len(fetch_phase), dep)
            )
            for index, dep in enumerate(analyzer_deps)
        ]

        if interactive is not None and not any(
            entry.interactive for entry in fetch_phase + analysis_phase
        ):
            raise Exception(
                f"An interactive analyzer was requested via specifier `{interactive}`, but no matching analyzer was run!"
            )
        return cls(
            fetch_phase=fetch_phase,
            analysis_phase=analysis_phase,
            code_fetcher=code_fetcher,
        )

    @classmethod
    def _fetcher_for(
        cls, registry_data: RegistryData, analyzer_input: AnalyzerInput
    ) -> Optional[SpecifiedAnalyzer]:
        """Determines which analyzer to use to fetch the given input.

        Each input type has some analyzer name (and optionally parameters) to
        use. We always use the latest version. This creates slight cacheing
        issues, but if we introduce actual changes in fetcher behavior we can
        just purge caches.

        Returns None for LocalCode since that doesn't need a fetcher.
        """
        if isinstance(analyzer_input, LocalCode):
            return None
        name, params = cls._name_and_params_for(analyzer_input)
        latest_version = max(registry_data.analyzer_for(AnalyzerName(name)).versions)
        return SpecifiedAnalyzer(
            name=AnalyzerName(name), version=latest_version, parameters=params
        )

    @classmethod
    def _name_and_params_for(
        cls, analyzer_input: AnalyzerInput
    ) -> Tuple[str, Dict[str, Any]]:
        if isinstance(analyzer_input, GitRepoCommit):
            return ("public/source-code", {})
        elif isinstance(analyzer_input, PackageVersion):
            if analyzer_input.repository == PackageRepository.NPM:
                return ("public/npm", {})
            elif analyzer_input.repository == PackageRepository.PYPI:
                return ("public/pypi", {})
            elif analyzer_input.repository is None:
                raise ValueError(
                    f"Cannot guess fetcher for {analyzer_input}: the repository is not set!"
                )
            else:
                raise ValueError(
                    f"Cannot guess fetcher for {analyzer_input}: unknown repository type"
                )
        elif isinstance(analyzer_input, GitRepo):
            return ("public/source-code", {"keep_history": True})
        else:
            raise ValueError(f"Unhandled input type {analyzer_input}")
