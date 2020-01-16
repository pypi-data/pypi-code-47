# Imports from python.
import json


# Imports from other dependencies.
from celery import chord
from celery import shared_task


# Imports from race_ratings.
from raceratings.models import RaceRating
from raceratings.tasks.utils.deltas import generate_delta_page
from raceratings.tasks.utils.deltas import get_changed_ratings
from raceratings.tasks.utils.deltas import split_days_into_pages
from raceratings.tasks.utils.io import upload_file
from raceratings.tasks.utils.workflow import gather_all_files


@shared_task(acks_late=True)
def bake_overall_deltas(election_year, include_special_elections):
    """Bake 'rating changelist' JSON files for all bodies and races.

    URLs of data produced (on S3, under UPLOADED_FILES_PREFIX):

        /changelist
            /page-001.json
            /page-002.json
    """
    changed_ratings = get_changed_ratings(election_year, None)

    day_pages = split_days_into_pages(changed_ratings)

    files_created = []

    for i, days_on_current_page in enumerate(day_pages):
        current_page = i + 1

        page_filename, page_payload = generate_delta_page(
            None,
            current_page,
            days_on_current_page,
            changed_ratings,
            len(day_pages),
        )

        s3_file_location = upload_file(page_filename, json.dumps(page_payload))

        files_created.append(s3_file_location)

    if not day_pages:
        blank_filename, blank_payload = generate_delta_page(
            None, 1, [], RaceRating.objects.none(), 1
        )

        s3_file_location = upload_file(
            blank_filename, json.dumps(blank_payload)
        )

        files_created.append(s3_file_location)

    return files_created


@shared_task(acks_late=True)
def bake_electoral_college_deltas(election_year, include_special_elections):
    """Bake 'rating changelist' JSON files for the electoral college.

    URLs of data produced (on S3, under UPLOADED_FILES_PREFIX):

        /electoral-college
            /changelist
                /page-001.json
                /page-002.json
    """
    changed_ratings = get_changed_ratings(election_year, "electoral-college")

    day_pages = split_days_into_pages(changed_ratings)

    files_created = []

    for i, days_on_current_page in enumerate(day_pages):
        current_page = i + 1

        page_filename, page_payload = generate_delta_page(
            "electoral-college",
            current_page,
            days_on_current_page,
            changed_ratings,
            len(day_pages),
        )

        s3_file_location = upload_file(page_filename, json.dumps(page_payload))

        files_created.append(s3_file_location)

    if not day_pages:
        blank_filename, blank_payload = generate_delta_page(
            "electoral-college", 1, [], RaceRating.objects.none(), 1
        )

        s3_file_location = upload_file(
            blank_filename, json.dumps(blank_payload)
        )

        files_created.append(s3_file_location)

    return files_created


@shared_task(acks_late=True)
def bake_senate_deltas(election_year, include_special_elections):
    """Bake 'rating changelist' JSON files for the U.S. Senate.

    URLs of data produced (on S3, under UPLOADED_FILES_PREFIX):

        /senate
            /changelist
                /page-001.json
                /page-002.json
    """
    changed_ratings = get_changed_ratings(election_year, "senate")

    day_pages = split_days_into_pages(changed_ratings)

    files_created = []

    for i, days_on_current_page in enumerate(day_pages):
        current_page = i + 1

        page_filename, page_payload = generate_delta_page(
            "senate",
            current_page,
            days_on_current_page,
            changed_ratings,
            len(day_pages),
        )

        s3_file_location = upload_file(page_filename, json.dumps(page_payload))

        files_created.append(s3_file_location)

    if not day_pages:
        blank_filename, blank_payload = generate_delta_page(
            "senate", 1, [], RaceRating.objects.none(), 1
        )

        s3_file_location = upload_file(
            blank_filename, json.dumps(blank_payload)
        )

        files_created.append(s3_file_location)

    return files_created


@shared_task(acks_late=True)
def bake_house_deltas(election_year, include_special_elections):
    """Bake 'rating changelist' JSON files for the U.S. House.

    URLs of data produced (on S3, under UPLOADED_FILES_PREFIX):

        /house
            /changelist
                /page-001.json
                /page-002.json
    """
    changed_ratings = get_changed_ratings(election_year, "house")

    day_pages = split_days_into_pages(changed_ratings)

    files_created = []

    for i, days_on_current_page in enumerate(day_pages):
        current_page = i + 1

        page_filename, page_payload = generate_delta_page(
            "house",
            current_page,
            days_on_current_page,
            changed_ratings,
            len(day_pages),
        )

        s3_file_location = upload_file(page_filename, json.dumps(page_payload))

        files_created.append(s3_file_location)

    if not day_pages:
        blank_filename, blank_payload = generate_delta_page(
            "house", 1, [], RaceRating.objects.none(), 1
        )

        s3_file_location = upload_file(
            blank_filename, json.dumps(blank_payload)
        )

        files_created.append(s3_file_location)

    return files_created


@shared_task(acks_late=True)
def bake_governor_deltas(election_year, include_special_elections):
    """Bake 'rating changelist' JSON files for gubernatorial races.

    URLs of data produced (on S3, under UPLOADED_FILES_PREFIX):

        /governors
            /changelist
                /page-001.json
                /page-002.json
    """
    changed_ratings = get_changed_ratings(election_year, "governorships")

    day_pages = split_days_into_pages(changed_ratings)

    files_created = []

    for i, days_on_current_page in enumerate(day_pages):
        current_page = i + 1

        page_filename, page_payload = generate_delta_page(
            "governors",
            current_page,
            days_on_current_page,
            changed_ratings,
            len(day_pages),
        )

        s3_file_location = upload_file(page_filename, json.dumps(page_payload))

        files_created.append(s3_file_location)

    if not day_pages:
        blank_filename, blank_payload = generate_delta_page(
            "governors", 1, [], RaceRating.objects.none(), 1
        )

        s3_file_location = upload_file(
            blank_filename, json.dumps(blank_payload)
        )

        files_created.append(s3_file_location)

    return files_created


@shared_task(acks_late=True)
def bake_all_race_rating_deltas(election_year, include_special_elections=True):
    publish_queue = chord(
        [
            # group([
            #     task.si(
            #         *i.args
            #     )
            #     for i in items
            # ]),
            bake_electoral_college_deltas.si(
                election_year, include_special_elections
            ),
            bake_senate_deltas.si(election_year, include_special_elections),
            bake_house_deltas.si(election_year, include_special_elections),
            bake_governor_deltas.si(election_year, include_special_elections),
            bake_overall_deltas.si(election_year, include_special_elections),
        ],
        gather_all_files.s(),
    )
    publish_queue.apply_async()
