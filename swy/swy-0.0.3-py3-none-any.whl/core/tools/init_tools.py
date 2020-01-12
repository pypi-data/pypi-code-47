from pathlib import Path
import tempfile


def create_tmp_dir() -> Path:
    return Path(tempfile.mkdtemp())

