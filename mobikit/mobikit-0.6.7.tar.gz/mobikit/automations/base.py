#
# Copyright (c) 2019 Mobikit, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
import requests
from requests.exceptions import HTTPError, RequestException

from mobikit.config import config
from mobikit.utils import token_required


@token_required
def fetch(workspace_id, automation_id):
    """
  Fetch an automation from a workspace.

  Parameters
  ----------
  workspace_id : str, int
      String or integer containing the workspace id
  automation_id : str, int
      String or integer containing the automation id

  Returns
  -------
  dict
  """
    headers = {"Authorization": "Token {}".format(config.api_token)}
    try:
        res = requests.get(
            f"{config.automations_route}workspace/{int(workspace_id)}/{int(automation_id)}/",
            headers=headers,
        )
        res.raise_for_status()
    except (HTTPError, RequestException) as exc:
        config.logger.exception(exc)
    return res.json()


@token_required
def create(workspace_id, title, feed, triggers, actions):
    """
  Create an automation in a workspace.

  Parameters
  ----------
  workspace_id : str, int
      String or integer containing the workspace id
  title : str
      Title of the workspace
  feed : str, int
      id of the feed to create the automation on
  triggers : [dict]
      an array of trigger dictionaries
  actions : [dict]
      an array of action dictionaries

  Returns
  -------
  int
  """
    headers = {"Authorization": "Token {}".format(config.api_token)}
    payload = {
        "title": title,
        "feed": int(feed),
        "triggers": triggers,
        "actions": actions,
    }
    try:
        res = requests.post(
            f"{config.automations_route}workspace/{int(workspace_id)}/",
            headers=headers,
            json=payload,
        )
        res.raise_for_status()
    except (HTTPError, RequestException) as exc:
        config.logger.exception(exc)
    return res.json()["id"]


@token_required
def delete(workspace_id, automation_id):
    """
  Delete an automation from a workspace.

  Parameters
  ----------
  workspace_id : str, int
      String or integer containing the workspace id
  automation_id : str, int
      String or integer containing the automation id

  Returns
  -------
  None
  """
    headers = {"Authorization": "Token {}".format(config.api_token)}
    try:
        res = requests.delete(
            f"{config.automations_route}workspace/{int(workspace_id)}/{int(automation_id)}/",
            headers=headers,
        )
        res.raise_for_status()
    except (HTTPError, RequestException) as exc:
        config.logger.exception(exc)
