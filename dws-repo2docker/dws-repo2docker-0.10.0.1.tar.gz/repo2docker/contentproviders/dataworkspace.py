import subprocess
import sys
import os
from os.path import join, isdir

from .base import ContentProvider, ContentProviderException
from ..utils import execute_cmd, check_ref


class Dataworkspace(ContentProvider):
    """Provide contents of a dataworkspaces workspace."""

    def detect(self, source, ref=None, extra_args=None):
        # for now we look for a .dataworkspaces directory, which
        # corresponds to a git-backed workspace.
        if source.startswith('dws+'):
            if ref is not None:
                raise ContentProviderException("Dataworkspace content provider does not currently support --ref")
            return {"repo": source[len('dws+'):], "ref": ref}

    def fetch(self, spec, output_dir, yield_output=False):
        repo = spec["repo"]
        ref = spec.get("ref", None)

        try:
            os.rmdir(output_dir) # clone is expecting directory to not exist
            cmd = ["dws", "--batch", "clone", "--hostname=docker"]
            cmd.extend([repo, output_dir])
            for line in execute_cmd(cmd, capture=yield_output):
                yield line

        except subprocess.CalledProcessError as e:
            msg = "Failed to clone workspace from {repo}.".format(repo=repo)
            raise ContentProviderException(msg) from e


        cmd = ["git", "rev-parse", "HEAD"]
        sha1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=output_dir)
        self._sha1 = sha1.stdout.read().decode().strip()

    @property
    def content_id(self):
        """A unique ID to represent the version of the content.
        Uses the first seven characters of the git commit ID of the repository.
        """
        return self._sha1[:7]
