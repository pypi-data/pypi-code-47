"""
    An interface to quickly install this tool as a systemd service
"""

import logging
import os
from shutil import copy2
from subprocess import check_call, check_output, CalledProcessError
import time
import sys
import shutil

SYSTEMD_PREINSTALL_FILE = os.path.realpath(os.path.join(os.path.dirname(__file__), "dockershield.service"))
SYSTEMD_POSTINSTALL_FILE = "/usr/lib/systemd/system/dockershield.service"

SYSTEMD_POSTINSTALL_EXECUTABLE = "/usr/local/bin/dockershield"
if os.path.isdir(sys.argv[0]):
    SYSTEMD_PREINSTALL_EXECUTABLE = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","scripts","dockershield"))
else:
    SYSTEMD_PREINSTALL_EXECUTABLE = shutil.which(sys.argv[0])

def stop():
    logging.debug("Stop any running service")
    check_call(["systemctl", "stop", "dockershield"])

def reload_daemon():
    logging.debug("Reload systemd daemon")
    check_call(["systemctl", "daemon-reload"])

def enable():
    logging.debug("Enable systemd service")
    check_call(["systemctl", "enable", "dockershield"])

def status():
    output = check_output(["systemctl", "status", "dockershield"])
    logging.debug("systemctl status: \n"+str(output, 'utf8'))
    return output

def restart():
    logging.debug("Start systemd service")
    check_call(["systemctl", "restart", "dockershield"])
    # FIXME: Hack: Wait for service to startup properly
    trial = 0
    max_trials = 3
    while trial < max_trials:
        trial += 1
        try:
            status()
            break
        except CalledProcessError:
            if trial > 3:
                raise
            time.sleep(10)

def disable():
    logging.debug("Disable systemd service")
    check_call(["systemctl", "disable", "dockershield"])


def install():
    os.environ["SYSTEMD_PAGER"] = ""
    if not os.path.exists(SYSTEMD_POSTINSTALL_EXECUTABLE):
        logging.debug("Create symbolic link at %s" % SYSTEMD_POSTINSTALL_EXECUTABLE)
        os.symlink(SYSTEMD_PREINSTALL_EXECUTABLE, SYSTEMD_POSTINSTALL_EXECUTABLE)
    logging.debug("Unit file at %s" % (SYSTEMD_PREINSTALL_FILE,))
    logging.debug("Destination %s" %  SYSTEMD_POSTINSTALL_FILE)
    logging.debug("Copy unit file")
    copy2(SYSTEMD_PREINSTALL_FILE, SYSTEMD_POSTINSTALL_FILE)
    reload_daemon()
    restart()

def uninstall():
    os.environ["SYSTEMD_PAGER"] = ""
    stop()
    disable()
    logging.debug("Remove unit file at %s" % SYSTEMD_POSTINSTALL_FILE)
    os.unlink(SYSTEMD_POSTINSTALL_FILE)
    reload_daemon()
    if os.path.islink(SYSTEMD_POSTINSTALL_EXECUTABLE):
        logging.debug("Remove symbolic link at %s" % SYSTEMD_POSTINSTALL_EXECUTABLE)
        os.unlink(SYSTEMD_POSTINSTALL_EXECUTABLE)


def process_args(args):
    """
    Processes an argparse.Namespace and returns True if any actions were taken
    """
    result = False
    if args.systemd_install:
        logging.info("Installing as Systemd unit.")
        install()
        logging.info("Installation complete!")
        result = True
    if args.systemd_uninstall:
        logging.info("Removing any Systemd unit.")
        uninstall()
        logging.info("Removal complete!")
        result = True
    return result
