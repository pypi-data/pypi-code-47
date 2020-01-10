#!/usr/bin/env python

import hashlib
import logging
import shutil
import tempfile
from pathlib import Path
from typing import List, Optional

import attr

from r2c.lib.filestore import FileStore
from r2c.lib.jobdef import CacheKey
from r2c.lib.manifest import AnalyzerOutputType

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@attr.s(auto_attribs=True)
class OutputStorage:
    """Copies the output of analyzers from the relevant FileStore.

    In addition, it keeps a cache on-disk to prevent repeatedly accessing the
    network.

    The cache is persistent between instances of OutputStorage.
    """

    _json_output_store: FileStore
    _filesystem_output_store: FileStore
    _cache_dir: Path

    def reset_cache(self) -> None:
        """Deletes all entries in the cache."""
        for child in self._cache_dir.iterdir():
            if child.is_file() or child.is_symlink():
                child.unlink()
            else:
                shutil.rmtree(child)

    def contains(self, cache_key: CacheKey, output_type: AnalyzerOutputType) -> bool:
        """Returns whether there's output for the given analyzer/input.

        This does *not* depend on whether the output is in the cache or not.

        If output_type is `both`, this is only true if it has both JSON and
        filesystem output.

        """
        if output_type.has_json():
            if not self._json_output_store.contains(cache_key):
                return False

        if output_type.has_filesystem():
            if not self._filesystem_output_store.contains(cache_key):
                return False

        return True

    def upload(
        self, cache_key: CacheKey, output_type: AnalyzerOutputType, base_dir: Path
    ) -> Path:
        """Uploads the output of the given analyzer from the given path.

        This also adds it to the OutputStorage's cache; the return value is the
        path inside the cache.

        base_dir should be the *directory* that contains the output.json and/or
        fs folder.

        Note that unlike fetch(), this *does* work with AnalyzerOutputType.both
        analyzers.
        """
        if not base_dir.is_dir():
            raise ValueError(f"Argument {base_dir} to upload should be a directory")

        if output_type.has_json():
            output_path = base_dir / "output.json"
            logger.info(f"Uploading {output_path}")
            self._json_output_store.put(cache_key, str(base_dir / "output.json"))

            # Store it in our cache.
            cached_path = self._cache_path(cache_key, AnalyzerOutputType.json)
            shutil.copyfile(output_path, cached_path)

        if output_type.has_filesystem():
            output_path = base_dir / "fs"
            logger.info(f"Uploading {output_path}")
            # We create a tempdir because we want to make sure the tarchive
            # gets automatically deleted, and creating the tempfile using
            # TemporaryFile will result in it trying to unlink the wrong file.
            with tempfile.TemporaryDirectory(prefix="output-archive-") as d:
                tarfile_path = shutil.make_archive(
                    base_name=d + "/output", format="gztar", root_dir=output_path
                )
                logger.info(f"Uploading {tarfile_path}")
                self._filesystem_output_store.put(cache_key, tarfile_path)

            # Store it in our cache.
            cached_path = self._cache_path(cache_key, AnalyzerOutputType.filesystem)
            shutil.copytree(output_path, cached_path)

        return output_path

    def fetch_analyzer_output(
        self, cache_key: CacheKey, output_type: AnalyzerOutputType
    ) -> Optional[Path]:
        """Gets the path to the output of an analyzer.

        If output_type is fs, this will fetch *and* extract the archive, and
        return the path *inside* the archive to the files (i.e., not the
        archive root, but the subdirectory inside the archive containing
        everything). Otherwise, it will just fetch it. Do not delete or modify
        the files returned from this function!

        This uses a cache to prevent repeatedly hitting the network; however,
        it will *not* cache failed lookups.

        Since this only returns a single path, if an analyzer has 'both' output
        type, you'll need to call this once with 'fs' and once with 'json'.

        Returns the path to the output on disk, or None if it couldn't be
        fetched.

        """
        if output_type == AnalyzerOutputType.both:
            # We can only return a single path; which path would we return if
            # the user asked for both?
            raise ValueError(
                "Internal error: cannot fetch both json and fs output from fetch_analyzer_output"
            )

        cached_path = self._cache_path(cache_key, output_type)
        if cached_path.exists():
            return cached_path

        success = self._fetch_analyzer_output_impl(cache_key, output_type, cached_path)
        if success:
            if not cached_path.exists():
                raise Exception(
                    f"Internal error; {cached_path} does not exist even after a successful fetch?"
                )
            return cached_path
        else:
            logger.info(
                f"Could not fetch output of type {output_type} for {cache_key.analyzer} when run on {cache_key.input}"
            )
            return None

    def _fetch_analyzer_output_impl(
        self, cache_key: CacheKey, output_type: AnalyzerOutputType, cached_path: Path
    ) -> bool:
        """Implementation for fetch_analyzer_output."""

        # Pick a human-readable prefix to assist in debugging.
        logger.info(
            f"Fetching output for {cache_key.analyzer} of type {output_type} for {cache_key.input}"
        )
        if output_type == AnalyzerOutputType.json:
            logger.info(f"Using path {cached_path}")
            return self._json_output_store.get(cache_key, str(cached_path))

        elif output_type == AnalyzerOutputType.filesystem:
            with tempfile.NamedTemporaryFile(suffix=".tar.gz") as temp_tgz:
                # Store the archive in a tempfile, then unzip it.
                if not self._filesystem_output_store.get(cache_key, temp_tgz.name):
                    return False
                logger.info(f"Using dir {cached_path}")
                shutil.unpack_archive(temp_tgz.name, cached_path)
                return True

        else:
            raise RuntimeError(f"Cannot fetch for type {output_type}")

    @classmethod
    def _cache_key(cls, cache_key: CacheKey) -> str:
        key_delimiter = "__"
        analyzer = cache_key.analyzer
        analyzer_name = analyzer.versioned_analyzer.name
        version = analyzer.versioned_analyzer.version

        parts: List[str] = [analyzer_name, str(version), cache_key.input.digest()]
        if analyzer.parameters:
            hasher = hashlib.sha256()
            # Hash the parameters to avoid running into length limits.
            for param_name in sorted(analyzer.parameters):
                hasher.update(
                    f"{param_name}:{analyzer.parameters[param_name]}".encode()
                )
            parts.append(hasher.hexdigest()[:20])

        return key_delimiter.join(parts).replace("/", "--")

    def _cache_path(self, cache_key: CacheKey, output_type: AnalyzerOutputType) -> Path:
        cache_path = self._cache_dir / self._cache_key(cache_key)
        if output_type == AnalyzerOutputType.json:
            return cache_path.with_suffix(cache_path.suffix + ".json")
        else:
            return cache_path
