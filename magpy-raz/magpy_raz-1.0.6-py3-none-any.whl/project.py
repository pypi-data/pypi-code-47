import datetime
import operator
import time
import threading
import magpy.general as mg
from magpy.events.project_event import ProjectEvent
from magpy.events.label_event import LabelEvent
from magpy.sprint_items.sprint_issue import SprintIssue
from magpy.sprint_items.sprint_balance import SprintBalance
from magpy.sprint_items.sprint_progress import SprintProgress
from magpy.sprint import Sprint
from magpy.backlog_issue import BacklogIssue


class Project:
    '''
    Represents a Magshimim project, with all its data
    '''

    def __init__(self, gl, hub_name, start_date, end_date, gl_project):
        start = time.time()

        # Project
        self.project = gl_project
        self.name = gl_project.name
        self.start_date = start_date
        self.end_date = end_date
        issues = self.project.issues.list(all=True, simple=True)
        events = self.project.events.list(all=True)

        # Group
        self.group = gl.gitlab.groups.get(self.project.namespace.get('id'))

        # Hub name
        self.hub_name = hub_name

        # Sprints
        self.sprints = self.__sprints(issues)

        # Events
        self.events = self.__project_events(events)
        self.events += self.__label_events(issues)

        # Backlog
        self.backlog = self.__backlog(issues)

        elapsed = round(time.time() - start, 1)
        print(f'{self.hub_name}: {self.name} loaded in {elapsed}s')

    def __project_events(self, gl_events):
        '''
        Returns a list of project events
        '''
        events = []
        sprint_start_dates = [s.start_date for s in self.sprints]
        for gl_event in gl_events:
            user_name = gl_event.author.get(mg.EVENT_NAME)
            event = ProjectEvent(hub_name=self.hub_name,
                                 project_name=self.name,
                                 user_name=user_name,
                                 sprint_start_dates=sprint_start_dates,
                                 gl_event=gl_event)
            events.append(event)
        return events

    def __label_events(self, gl_issues):
        '''
        Returns a list of label events, for each related issue
        '''
        threads = []
        issue_events = [[] for i in range(len(gl_issues))]
        sprint_start_dates = [s.start_date for s in self.sprints]
        for i, gl_issue in enumerate(gl_issues):
            thread = threading.Thread(target=self.get_label_events,
                                      args=[gl_issue, self.hub_name,
                                            self.name,
                                            sprint_start_dates,
                                            i, issue_events])
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Combine all events to a sinle list
        events = [event for events in issue_events for event in events]

        return events

    def __backlog(self, issues):
        '''
        Returns the project backlog
        '''
        backlog = []
        for issue in issues:
            issue_is_open = issue.state == mg.ISSUE_STATE_OPENED
            not_in_milestone = issue.milestone is None
            not_assigned = issue.assignee is None
            # only open issues, unassigned and not associated with a milestone
            # are considered as a backlog issue
            if issue_is_open and not_in_milestone and not_assigned:
                backlog.append(BacklogIssue(self, issue))

        return backlog

    def __sprints(self, issues):
        '''
        Returns a list of sprints and their associated issues.
        If no valid sprint (milestones) exists, consider the entire
        project as sprint 0.
        '''
        # Start date
        sprints = []
        for milestone in self.project.milestones.list():
            if milestone.start_date is not None and milestone.due_date is not None:
                # Milestones with start and due dates can be made into sprints
                start_date = mg.str_to_date(milestone.start_date)
                end_date = mg.str_to_date(milestone.due_date)
                sprint = Sprint(milestone, start_date, end_date)
                sprints.append(sprint)

        if len(sprints) > 0:
            sprints.sort(key=operator.attrgetter('start_date'))
        else:
            # No valid milestones => entire project is sprint 0
            sprints.append(Sprint(None, self.start_date, self.end_date))

        # Collect data for all sprint issues
        for n, sprint in enumerate(sprints):
            sprint.number = n
            allocated = 0

            # Sprint issues
            for gl_issue in issues:
                if gl_issue.milestone is None:
                    continue

                milestone_id = gl_issue.milestone.get(mg.MILESTONE_ID)
                if milestone_id != sprint.milestone_id:
                    continue

                issue = SprintIssue(self, sprint, gl_issue)
                sprint.items.append(issue)

                allocated += issue.work

            # Sprint balance: unallocated time vs budget
            if sprint.budget > 0:
                balance = sprint.budget - allocated
                sprint_balance = SprintBalance(self, sprint, balance)
                sprint.items.append(sprint_balance)

            # Sprint progress: estimated percentage of sprint at current time
            progress = SprintProgress(self, sprint)
            sprint.items.append(progress)

        return sprints

    def get_label_events(self, gl_issue, hub_name, project_name,
                         sprint_start_dates, i, events):
        '''
        Get all the label changes of an issue. Specifically, look
        for change event pairs, happening at the same time
        '''
        label_events = gl_issue.resourcelabelevents.list()

        remove_label_event = None
        for label_event in label_events:
            if label_event.label is None:
                continue

            if label_event.action == mg.LABEL_EVENT_REMOVE:
                remove_label_event = label_event
            else:
                if remove_label_event is not None:
                    same_time_events = label_event.created_at == remove_label_event.created_at
                    if same_time_events:
                        # Change issue status event (e.g., To Do => In
                        # Progress)
                        user_name = label_event.user.get(mg.LABEL_EVENT_NAME)
                        event = LabelEvent(hub_name=hub_name,
                                           project_name=project_name,
                                           user_name=user_name,
                                           sprint_start_dates=sprint_start_dates,
                                           issue_number=gl_issue.iid,
                                           issue_title=gl_issue.title,
                                           from_label_event=remove_label_event,
                                           to_label_event=label_event)
                        events[i].append(event)

                elif label_event.label.get(mg.LABEL_EVENT_NAME) in \
                        (mg.LABEL_TO_DO, mg.LABEL_IN_PROGRESS, mg.LABEL_DONE):
                    # Set issue initial status (e.g., => To Do)
                    user_name = label_event.user.get(mg.LABEL_EVENT_NAME)
                    event = LabelEvent(hub_name=hub_name,
                                       project_name=project_name,
                                       user_name=user_name,
                                       sprint_start_dates=sprint_start_dates,
                                       issue_number=gl_issue.iid,
                                       issue_title=gl_issue.title,
                                       from_label_event=None,
                                       to_label_event=label_event)
                    events[i].append(event)
