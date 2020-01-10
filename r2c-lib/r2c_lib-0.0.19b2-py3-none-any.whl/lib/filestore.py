import abc
import hashlib
import json
import os
import shutil
from pathlib import Path
from typing import List, Optional

from r2c.lib.constants import DEFAULT_LOCAL_RUN_DIR_SUFFIX
from r2c.lib.jobdef import CacheKey
from r2c.lib.util import get_tmp_dir


class FileStore(metaclass=abc.ABCMeta):
    """
        Abstract base class for something that stores and retrieves files
    """

    @abc.abstractmethod
    def put(self, cache_key: CacheKey, source: str) -> None:  # Path,
        """
            Stores the file/directory in SOURCE so that it is retreivable given
            GIT_URL, COMMIT_HASH, and SPECIFIED_ANALYZER
        """

    @abc.abstractmethod
    def write(self, cache_key: CacheKey, obj_str: str) -> None:
        """
            Would be equivalent if obj_str was written to a file and self.put was
            called on that file
        """

    @abc.abstractmethod
    def get(self, cache_key: CacheKey, destination: str) -> bool:  # Path,
        """
            Retieved file/directory previously stored and writes it to DESITINATION

            Returns True if file was retrieved, False if file did not exist
        """

    @abc.abstractmethod
    def read(self, cache_key: CacheKey) -> Optional[str]:
        """
            Reads the file stored as a string. Returns None if file does not exist
        """

    @abc.abstractmethod
    def contains(self, cache_key: CacheKey) -> bool:
        """
            Returns true if file/directory exists in filestore
        """

    @classmethod
    @abc.abstractmethod
    def _key_delimiter(cls):
        pass

    @classmethod
    @abc.abstractmethod
    def _key_suffix(cls):
        pass

    @classmethod
    def _key(cls, cache_key: CacheKey) -> str:
        """
            Key used to identify the file stored
        """
        specified_analyzer = cache_key.analyzer
        analyzer_input = cache_key.input
        analyzer_name = specified_analyzer.versioned_analyzer.name
        version = specified_analyzer.versioned_analyzer.version

        parts: List[str] = [analyzer_name, str(version), analyzer_input.digest()]
        if specified_analyzer.parameters:
            hasher = hashlib.sha256()
            # Hash the parameters to avoid running into length limits.
            for param_name in sorted(specified_analyzer.parameters):
                hasher.update(
                    f"{param_name}:{specified_analyzer.parameters[param_name]}".encode()
                )
            parts.append(hasher.hexdigest()[:20])

        parts.append(cls._key_suffix())

        return cls._key_delimiter().join(part.replace("/", "--") for part in parts)


def get_default_local_filestore_dir():
    return os.path.join(get_tmp_dir(), DEFAULT_LOCAL_RUN_DIR_SUFFIX)


class LocalFileStore(FileStore):
    def __init__(self, path: str) -> None:
        self._directory = os.path.join(get_default_local_filestore_dir(), path)
        Path(os.path.join(self._directory, "metadata")).mkdir(
            parents=True, exist_ok=True
        )
        Path(os.path.join(self._directory, "data")).mkdir(parents=True, exist_ok=True)

    def delete(self, cache_key: CacheKey) -> None:
        key = self._key(cache_key)
        if os.path.isfile(os.path.join(self._directory, "data", key)):
            os.remove(os.path.join(self._directory, "data", key))
        if os.path.isfile(os.path.join(self._directory, "metadata", key)):
            os.remove(os.path.join(self._directory, "metadata", key))

    def delete_all(self) -> None:
        shutil.rmtree(self._directory)
        Path(os.path.join(self._directory, "metadata")).mkdir(
            parents=True, exist_ok=True
        )
        Path(os.path.join(self._directory, "data")).mkdir(parents=True, exist_ok=True)

    def put(self, cache_key: CacheKey, source: str) -> None:  # Path,
        key = self._key(cache_key)

        # For now metadata is unused
        metadata_path = os.path.join(self._directory, "metadata", key)
        with open(metadata_path, "w") as f:
            f.write(json.dumps({}))

        target_path = os.path.join(self._directory, "data", key)
        shutil.copy(source, target_path)

    def write(self, cache_key: CacheKey, obj_str: str) -> None:
        key = self._key(cache_key)

        # always create empty metadata object so metadata dir reflects data dir 1:1
        with open(os.path.join(self._directory, "metadata", key), "w") as f:
            pass

        with open(os.path.join(self._directory, "data", key), "w") as f:
            f.write(obj_str)

    def get(self, cache_key: CacheKey, destination: str) -> bool:  # Path,
        key = self._key(cache_key)
        try:
            shutil.copy(os.path.join(self._directory, "data", key), destination)
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            raise e

    def read(self, cache_key: CacheKey) -> Optional[str]:
        bytestream = self.read_bytes(cache_key)
        if bytestream is not None:
            return bytestream.decode("utf-8")
        else:
            return None

    def read_bytes(self, cache_key: CacheKey) -> Optional[bytes]:
        key = self._key(cache_key)
        try:
            with open(os.path.join(self._directory, "data", key), "rb") as f:
                return f.read()
        except FileNotFoundError:
            return None

    def contains(self, cache_key: CacheKey) -> bool:
        key = self._key(cache_key)
        return Path(os.path.join(self._directory, "data", key)).exists()

    @classmethod
    def _key_delimiter(cls):
        return "___"


class LocalFilesystemOutputStore(LocalFileStore):
    def __init__(self) -> None:
        super().__init__("analysis_output")

    @classmethod
    def _key_suffix(cls):
        return "output.tar.gz"


class LocalJsonOutputStore(LocalFileStore):
    def __init__(self) -> None:
        super().__init__("analysis_output")

    @classmethod
    def _key_suffix(cls):
        return "output.json"


class LocalLogStore(LocalFileStore):
    def __init__(self) -> None:
        super().__init__("analysis_log")

    @classmethod
    def _key_suffix(cls):
        return "container.log"


class LocalStatsStore(LocalFileStore):
    def __init__(self) -> None:
        super().__init__("analysis_log")

    @classmethod
    def _key_suffix(cls):
        return "container_stats.json"
