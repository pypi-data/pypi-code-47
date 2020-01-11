# pylint: disable=unused-wildcard-import
from toolz.curried import *
from .git_interop import *
import re


def extract_gitlab_project_id(remote):
  match = re.search(r'git@gitlab.com:(?P<project_id>.+?)\.git', remote)
  return None if match is None else match.group('project_id')
