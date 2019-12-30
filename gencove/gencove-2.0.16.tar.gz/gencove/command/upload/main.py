"""Entry point into upload command."""
import os
import uuid
from datetime import datetime
from time import sleep

import backoff

import requests

from gencove.client import APIClientError  # noqa: I100
from gencove.command.base import Command, ValidationError
from gencove.constants import FASTQ_MAP_EXTENSION, SAMPLE_ASSIGNMENT_STATUS
from gencove.utils import (
    batchify,
    get_regular_progress_bar,
    get_s3_client_refreshable,
)

from .constants import (
    ASSIGN_BATCH_SIZE,
    ASSIGN_ERROR,
    FASTQ_EXTENSIONS,
    TMP_UPLOADS_WARNING,
    UPLOAD_PREFIX,
    UPLOAD_STATUSES,
)
from .exceptions import SampleSheetError, UploadError, UploadNotFound
from .multi_file_reader import MultiFileReader
from .utils import (
    get_filename_from_path,
    get_get_upload_details_retry_predicate,
    get_gncv_path,
    parse_fastqs_map_file,
    seek_files_to_upload,
    upload_file,
    upload_multi_file,
)


class Upload(Command):
    """Upload command executor."""

    def __init__(self, source, destination, credentials, options):
        super(Upload, self).__init__(credentials, options)
        self.source = source
        self.destination = destination
        self.project_id = options.project_id
        self.fastqs = []
        self.fastqs_map = {}
        self.upload_ids = set()

    @staticmethod
    def generate_gncv_destination():
        """Autogenerate gencove destination path."""
        return "{}cli-{}-{}".format(
            UPLOAD_PREFIX,
            datetime.utcnow().strftime("%Y%m%d%H%M%S"),
            uuid.uuid4().hex,
        )

    def initialize(self):
        """Initialize upload command parameters from provided arguments."""
        self.echo_debug("Host is {}".format(self.options.host))
        self.echo_warning(TMP_UPLOADS_WARNING, err=True)

        if os.path.isfile(self.source) and self.source.endswith(
            FASTQ_MAP_EXTENSION  # pylint: disable=C0330
        ):
            self.echo_debug("Scanning fastqs map file")
            self.fastqs_map = parse_fastqs_map_file(self.source)
        else:
            self.echo_debug("Seeking files to upload")
            self.fastqs = list(seek_files_to_upload(self.source))

        if not self.destination:
            self.destination = self.generate_gncv_destination()
            self.echo(
                "Files will be uploaded to: {}".format(self.destination)
            )

        # Make sure there is just one trailing slash. Only exception is
        # UPLOAD_PREFIX itself, which can have two trailing slashes.
        if self.destination != UPLOAD_PREFIX:
            self.destination = self.destination.rstrip("/")
            self.destination += "/"

        self.login()

    def validate(self):
        """Validate command setup before execution.

        Raises:
            ValidationError - if something is wrong with command parameters.
        """
        if self.destination and not self.destination.startswith(
            UPLOAD_PREFIX  # pylint: disable=C0330
        ):
            self.echo(
                "Invalid destination path. Must start with '{}'".format(
                    UPLOAD_PREFIX
                ),
                err=True,
            )
            raise ValidationError("Bad configuration. Exiting.")

        if not self.fastqs and not self.fastqs_map:
            self.echo(
                "No FASTQ files found in the path. "
                "Only following files are accepted: {}".format(
                    FASTQ_EXTENSIONS
                ),
                err=True,
            )
            raise ValidationError("Bad configuration. Exiting.")

    def execute(self):
        """Upload fastq files from host system to Gencove cloud.

        If project id was provided, all fastq files will
        be assigned to this project, after upload.
        """
        s3_client = get_s3_client_refreshable(
            self.api_client.get_upload_credentials
        )

        if self.fastqs:
            self.upload_from_source(s3_client)
        elif self.fastqs_map:
            self.upload_from_map_file(s3_client)

        self.echo_debug("Upload ids are now: {}".format(self.upload_ids))
        if self.project_id:
            self.echo_debug("Cooling down period.")
            sleep(10)
            self.assign_uploads_to_project()

    def upload_from_source(self, s3_client):
        """Upload command with <source> argument provided."""
        for file_path in self.fastqs:
            upload = self.upload_from_file_path(file_path, s3_client)
            if self.project_id and upload:
                self.upload_ids.add(upload["id"])

        self.echo("All files were successfully uploaded.")

    def upload_from_map_file(self, s3_client):
        """Upload fastq files from a csv file."""
        for key, fastqs in self.fastqs_map.items():
            upload = self.concatenate_and_upload_fastqs(
                key, fastqs, s3_client
            )
            if self.project_id and upload:
                self.upload_ids.add(upload["id"])

        self.echo("All files were successfully uploaded.")

    def concatenate_and_upload_fastqs(self, key, fastqs, s3_client):
        """Upload fastqs parts as one file."""
        client_id, r_notation = key
        self.echo_debug(
            "Uploading fastq. client_id={} r_notation={}".format(
                client_id, r_notation
            )
        )
        self.echo_debug("FASTQS: {}".format(fastqs))

        gncv_path = self.destination + get_gncv_path(client_id, r_notation)
        self.echo_debug("Calculated gncv path: {}".format(gncv_path))

        upload_details = self.get_upload_details(
            gncv_path, dict(client_id=client_id, r_notation=r_notation)
        )

        if upload_details["last_status"]["status"] == UPLOAD_STATUSES.done:
            self.echo("File was already uploaded: {}".format(gncv_path))
            return upload_details

        self.echo("Uploading to {}".format(gncv_path))
        upload_multi_file(
            s3_client,
            MultiFileReader(fastqs),
            upload_details["s3"]["bucket"],
            upload_details["s3"]["object_name"],
        )
        return upload_details

    def upload_from_file_path(self, file_path, s3_client):
        """Prepare file and upload, if it wasn't uploaded yet.

        Args:
            file_path (str): a local system path to a file to be uploaded.
            s3_client (boto3 s3 client): instantiated boto3 S3 client.

        Returns:
            dict representing upload details
        """
        clean_file_path = get_filename_from_path(file_path, self.source)
        self.echo_debug(
            "Uploading clean file path: {}".format(clean_file_path)
        )
        gncv_notated_path = self.destination + clean_file_path

        self.echo(
            "Checking if file was already uploaded: {}".format(
                clean_file_path
            )
        )

        upload_details = self.get_upload_details(gncv_notated_path)
        if upload_details["last_status"]["status"] == UPLOAD_STATUSES.done:
            self.echo("File was already uploaded: {}".format(clean_file_path))
            return upload_details

        self.echo("Uploading {} to {}".format(file_path, gncv_notated_path))
        upload_file(
            s3_client=s3_client,
            file_name=file_path,
            bucket=upload_details["s3"]["bucket"],
            object_name=upload_details["s3"]["object_name"],
        )
        return upload_details

    @backoff.on_predicate(
        backoff.expo, get_get_upload_details_retry_predicate, max_tries=10
    )
    def get_upload_details(self, gncv_path, extra_params=None):
        """Get upload details with retry for last status update."""
        return self.api_client.get_upload_details(gncv_path, extra_params)

    def assign_uploads_to_project(self):
        """Assign uploads to a project and trigger a run."""
        self.echo("Assigning uploads to project {}".format(self.project_id))

        try:
            samples = self.build_samples(self.upload_ids)
        except (UploadError, SampleSheetError):
            self.echo_warning(
                ASSIGN_ERROR.format(self.project_id, self.destination)
            )
            return

        if not samples:
            self.echo_debug("No related samples were found")
            self.echo_warning(
                ASSIGN_ERROR.format(self.project_id, self.destination)
            )
            return

        self.echo_debug("Sample sheet now is: {}".format(samples))

        self.echo_debug(
            "Assigning samples to project ({})".format(self.project_id)
        )

        assigned_count = 0
        progress_bar = get_regular_progress_bar(len(samples), "Assigning: ")
        progress_bar.start()
        for samples_batch in batchify(samples, batch_size=ASSIGN_BATCH_SIZE):
            try:
                samples_batch_len = len(samples_batch)
                self.echo_debug(
                    "Assigning batch: {}".format(samples_batch_len)
                )
                self.api_client.add_samples_to_project(
                    samples_batch, self.project_id
                )
                assigned_count += samples_batch_len
                progress_bar.update(samples_batch_len)
                self.echo_debug("Total assigned: {}".format(assigned_count))
            except APIClientError as err:
                self.echo_debug(err)
                self.echo_warning(
                    "There was an error assigning/running samples."
                )
                if assigned_count > 0:
                    self.echo_warning(
                        "Some of the samples were assigned. "
                        "Please use the Web UI to assign "
                        "the rest of the samples"
                    )
                else:
                    self.echo_warning(
                        ASSIGN_ERROR.format(self.project_id, self.destination)
                    )
                progress_bar.finish()
                return

        progress_bar.finish()
        self.echo("Assigned all samples to a project")

    @backoff.on_exception(
        backoff.expo, (SampleSheetError, UploadNotFound), max_time=300
    )
    def build_samples(self, uploads):
        """Get samples for current uploads.

        Returns:
            list of dict: a list of samples for the uploads.
        """
        # make a copy of uploads so as not to change the input
        search_uploads = uploads.copy()
        samples = []
        for sample_sheet in self.sample_sheet_paginator():
            if not sample_sheet:
                self.echo_debug("Sample sheet returned empty.")
                raise UploadError

            for sample in sample_sheet:
                self.echo_debug("Checking sample: {}".format(sample))
                add_it = False
                if "r1" in sample["fastq"]:
                    if sample["fastq"]["r1"]["upload"] in search_uploads:
                        add_it = True
                        search_uploads.remove(sample["fastq"]["r1"]["upload"])
                        self.echo_debug(
                            "Found sample for upload r1: {}".format(
                                sample["fastq"]["r1"]["upload"]
                            )
                        )
                    else:
                        self.echo_debug(
                            "R1 upload not found. sample {} uploads {}".format(
                                sample, search_uploads
                            )
                        )
                        raise UploadNotFound
                if "r2" in sample["fastq"]:
                    if sample["fastq"]["r2"]["upload"] in search_uploads:
                        add_it = True
                        search_uploads.remove(sample["fastq"]["r2"]["upload"])
                        self.echo_debug(
                            "Found sample for upload r2: {}".format(
                                sample["fastq"]["r2"]["upload"]
                            )
                        )
                    else:
                        self.echo_debug(
                            "R2 upload not found. sample {} uploads {}".format(
                                sample, search_uploads
                            )
                        )
                        raise UploadNotFound

                if add_it:
                    samples.append(sample)

        if search_uploads:
            self.echo_debug(
                "Have uploads without samples: {}".format(search_uploads)
            )
            raise SampleSheetError

        return samples

    def sample_sheet_paginator(self):
        """Paginate over all sample sheets for the destination.

        Yields:
            paginated lists of samples
        """
        more = True
        next_link = None
        while more:
            self.echo_debug("Get sample sheet page")
            try:
                resp = self.get_sample_sheet(next_link)
                yield resp["results"]
                next_link = resp["meta"]["next"]
                more = next_link is not None
            except APIClientError as err:
                self.echo_debug(err)
                raise UploadError

    @backoff.on_exception(
        backoff.expo,
        (requests.exceptions.ConnectionError, requests.exceptions.Timeout),
        max_tries=5,
        max_time=30,
    )
    def get_sample_sheet(self, next_link=None):
        """Get samples by gncv path."""
        return self.api_client.get_sample_sheet(
            self.destination, SAMPLE_ASSIGNMENT_STATUS.unassigned, next_link
        )
