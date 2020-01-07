#!/usr/bin/env python

import logging
import shutil
from pathlib import Path
from typing import Optional

import attr

from r2c.lib.analysis.mount_manager import MountManager
from r2c.lib.analysis.output_storage import OutputStorage
from r2c.lib.analyzer import SpecifiedAnalyzer
from r2c.lib.input import AnalyzerInput
from r2c.lib.jobdef import CacheKey
from r2c.lib.manifest import AnalyzerOutputType
from r2c.lib.registry import RegistryData

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@attr.s(auto_attribs=True)
class DependencyMounter:
    """Mounts the dependencies of an analyzer.

    This class is responsible for figuring out where inside a MountManager's
    input directory each dependency should go and then fetching those
    dependencies from storage.
    """

    _registry_data: RegistryData
    output_storage: OutputStorage
    # Path to where the fetched code lives on disk. This doesn't need to be set
    # at construction time, but it *must* be set before any non-fetcher
    # analyzers are run.
    fetched_code: Optional[Path] = None

    def mount_all(
        self,
        analyzer: SpecifiedAnalyzer,
        input: AnalyzerInput,
        mount_manager: MountManager,
    ) -> None:
        """Mounts all dependencies.

        As a special case, if the input is an instance of LocalCode, then the
        LocalCode's code_dir will be used as the output for all of the
        'fetcher' analyzers (i.e., those where is_fetcher() returns true).

        Raises an exception if a dependency failed to mount.
        """
        logger.info(f"Mounting dependencies for {analyzer} on {input}")

        for dependency in self._registry_data.get_direct_dependencies(
            analyzer.versioned_analyzer
        ):
            if not self._mount(dependency, input, mount_manager):
                raise Exception(f"Error while mounting output of {dependency}")

    def _mount(
        self,
        dependency: SpecifiedAnalyzer,
        input: AnalyzerInput,
        mount_manager: MountManager,
    ) -> bool:
        """Mounts a single dependency."""
        cache_key = CacheKey(analyzer=dependency, input=input)
        logger.info(f"Mounting output of {dependency}")
        output_type = self._registry_data.manifest_for(
            dependency.versioned_analyzer
        ).output_type
        input_dir = mount_manager.input_dir()

        if output_type.has_json():
            target = input_dir / f"{dependency.versioned_analyzer.name}.json"
            fetched = self.output_storage.fetch_analyzer_output(
                cache_key, AnalyzerOutputType.json
            )
            if fetched is not None:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(fetched, target)
            else:
                return False

        if output_type.has_filesystem():
            # Instead of looking at the output of fetcher analyzers, we just
            # use `fetched_code` instead. This is transitional while we move
            # away from depending on fetcher analyzers and towards always
            # mounting the input directly at a fixed location, since specifying
            # the fetcher analyzer is inflexible.
            if dependency.is_fetcher():
                if self.fetched_code is None:
                    raise ValueError(
                        "fetched_code must be set before running anything that depends on a fetcher!"
                    )
                logger.info(f"Overriding fetcher with {self.fetched_code}")
                fetched = self.fetched_code
            else:
                fetched = self.output_storage.fetch_analyzer_output(
                    cache_key, AnalyzerOutputType.filesystem
                )
            if fetched is not None:
                shutil.copytree(fetched, input_dir / dependency.name)
            else:
                return False

        return True

    def contains(self, cache_key: CacheKey) -> bool:
        """Returns if we already have output for the given analyzer/input. """
        output_type = self._registry_data.manifest_for(
            cache_key.analyzer.versioned_analyzer
        ).output_type

        return self.output_storage.contains(cache_key, output_type)
