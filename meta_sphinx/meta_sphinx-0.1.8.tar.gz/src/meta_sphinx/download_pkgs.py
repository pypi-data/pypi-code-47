import os
import re
import subprocess
import sys
from pathlib import Path

import urllib3

pip_download_command = [sys.executable, "-m", "pip", "download"]


def download(name: str, dir_: Path = Path("."), timeout: int = 5) -> Path:
    pip_download_options = ["--dest", str(dir_), "--no-deps"]
    # add extra indices if available:
    if "PIP_EXTRA_INDEX_URL" in os.environ:
        pip_download_options += [
            "--extra-index-url",
            os.getenv("PIP_EXTRA_INDEX_URL"),
            "--trusted-host",
            urllib3.util.parse_url(os.getenv("PIP_EXTRA_INDEX_URL")).host,
        ]

    # set a timeout:
    pip_download_options += ["--timeout", str(timeout)]

    process = subprocess.Popen(
        pip_download_command + pip_download_options + [name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, stderr = process.communicate()  # wait to finish & read output
    filename = _get_filename_from_download_output(stdout, name)

    return filename


def _get_filename_from_download_output(output: str, name: str) -> Path:
    match = re.search(
        r"(?:Saved )(\/[\w/]*"
        + name.replace("-", "_")
        + r".+\.(whl|tar\.gz))",
        output,
    )
    if match:
        return Path(match.group(1))
    else:
        return None
