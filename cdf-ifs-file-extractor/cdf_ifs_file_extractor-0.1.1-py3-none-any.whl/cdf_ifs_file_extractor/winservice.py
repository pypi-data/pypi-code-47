import win32service
import win32serviceutil
import win32event

import argparse
import logging
import os
import sys
import servicemanager
from pathlib import Path

from cognite.client import CogniteClient
from cognite.client.exceptions import CogniteAPIError

from .helper import configure_logger
from .monitoring import Monitor
from .utils import read_yaml
from .file_uploader import FileUploader


class PySvc(win32serviceutil.ServiceFramework):
    # you can NET START/STOP the service by the following name
    _svc_name_ = "CDF_IFS_File_Extractor"
    # this text shows up as the service name in the Service
    # Control Manager (SCM)
    _svc_display_name_ = "CDF IFS File extractor"
    # this text shows up as the description in the SCM
    _svc_description_ = "This service import exported IFS files from a folder."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

        try:
            config = read_yaml(os.environ.get("CDF_IFS_CONFIG_FILE"))
        except OSError as exc:
            logging.error("Failed to load yaml config: {}. {}".format(args.conf, exc))
            sys.exit(1)

        try:
            configure_logger(
                config.get("log_level", logging.INFO), Path(config.get("log_path", "log")),
            )
            client = CogniteClient(
                api_key=os.environ.get(config.get("api_key_name")),
                project=config.get("project"),
                base_url=config.get("base_url"),
                client_name=config.get("client_name"),
                timeout=config.get("client_timeout"),
            )
            login_status = client.login.status()
            logging.info(login_status)
            if not login_status.logged_in:
                logging.error("Not logged in to CDF API")
                sys.exit(2)
        except CogniteAPIError as exc:
            logging.error("Failed to create CDF client: {!s}".format(exc))
            sys.exit(2)

        path = config.get("path")
        mapping_file = config.get("mapping_file")

        monitor = Monitor(namespace="cdf_ifs_file_extractor", project_name=login_status.project)
        monitor.push()
        logging.info(
            "Start uploading files from path: %s \n using the mapping file: %s", path, mapping_file,
        )

        self.fileUploader = FileUploader(monitor=monitor, client=client, path=path, mapping_file=mapping_file)

    # core logic of the service
    def SvcDoRun(self):

        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_, ""),
        )

        rc = None
        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            self.fileUploader.process_csv()
            # block for one hour and listen for a stop event
            rc = win32event.WaitForSingleObject(self.hWaitStop, 60 * 60 * 1000)

    # called when we're being shut down
    def SvcStop(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STOPPING, (self._svc_name_, ""),
        )
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
        win32event.SetEvent(self.hWaitStop)


def install():
    win32serviceutil.HandleCommandLine(PySvc)
