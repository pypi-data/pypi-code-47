# dbnomics-fetcher-toolbox
# Toolbox of functions and data types helping writing DBnomics fetchers.
# By: Christophe Benz <christophe.benz@cepremap.org>
#
# Copyright (C) 2019 Cepremap
# https://git.nomics.world/dbnomics/dbnomics-fetcher-toolbox
#
# dbnomics-fetcher-toolbox is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# dbnomics-fetcher-toolbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""Functions and data types helping processing resources in DBnomics fetchers."""


import argparse
import asyncio
import shutil
from pathlib import Path
from typing import Awaitable, Callable, Dict, Sequence, Set

import daiquiri
from contexttimer import Timer
from humanfriendly import format_number, format_timespan, pluralize
from pydantic import BaseModel
from toolz import take

from .status import EventType, ResourceEvent, ResourceStatus

logger = daiquiri.getLogger(__name__)

ResourceId = str


class Resource(BaseModel):
    """A resource to be processed by :func:`process_resources`."""

    id: ResourceId

    def create_context(self):
        """Create a context necessary to process the resource.

        This method is called by :func:`process_resources` before calling
        ``process_resource``.

        Override it to do anything you need (e.g. creating a directory...).
        """

    def delete(self):
        """Delete a resource.

        This method is called by :func:`process_resources` if any error occurred
        during the execution of the ``process_resource`` callback.

        Override it to do anything you need (e.g. delete a directory...).
        """


class DbnomicsDatasetResource(Resource):
    """A resource representing a dataset converted to DBnomics data model."""

    base_dir: Path

    @property
    def target_dir(self) -> Path:
        """Directory where the dataset will be written, following DBnomics data model.

        The name of the directory is the resource ``id``.
        """
        return self.base_dir / self.id

    def create_context(self):
        """Create the dataset target directory, following DBnomics data model."""
        self.target_dir.mkdir(exist_ok=True)

    def delete(self):
        """Delete the dataset target directory, following DBnomics data model."""
        shutil.rmtree(self.target_dir)


ProcessResourceCallback = Callable[[Resource], Awaitable[None]]
OnEventCallback = Callable[[ResourceEvent], None]


async def process_resources(
    resources: Sequence[Resource],
    args: argparse.Namespace,
    process_resource: ProcessResourceCallback,
    on_event: OnEventCallback = None,
    events: Sequence[ResourceEvent] = None,
) -> Dict[ResourceId, ResourceEvent]:
    """Handle the common work of processing resources.

    Iterate over ``resources``:

    * removing the excluded ones if the ``--exclude`` option is used
    * keeping only some of them if the ``--only`` option is used

    By default, any resource already processed is skipped,
    whatever its status was (SUCCESS or FAILURE).
    If the option ``--retry-failed`` is used, retry resources with FAILURE status.
    If the option ``--force`` is used, process all resources.

    For each resource, call ``process_resource(resource)``, logging messages allowing
    to track the processing progress.
    If an exception is raised during the execution of ``process_resource``:

    * log the error and process the next resource or re-raise
      if ``--fail-fast`` option is used
    * call ``resource.delete()`` if ``--delete-on-error`` option is used
    """
    resource_event_by_id = {
        event.id: event for event in events or [] if event.type == EventType.RESOURCE
    }

    resources_to_process = get_resources_to_process(resources, args)

    if not resources_to_process:
        logger.debug(
            "No resource to process was found among %s",
            pluralize(len(resources), "resource"),
        )
        return resource_event_by_id

    ids = ", ".join(resource.id for resource in resources_to_process)
    logger.debug(
        "About to process %s: %s",
        pluralize(len(resources_to_process), "resource"),
        ids,
    )

    await _process_resources_in_sequence(
        args=args,
        process_resource=process_resource,
        resources_to_process=resources_to_process,
        resource_event_by_id=resource_event_by_id,
        on_event=on_event,
    )

    return resource_event_by_id


