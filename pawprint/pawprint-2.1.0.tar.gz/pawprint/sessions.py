import pandas as pd


class UserCurrentSession:
    """
    One user's current session. This stores the start and end of the 
    session, the number of events in the session, and the name of the event.
    """

    def __init__(self, user_id, start_time, events, last_time=None):
        """
        Instantiate a new user session, given the user's ID,
        the time of the event, and the event itself.
        """

        # Store the user's ID and the timestamp of the start of this session
        self.user_id = user_id
        self.first_timestamp = start_time

        # If the user had a known previous session end time, let's store that
        if last_time is not None:
            self.last_timestamp = last_time
        # Otherwise, let's store this event as the last known event
        else:
            self.last_timestamp = start_time

        self.events_in_session = events + ","

    def log_event(self, event_timestamp, events, duration=30):
        """
        Log an event to this user's current session.
        """

        # If the event is within the session
        if (event_timestamp - self.last_timestamp).seconds < duration * 60:

            # Update the current session's last event time
            # and add the event to the list of events
            self.last_timestamp = event_timestamp
            self.events_in_session += events + ","

            # The session is ongoing, so don't return a session data payload
            return None

        # Otherwise, this event is part of a new session
        else:
            # Close the existing session
            db_record = self.close_session()

            # Reinitialise the current session to a fresh session
            self.__init__(self.user_id, event_timestamp, events)

            # Return data about the session that just closed
            return db_record

    def close_session(self):
        """
        The current session has come to a close when we received an event
        outside of the max inter-event duration. As such, construct a 
        payload that contains information about this session, for later storage.
        """
        return {
            "duration": (self.last_timestamp - self.first_timestamp).seconds / 60,
            "total_events": len(self.events_in_session[:-1].split(",")),
            "user_id": self.user_id,
            "timestamp": self.first_timestamp,
            "last_timestamp": self.last_timestamp,
            "events": self.events_in_session[:-1],
        }


class Sessions:
    """
    A collection of all sessions in the current computation.
    Includes both open and closed sessions.
    """

    def __init__(self):

        # We map current users (by their user_id) to existing (open) sessions
        self.current_sessions = {}

        # Closed sessions are a list of payloads for writing to the database
        self.closed_sessions = []

    def log_event(self, user_id, timestamp, events, duration=30):
        """
        Log an event. If the user has an existing session open, it will be
        added to that session; otherwise, a new one will be created for them.
        """

        # If the user doesn't have an open session
        if self.current_sessions.get(user_id) is None:
            # Then create a new one, and store that current session
            session = UserCurrentSession(user_id, timestamp, events)
            self.current_sessions[user_id] = session

        # Otherwise, log the event to their existing session
        else:
            log_output = self.current_sessions[user_id].log_event(
                timestamp, events, duration
            )

            # If they had a previous session, this event may be far enough in time from
            # the last event to close that previous session. If so, take the last
            # session's payload and append it to our list of closed sessions
            if log_output is not None:
                self.closed_sessions.append(log_output)

    def close_open_sessions(self):
        """
        When we've iterated through all events, we're ready to write all sessions
        to the database. This closes all existing open sessions, in order to
        have all session information ready to save to the database.
        """
        for open_session in self.current_sessions.values():
            self.closed_sessions.append(open_session.close_session())
        self.current_sessions = {}

    def write_to_db(self, table, db, if_exists="append", index=False):
        """
        Write all sessions to a database.
        """

        # Cast all sessions to dataframe
        sessions_df = pd.DataFrame.from_records(self.closed_sessions)

        # If we have sessions to write, sort them and write to the database
        if sessions_df.shape[0] > 0:
            sessions_df = sessions_df.sort_values("last_timestamp", ascending=True)
            sessions_df.to_sql(table, db, if_exists=if_exists, index=index)

        # Don't double-write closed events
        self.closed_sessions = []
