# Imports from python.
import logging


# Imports from other dependencies.
from celery import shared_task


logger = logging.getLogger("tasks")


@shared_task(bind=True)
def gather_all_files(self, grouped_files):
    created_files = [
        file
        for per_task_file_list in grouped_files
        for file in per_task_file_list
        if isinstance(per_task_file_list, list)
    ]

    created_files.extend(
        [file for file in grouped_files if not isinstance(file, list)]
    )

    logger.info(f"Created {len(created_files)} file(s).")

    return created_files
