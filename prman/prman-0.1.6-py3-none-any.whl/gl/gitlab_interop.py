# pylint: disable=unused-wildcard-import
import gitlab
from toolz.curried import *


def init_gitlab_client(gitlab_url, token):
  client = gitlab.Gitlab(gitlab_url, private_token=token)
  client.auth()
  return client


def get_current_user(client):
  return client.user


def get_project(client, project_id):
  return client.projects.get(project_id)


def get_project_users_except_me_and_ci(client, project):
  user_id = client.user.id
  return pipe(
    project.users.list(),
    map(lambda x: x.id),
    filter(lambda x: x != user_id and x != 3696277),
    map(lambda x: client.users.get(x)),
    list
  )


def get_opened_prs_for_branch(project, source_branch):
  return pipe(
    project.mergerequests.list(state='opened', source_branch=source_branch),
    map(lambda x: x.iid),
    map(project.mergerequests.get),
    list
  )


def create_pr(approvers_required_count_config, client, project, source_branch, target_branch, title, message, approver_ids):
  user = get_current_user(client)
  pr_create_req = {
    'source_branch': source_branch,
    'target_branch': target_branch,
    'title': title,
    'remove_source_branch': True,
    'squash': True,
    'assignee_ids': [user.id] + approver_ids,
  }
  if not message is None:
    pr_create_req['description'] = message
  if approvers_required_count_config['set']:
    required_count = len(approver_ids)
    max_required_count = approvers_required_count_config['max']
    if max_required_count != -1:
      required_count = min(required_count, max_required_count)
    pr_create_req['approvals_before_merge'] = required_count
  pr = project.mergerequests.create(pr_create_req)

  pr.approvals.set_approvers() # set_approvers does not work without it
  pr.approvals.set_approvers(approver_ids)
  return pr
