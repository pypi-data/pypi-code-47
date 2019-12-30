import magpy.general as mg
from magpy.events.base import Event


class LabelEvent(Event):
    '''
    Events of label change on an issue (e.g., 'To Do' => 'In Progress')
    '''
    ACTION_MOVED = 'Moved'

    def __init__(self,
                 hub_name,
                 project_name,
                 user_name,
                 sprint_start_dates,
                 issue_number,
                 issue_title,
                 from_label_event,
                 to_label_event):

        super().__init__(hub_name,
                         project_name,
                         user_name,
                         sprint_start_dates,
                         to_label_event.created_at)

        self.target_type = Event.TARGET_TYPE_GITLAB
        self.action_name = LabelEvent.ACTION_MOVED
        if from_label_event is not None:
            from_label = from_label_event.label.get(mg.LABEL_EVENT_NAME)
        else:
            from_label = ''
        to_label = to_label_event.label.get(mg.LABEL_EVENT_NAME)
        self.action_details = f'{from_label} => {to_label}'
        self.action_details += f': {issue_title} (#{issue_number})'
