import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy.exc import ProgrammingError

from pawprint import Tracker, Sessions, UserCurrentSession


class Statistics(object):
    """
    This class interfaces with an existing Tracker and calculated derived statistics.
    """

    def __init__(self, tracker):
        self.tracker = tracker

    def __getitem__(self, tracker):
        """
        Overload the [] operator. This is used to access the various statistics tables.
        """
        return Tracker(
            db=self.tracker.db, table="{}__{}".format(self.tracker.table, tracker)
        )

    def sessions(self, duration=30, clean=False, batch_size=100000):
        """Create a table of user sessions."""

        # Create a tracker for basic interaction
        stats = self["sessions"]

        # Initialize a Sessions container
        open_sessions = Sessions()

        # If we're starting clean, drop the database table containint existing sessions
        if clean:
            stats.drop_table()

        # This try statement contains a few SQL queries; if any of them fail with a
        # ProgrammingError, the try is exited and the sessions will be rebuilt from scratch.
        try:
            # Try to get the time of the very last event stored in the database
            # If the query fails, sessions will be built from scratch
            last_entry = pd.read_sql(
                "SELECT last_timestamp FROM {} ORDER BY last_timestamp DESC LIMIT 1".format(
                    stats.table
                ),
                self.tracker.db,
            ).loc[0, "last_timestamp"]

            # All events after this time are new to us, so construct the query
            # to get the list of unique users since this last event
            user_query = "SELECT DISTINCT({}) FROM {} WHERE {} > %(last_entry)s".format(
                self.tracker.user_field,
                self.tracker.table,
                self.tracker.timestamp_field,
            )
            params = {"last_entry": str(last_entry)}

            # Get the unique users since the last data we've tracked
            unique_users = pd.read_sql(user_query, self.tracker.db, params=params)[
                self.tracker.user_field
            ].values

            # If there are no users, exit because there's nothing to update
            if len(unique_users) == 0:
                return

            # Construct a PostgreSQL-friendly string representing the list of unique users
            unique_user_str = (
                "('" + "','".join([str(user) for user in unique_users]) + "')"
            )

            # Grab the last recorded session for each user in unique users
            last_sessions = pd.read_sql(
                "SELECT DISTINCT ON ({}) * FROM {} WHERE {} IN {} ORDER BY {}, last_timestamp DESC".format(
                    self.tracker.user_field,
                    stats.table,
                    self.tracker.user_field,
                    unique_user_str,
                    self.tracker.user_field,
                ),
                self.tracker.db,
            )

            # Create UserCurrentSession() from last session of each unique user
            for _, session in last_sessions.iterrows():
                existing_session = UserCurrentSession(
                    user_id=session["user_id"],
                    start_time=session["timestamp"],
                    events=session["events"],
                    last_time=session["last_timestamp"],
                )
                open_sessions.current_sessions[session["user_id"]] = existing_session

            # We've fully reconstructed the last session of each user, so handle the case
            # where the user's session was not finished when we last built Sessions
            # Now we need to delete those sessions from the database so we don't double-count
            rows_to_delete = zip(
                last_sessions["user_id"].values, last_sessions["timestamp"].values
            )

            # Delete the last recorded sessions from the sessions table
            try:
                for user, time in rows_to_delete:
                    time = pd.Timestamp(time)
                    delete_session_query = "DELETE FROM {} WHERE {} = '{}' AND {} = '{}'".format(
                        stats.table,
                        self.tracker.user_field,
                        user,
                        self.tracker.timestamp_field,
                        time,
                    )
                    pd.io.sql.execute(delete_session_query, con=self.tracker.db)
            except ProgrammingError:
                raise

        except ProgrammingError:  # raised when some query above fails; triggers full session rebuild
            last_entry = datetime(1900, 1, 1)
            params = {"last_entry": str(last_entry)}

        # We have previous session information for all relevant users, if there is any
        # We can now read all events since the last recorded event and construct sessions
        # Let's grab the first batch of new events from the events table
        batch_number = 0
        events_query = "SELECT * FROM {} WHERE {} > %(last_entry)s LIMIT {} OFFSET {}".format(
            self.tracker.table,
            self.tracker.timestamp_field,
            batch_size,
            batch_size * batch_number,
        )
        events = pd.read_sql(events_query, self.tracker.db, params=params)

        # While there are events, read them in batches and add them to user session data
        while events.shape[0] > 0:

            print("batch: ", batch_number)
            print("num events in batch: ", events.shape[0])

            # Process events that we have read
            for _, event_row in events.iterrows():  # loop through events
                open_sessions.log_event(  # add events to Sessions()
                    user_id=event_row["user_id"],
                    timestamp=event_row["timestamp"],
                    events=event_row["event"],
                    duration=duration,
                )

            # Write all (sorted) closed sessions to database
            # This resets `open_sessions.closed_sessions` to empty list
            # and leaves `open_sessions.current_sessions` as-is for next run through loop
            open_sessions.write_to_db(
                table=stats.table, db=self.tracker.db, if_exists="append", index=False
            )

            # Grab the next batch of events from the database
            batch_number += 1
            events = pd.read_sql(
                "SELECT * FROM {} WHERE {} > %(last_entry)s LIMIT {} OFFSET {}".format(
                    self.tracker.table,
                    self.tracker.timestamp_field,
                    batch_size,
                    batch_size * batch_number,
                ),
                self.tracker.db,
                params=params,
            )

        # Close and write any leftover open sessions
        open_sessions.close_open_sessions()
        open_sessions.write_to_db(
            table=stats.table, db=self.tracker.db, if_exists="append", index=False
        )

    def engagement(self, clean=False, start=None, min_sessions=3):
        """Calculates the daily and monthly average users, and the stickiness as the ratio."""

        # Create a tracker for basic interaction
        stats = self["engagement"]

        # If we're starting clean, delete the table
        if clean:
            stats.drop_table()

        # Determine whether the stats table exists and contains data, or if we should create one
        try:  # if this passes, the table exists and may contain data
            last_entry = pd.read_sql(
                "SELECT timestamp FROM {} ORDER BY timestamp DESC LIMIT 1".format(
                    stats.table
                ),
                self.tracker.db,
            ).loc[0, "timestamp"]
        except ProgrammingError:  # otherwise, the table doesn't exist
            last_entry = None

        # If a start_date isn't passed, start from the last known date, or from the beginning
        if not start:
            if last_entry:
                start = last_entry + timedelta(days=1)
            else:
                start = "1900-01-01"  # datetime(year=1900, month=1, day=1).date()

        # If we're also calculating by imposing a minimum number of events per user
        if min_sessions:
            # Count the number of rows per user in the sessions table
            session_counts = (
                self["sessions"].read().groupby(self.tracker.user_field).count()
            )

            # Select the active users where there are at least min_sessions rows per user
            active_users = session_counts[
                session_counts["duration"] >= min_sessions
            ].index
            active_users = [str(user) for user in active_users]

            # If there are no users that qualify, turn off min_sessions calculations
            if not len(active_users):
                min_sessions = 0

        # DAU : daily active users
        stickiness = self["sessions"].count(
            "DISTINCT({})".format(self.tracker.user_field), timestamp__gt=start
        )
        if not len(stickiness):  # if this has been run too recently, do nothing
            return
        stickiness.rename(
            columns={"count": "dau", "datetime": "timestamp"}, inplace=True
        )
        stickiness.index = pd.to_datetime(stickiness["timestamp"])
        stickiness.drop("timestamp", axis=1, inplace=True)
        stickiness = stickiness.resample("D").sum().fillna(0).astype(int)

        # Calculate DAU for active users if requested
        if min_sessions:
            active_users_query = {
                "{}__in".format(self.tracker.user_field): list(active_users)
            }
            active_dau = self["sessions"].count(
                "DISTINCT({})".format(self.tracker.user_field),
                timestamp__gt=start,
                **active_users_query
            )
            active_dau.index = pd.to_datetime(active_dau["datetime"])
            active_dau = active_dau.resample("D").sum().fillna(0).astype(int)
            stickiness["dau_active"] = active_dau["count"]

        # Weekly and monthly average users
        stickiness["wau"] = np.nan
        stickiness["mau"] = np.nan

        if min_sessions:
            stickiness["wau_active"] = np.nan
            stickiness["mau_active"] = np.nan

        # Calculate weekly and monthly average users
        for date in stickiness.index:
            weekly = (
                self["sessions"]
                .read(
                    "DISTINCT({})".format(self.tracker.user_field),
                    timestamp__gt=date - timedelta(days=6),
                    timestamp__lte=date + timedelta(days=1),
                )
                .count()
            )
            monthly = (
                self["sessions"]
                .read(
                    "DISTINCT({})".format(self.tracker.user_field),
                    timestamp__gt=date - timedelta(days=29),
                    timestamp__lte=date + timedelta(days=1),
                )
                .count()
            )

            # Calculate WAU and MAU for active users only if requested
            if min_sessions:
                weekly_active = (
                    self["sessions"]
                    .read(
                        "DISTINCT({})".format(self.tracker.user_field),
                        timestamp__gt=date - timedelta(days=6),
                        timestamp__lte=date + timedelta(days=1),
                        **active_users_query
                    )
                    .count()
                )
                monthly_active = (
                    self["sessions"]
                    .read(
                        "DISTINCT({})".format(self.tracker.user_field),
                        timestamp__gt=date - timedelta(days=29),
                        timestamp__lte=date + timedelta(days=1),
                        **active_users_query
                    )
                    .count()
                )

                stickiness.loc[date, "wau_active"] = weekly_active.iloc[0]
                stickiness.loc[date, "mau_active"] = monthly_active.iloc[0]

            stickiness.loc[date, "wau"] = weekly.iloc[0]
            stickiness.loc[date, "mau"] = monthly.iloc[0]

        # Calculate engagement as DAU / MAU
        stickiness["engagement"] = stickiness.dau / stickiness.mau
        if min_sessions:
            stickiness["engagement_active"] = (
                stickiness.dau_active / stickiness.mau_active
            )

        # Active user counts should be ints
        stickiness.wau = stickiness.wau.astype(int)
        stickiness.mau = stickiness.mau.astype(int)
        if min_sessions:
            stickiness.wau_active = stickiness.wau_active.astype(int)
            stickiness.mau_active = stickiness.mau_active.astype(int)

        # Write the engagement data to the database
        stickiness.sort_index().to_sql(stats.table, stats.db, if_exists="append")