async def _process_resources_in_sequence(
    args: argparse.Namespace,
    process_resource: ProcessResourceCallback,
    resources_to_process: Sequence[Resource],
    resource_event_by_id: Dict[ResourceId, ResourceEvent],
    on_event: OnEventCallback = None,
):
    for resource_number, resource in enumerate(resources_to_process, start=1):
        await _process_resource_wrapper(
            args=args,
            process_resource=process_resource,
            resources_to_process=resources_to_process,
            resource_event_by_id=resource_event_by_id,
            resource=resource,
            resource_number=resource_number,
            on_event=on_event,
        )


async def _process_resource_wrapper(
    args: argparse.Namespace,
    process_resource: ProcessResourceCallback,
    resources_to_process: Sequence[Resource],
    resource_event_by_id: Dict[ResourceId, ResourceEvent],
    resource: Resource,
    resource_number: int,
    on_event: OnEventCallback = None,
):
    # Skip previous executed steps if "events" sequence was given.
    event = resource_event_by_id.get(resource.id)
    if (
        not args.force
        and event is not None
        and (not args.retry_failed or event.status != ResourceStatus.FAILURE)
    ):
        logger.debug(
            "Skipping resource %d/%d because it has already been processed (%s)",
            resource_number,
            len(resources_to_process),
            event.status.value,
            resource=resource.id,
        )
        return

    logger.info(
        "Processing resource %d/%d",
        resource_number,
        len(resources_to_process),
        resource=resource.id,
    )

    with Timer() as t:
        resource.create_context()
        try:
            if asyncio.iscoroutinefunction(process_resource):
                await process_resource(resource)
            else:
                process_resource(resource)
        except Exception as exc:
            event = ResourceEvent(
                id=resource.id,
                status=ResourceStatus.FAILURE,
                duration=t.elapsed,
                message=str(exc),
            )
            resource_event_by_id[resource.id] = event
            if on_event:
                on_event(event)
            if args.delete_on_error:
                logger.debug("Deleting resource data", resource=resource.id)
                resource.delete()
            logger.error(  # noqa
                "Error processing resource after %s",
                format_timespan(t.elapsed),
                resource=resource.id,
                exc_info=not args.fail_fast,
            )
            if args.fail_fast:
                raise
        else:
            event = ResourceEvent(
                id=resource.id, status=ResourceStatus.SUCCESS, duration=t.elapsed,
            )
            resource_event_by_id[resource.id] = event
            if on_event:
                on_event(event)
            logger.info(
                "Resource processed in %s",
                format_timespan(t.elapsed),
                resource=resource.id,
            )


def get_resources_to_process(
    resources: Sequence[Resource], args: argparse.Namespace
) -> Sequence[Resource]:
    """Apply ``--only``, ``--exclude`` and ``--limit`` script options."""

    def check_invalid(option_ids: Set[ResourceId], option_name: str) -> Set[ResourceId]:
        """Check for invalid resources and return valid ones."""
        invalid_resources = option_ids - ids
        if invalid_resources:
            logger.error(
                "%s were given to %s: %s",
                pluralize(len(invalid_resources), "invalid resource"),
                option_name,
                ", ".join(sorted(invalid_resources)),
            )
        valid_resources = option_ids - invalid_resources
        return valid_resources

    resources_to_process = resources
    ids = {resource.id for resource in resources}

    if args.only:
        valid_only = check_invalid(set(args.only), "--only")
        logger.debug(
            "Process only %d of %s because of --only: %s",
            len(valid_only),
            pluralize(len(resources), "resource"),
            ", ".join(valid_only),
        )
        resources_to_process = [
            resource for resource in resources_to_process if resource.id in valid_only
        ]

    if args.exclude:
        valid_exclude = check_invalid(set(args.exclude), "--exclude")
        logger.debug(
            "Exclude %d of %s because of --exclude: %s",
            len(valid_exclude),
            pluralize(len(resources), "resource"),
            ", ".join(valid_exclude),
        )
        resources_to_process = [
            resource
            for resource in resources_to_process
            if resource.id not in valid_exclude
        ]

    if args.limit is not None:
        logger.debug(
            "%s because of --limit",
            "Process only the first resource"
            if args.limit == 1
            else "Don't process any resource"
            if args.limit == 0
            else f"Process only the {format_number(args.limit)} first resources",
        )
        resources_to_process = list(take(args.limit, resources_to_process))

    return resources_to_process
