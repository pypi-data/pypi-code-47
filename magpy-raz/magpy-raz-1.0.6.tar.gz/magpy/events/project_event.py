import magpy.general as mg
from magpy.events.base import Event


class ProjectEvent(Event):
    '''
    GitLab project event
    '''
    __NEW_PROJECT = 'new project'

    def __init__(self,
                 hub_name,
                 project_name,
                 user_name,
                 sprint_start_dates,
                 gl_event):

        super().__init__(hub_name,
                         project_name,
                         user_name,
                         sprint_start_dates,
                         gl_event.created_at)

        self.action_name = gl_event.action_name.capitalize()
        self.target_type = self.__target_type(gl_event.target_type)
        self.action_details = self.__action_details(gl_event)

    def __target_type(self, target_type):
        '''
        Event can be either a Gitlab event or a Repository one
        '''
        if target_type is None:
            return Event.TARGET_TYPE_REPOSITOTY

        return Event.TARGET_TYPE_GITLAB

    def __action_details(self, gl_event):
        '''
        Returns a string with the event action details
        '''
        action_text = gl_event.action_name.capitalize()
        if gl_event.target_type is not None:
            if gl_event.action_name == mg.EVENT_ACTION_COMMENTED_ON:
                action_subject = gl_event.note.get(mg.NOTEABLE_TYPE)
                action_text += f' {action_subject.lower()}'
            else:
                action_text += f' {gl_event.target_type.lower()}'
            if gl_event.target_title is not None:
                action_text += f': {gl_event.target_title}'

        # Add issue number
        issue_number = None
        if gl_event.action_name in (mg.EVENT_ACTION_OPENED,
                                    mg.EVENT_ACTION_CLOSED):
            issue_number = gl_event.target_iid
        elif gl_event.action_name == mg.EVENT_ACTION_COMMENTED_ON:
            issue_number = gl_event.note.get(mg.NOTEABLE_IID)

        if issue_number is not None:
            action_text += f' (#{issue_number})'

        # Pushed to repository
        if gl_event.action_name == mg.EVENT_ACTION_PUSHED_TO:
            action_text += f' {gl_event.push_data.get(mg.PUSH_REF_TYPE)}'
            action_text += f' {gl_event.push_data.get(mg.PUSH_REF)}'
            commit_title = gl_event.push_data.get(mg.PUSH_COMMIT_TITLE)
            if commit_title is not None:
                action_text += f': {commit_title}'

        # Pushed new branch
        if gl_event.action_name == mg.EVENT_ACTION_PUSHED_NEW:
            action_text += ' ' + gl_event.push_data.get(mg.PUSH_REF_TYPE)
            branch_name = gl_event.push_data.get(mg.PUSH_REF)
            if branch_name is not None:
                action_text += f' {branch_name}'

        # Created new branch/repository
        if gl_event.action_name == mg.EVENT_ACTION_CREATED:
            action_text += f' {ProjectEvent.__NEW_PROJECT}'

        return action_text
