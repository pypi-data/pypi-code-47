import tarfile
import tempfile
import zipfile
from pathlib import Path

from functools import lru_cache
from sphinx.util import logging
from sphinx.util.console import bold
from slugify import slugify

from .download_pkgs import download

logger = logging.getLogger(__file__)


@lru_cache()
def get_package_metadata(name: str) -> dict:
    with tempfile.TemporaryDirectory() as tempdir:
        logger.info(bold("downloading package: ") + name)
        archive_name = download(name, tempdir)
        if archive_name is None:
            return {}
        if archive_name.suffix == ".whl":
            metadata = _read_meta_from_wheel(archive_name)
        if archive_name.suffix == ".gz":
            metadata = _read_meta_from_tar(archive_name)

    return _parse_metadata(metadata)


def _read_meta_from_wheel(archive_name: Path) -> str:
    if not archive_name.suffix == ".whl":
        raise TypeError("Wrong file type.")
    with zipfile.ZipFile(archive_name) as zfo:
        path = next(
            zippath
            for zippath in zfo.namelist()
            if zippath.endswith("METADATA")
        )
        metadata = zfo.read(path).decode()
        return metadata


def _read_meta_from_tar(archive_name: Path) -> str:
    if not archive_name.suffix == ".gz":
        raise TypeError("Wrong file type.")
    with tarfile.open(archive_name) as tfo:
        path = next(
            tarpath
            for tarpath in tfo.getnames()
            if tarpath.endswith("PKG-INFO")
        )
        with tfo.extractfile(path) as meta_file:
            return meta_file.read().decode("utf-8")


def _parse_metadata(metadata: str) -> dict:
    parsed_metadata = {}
    lines = [line.strip() for line in metadata.split("\n")]

    while lines:
        line = lines.pop(0)

        if ": " in line:
            key, val = line.split(": ", maxsplit=1)

            while lines and ": " not in lines[0] and len(lines[0]) > 0:
                val += lines.pop(0)
            else:
                parsed_metadata[key.lower()] = val

        if len(lines[0]) == 0:
            break

    if lines:
        parsed_metadata["long_description"] = "\n".join(lines)

    return parsed_metadata
