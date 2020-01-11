# pylint: disable=unused-wildcard-import
from .cli.argparsing import *
from .config import *
from .cli.interaction import *
from .git.git_interop import *
from .git.git_conventions import *
from .gl.gitlab_interop import *
from .gl.gitlab_conventions import *
from toolz.curried import *
import logging
import os


__version__ = "0.1.6"


def prman():
  args = read_args(__version__)
  if args['config']:
    key = args['<key>']
    value = args.get('<value>', None)
    if value is None:
      config = read_config()
      value = config.get(key, '')
      print(value)
    else:
      add_config_kvp(key, value)
    return

  config = read_config()

  repo_path = os.getcwd()
  repo = get_repo(repo_path)
  if repo is None:
    print_dir_is_not_repo(repo_path)
    return
  repo_name = get_repo_name(repo)
  print_repo_name(repo_name)

  remote_url = get_first_remote_url(repo)
  project_id = extract_gitlab_project_id(remote_url)
  if project_id is None:
    print_repo_gitlab_project_id_can_not_be_extracted(remote_url)
    return
  print_project_id(project_id)

  current_branch = get_current_branch(repo)
  print_current_branch(current_branch)

  if current_branch == 'master':
    print_can_not_create_pr_from_master()
    return

  if not is_git_working_tree_clean(repo):
    print_repo_should_not_have_changes()
    return

  if get_current_branch_commits_till_master_count(repo) == 0:
    print_current_branch_is_not_ahead()
    return

  pr_name = get_pr_name(
    config['conventions.branch_to_pr_mappings'],
    current_branch
  )
  if pr_name is None:
    print_current_branch_can_not_be_mapped_to_pr_name()
    return
  print_pr_name(pr_name)

  print_fetching_project()
  gl_client = init_gitlab_client(config['gitlab.url'], config['gitlab.token'])
  project = get_project(gl_client, project_id)

  print_fetching_prs()
  prs_for_current_branch = get_opened_prs_for_branch(project, current_branch)

  pr_for_current_branch = None if len(prs_for_current_branch) == 0 else prs_for_current_branch[0]
  if not pr_for_current_branch is None:
    print_pr_is_already_created(current_branch, pr_for_current_branch.web_url)
    return

  print_fetching_users()
  users = get_project_users_except_me_and_ci(gl_client, project)
  approvers = select_approvers(users)
  approver_ids = pipe(approvers, map(lambda x: x.id), list)

  print_pushing_to_origin()
  push_origin(repo)

  print_creating_pr()
  approvers_required_count_prefix = 'conventions.approvers.required_count.'
  approvers_required_count_config = {
    'set': config[approvers_required_count_prefix + 'set'] == 'true',
    'max': int(config[approvers_required_count_prefix + 'max'])
  }
  pr_message = args['<message>'] if args.get('-m', False) or args.get('--message', False) else None
  pr = create_pr(
    approvers_required_count_config,
    gl_client,
    project,
    current_branch,
    'master',
    pr_name,
    pr_message,
    approver_ids
  )

  pr_web_url = pr.web_url
  print_pr_is_created(pr_web_url)


def main():
  try:
    prman()
  except KeyboardInterrupt:
    return


if __name__ == '__main__':
  main()
