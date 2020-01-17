from enum import Enum
from django.template import engines
import yaml, json, os

class STATUS(Enum):
    TODO = 'todo'
    ALPHA = 'alpha'
    BETA = 'beta'
    PROD = 'prod'

class ACTION_TYPE(Enum):
    BULK = 'bulk'
    INSTANCE = 'instance'

def get_instance_action_path(context, collection, id, action):
    return '/api/v3/{}/{}/{}/actions/{}/'.format(
        context,
        collection,
        id,
        action
    )

def get_action_docs(base_path, action_id):
    filepath = '{}/actiondocs/{}.yaml'.format(base_path, action_id)
    with open(filepath) as file:
        parsed_yml = yaml.load(file, Loader=yaml.FullLoader)
        json_string = json.dumps(parsed_yml)
        django_engine = engines['django']
        template = django_engine.from_string(json_string)
        rendered = template.render(context={})
        return json.loads(rendered)

def enrich_actions(base_path, ACTIONS, action_list, environment = {}):
    for action, action_type, action_status in action_list:
        data = get_action_docs(base_path, action)
        data.update(environment)
        data.update({
            "id": action,
            "type": action_type,
            "status": action_status,
        })
        ACTIONS.get('actions').update({
            action: data
        })
    return ACTIONS