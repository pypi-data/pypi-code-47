import logging
from collections import namedtuple
from typing import Optional
from datetime import datetime, date

from .plugin.settings_service import PluginSettingsService, PluginSettingMissingError
from .project import Project
from .plugin import PluginType, PluginRef
from .db import project_engine
from .utils import nest, iso8601_datetime, coerce_datetime, find_named, NotFound
from .meltano_file import Schedule


class ScheduleAlreadyExistsError(Exception):
    """Occurs when a schedule already exists."""

    def __init__(self, schedule):
        self.schedule = schedule


class ScheduleDoesNotExistError(Exception):
    """Occurs when a schedule does not exist."""

    def __init__(self, name):
        self.name = name


class ScheduleService:
    def __init__(
        self, project: Project, plugin_settings_service: PluginSettingsService = None
    ):
        self.project = project
        self.plugin_settings_service = plugin_settings_service or PluginSettingsService(
            project
        )

    def add(
        self,
        session,
        name,
        extractor: str,
        loader: str,
        transform: str,
        interval: str,
        start_date: Optional[datetime] = None,
        **env,
    ):
        start_date = coerce_datetime(start_date) or self.default_start_date(
            session, extractor
        )

        schedule = Schedule(
            name, extractor, loader, transform, interval, start_date, env=env
        )

        return self.add_schedule(schedule)

    def remove(self, name):
        return self.remove_schedule(name)

    def default_start_date(self, session, extractor: str) -> datetime:
        """
        Returns the `start_date` of the extractor, or now.
        """
        extractor_ref = PluginRef(PluginType.EXTRACTORS, extractor)
        start_date = None
        try:
            start_date, _ = self.plugin_settings_service.get_value(
                session, extractor_ref, "start_date"
            )
        except PluginSettingMissingError:
            logging.debug(f"`start_date` not found in {extractor}.")

        # TODO: this coercion should be handled by the `kind` attribute
        # on the actual setting
        if isinstance(start_date, date):
            return coerce_datetime(start_date)

        if isinstance(start_date, datetime):
            return start_date

        return iso8601_datetime(start_date) or datetime.utcnow()

    def add_schedule(self, schedule: Schedule):
        with self.project.meltano_update() as meltano:
            # guard if it already exists
            if schedule in meltano.schedules:
                raise ScheduleAlreadyExistsError(schedule)

            meltano.schedules.append(schedule)

        return schedule

    def remove_schedule(self, name: str):
        with self.project.meltano_update() as meltano:
            try:
                # guard if it doesn't exist
                schedule = find_named(self.schedules(), name)
            except NotFound:
                raise ScheduleDoesNotExistError(name)

            # find the schedules plugin config
            meltano.schedules.remove(schedule)

        return name

    def schedules(self):
        return self.project.meltano.schedules
