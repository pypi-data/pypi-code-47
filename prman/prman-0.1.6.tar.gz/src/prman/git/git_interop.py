# pylint: disable=unused-wildcard-import
import brigit
from toolz.curried import *
import os
from pyrecord import Record


def get_repo(path):
  try:
    repo = brigit.Git(path)
    repo.status()
    return repo
  except brigit.GitException:
    return None


def get_first_remote_url(repo):
  return repo.remote('-v').rstrip().split('\n')[0].replace('\t', ' ').split(' ')[1]


def get_repo_name(repo):
  path = repo.__call__('rev-parse', '--show-toplevel').strip()
  return os.path.basename(path)


def get_current_branch_commits_till_master_count(repo):
  try:
    log = list(repo.pretty_log('origin/master..HEAD'))
  except IndexError: # brigit bug if the log is empty
    log = []
  return len(log)


def get_current_branch(repo):
  return repo.__call__('rev-parse', '--abbrev-ref', 'HEAD').strip()


def is_branch_exists(repo, branch_name):
  try:
    repo.__call__('rev-parse', '--verify', branch_name)
    return True
  except brigit.GitException:
    return False


def is_git_working_tree_clean(repo):
  output = repo.status()
  return 'working tree clean' in output


def push_origin(repo):
  repo.push('-u', 'origin', 'HEAD')
