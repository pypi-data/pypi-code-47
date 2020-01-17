import setuptools
import subprocess

## Taken from numpy:
# https://github.com/numpy/numpy/blob/master/setup.py
MAJOR   = 0
MINOR   = 3
MICRO   = 0

def run_gitcmd(git_cmd):
  output = subprocess.run(git_cmd, text=True, capture_output=True)
  if output.returncode == 0:
    return output.stdout.strip()
  return None

def git_revision():
  """Get git revision as short SHA1 string"""
  revision = run_gitcmd(['git', 'rev-parse', '--short', 'HEAD'])
  if not revision:
    return 'UNK'
  return revision

def git_branch(release_branch):
  """
  Get git branch from where setup.py was run. Use to set release part. If
  :param str release_branch: stable branch name, i.e. not a release branch
  """
  branch = run_gitcmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
  if not branch:
    return 'UNK'
  if branch == release_branch:
    return None
  return 'dev'

def git_commits_since_last_tag():
  """Count commits since last tag on actual branch"""
  last_tag = run_gitcmd(['git', 'rev-list', '--abbrev-commit', '--tags', '--no-walk', '--max-count=1'])
  if not last_tag:
    return -1
  return int(run_gitcmd(['git', 'rev-list', last_tag+'..HEAD', '--count']))

def assemble_version():
  """Assemble version string"""

  release_branch = 'master'
  version = "{0:d}.{1:d}.{2:d}".format(MAJOR, MINOR, MICRO)
  commits = git_commits_since_last_tag()
  branch = git_branch(release_branch)
  if branch:
    if commits >= 0:
      version = '.'.join([version, branch+str(commits)])
    else:
      version = '.'.join([version, branch])
  #revision = git_revision()
  #if revision:
    #version = '+'.join([version, revision])


  return version

setuptools.setup( version=assemble_version() )
