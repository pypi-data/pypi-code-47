from pathlib import Path
from typing import List

from .errors import NetworkLoadError


def _possible_formats(netname: Path) -> List[str]:
    ext = netname.suffix
    if ext == ".onnx":
        return ["onnx"]
    return ["onnx"]


def _load(path: Path, fmt: str):
    if fmt == "onnx":
        from . import onnx

        return onnx.load(path)
    raise NetworkLoadError(f"Unsupported network format: {fmt}")


def load(path: Path, fmt: str = None):
    if fmt is not None:
        return _load(path, fmt)
    possible_formats = _possible_formats(path)
    for fmt in possible_formats:
        try:
            return _load(path, fmt)
        except NetworkLoadError as e:
            if e.args[0] != "Incorrect network format.":
                raise
    raise NetworkLoadError(f"Unknown format for network: {path}")
