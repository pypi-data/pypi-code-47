import pandas as pd


class UserCurrentSession:
    """One user's current session. This stores the start of the session,
    the number of events in the session, and the name of the event
    """

    def __init__(self, user_id, start_time, events, last_time=None):
        self.user_id = user_id
        if last_time:
            self.last_timestamp = last_time
        else:
            self.last_timestamp = start_time
        self.first_timestamp = start_time

        self.events_in_session = events + ","
        # if isinstance(events, list):
        #     self.events_in_session = events
        # else:
        #     self.events_in_session = [events]

    def log(self, event_timestamp, events, duration=30):
        # if new event within 30 min of last event for user,
        # update session end timestamp with this time and
        # add one to event count
        if (event_timestamp - self.last_timestamp).seconds < duration * 60:
            self.last_timestamp = event_timestamp
            self.events_in_session += events + ","
            # if isinstance(events, list):
            #     self.events_in_session += events
            # else:
            #     self.events_in_session += [events]
            return None

        # else the previous session is done so close it
        # and initialize a new session with the current event's timestamp
        else:
            db_record = self.close_session()
            self.__init__(self.user_id, event_timestamp, events)
            return db_record

    def close_session(self):
        return {
            "duration": (self.last_timestamp - self.first_timestamp).seconds / 60,
            "total_events": len(self.events_in_session[:-1].split(",")),
            "user_id": self.user_id,
            "timestamp": self.first_timestamp,
            "last_timestamp": self.last_timestamp,
            "events": self.events_in_session[:-1],
        }


class Sessions:
    """A collection of all sessions in the current computation.
    Includes both open and closed sessions.
    """

    def __init__(self):
        self.current_sessions = {}
        self.closed_sessions = []

    def add_event(self, user_id, timestamp, events, duration=30):

        if self.current_sessions.get(user_id) is None:
            session = UserCurrentSession(user_id, timestamp, events)
            self.current_sessions[user_id] = session

        else:
            log_output = self.current_sessions[user_id].log(timestamp, events, duration)

            if log_output is not None:
                self.closed_sessions.append(log_output)

    def close_open_sessions(self):
        for open_session in self.current_sessions.values():
            self.closed_sessions.append(open_session.close_session())

    def write_to_db(self, table, db, if_exists="append", index=False):
        sessions_df = pd.DataFrame.from_records(self.closed_sessions)
        sessions_df = sessions_df.sort_values("last_timestamp", ascending=True)
        sessions_df.to_sql(table, db, if_exists=if_exists, index=index)
