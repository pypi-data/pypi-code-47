from argparse import Namespace

import socket
import sys
import os
import logging
from shutil import copy2
from subprocess import check_call, check_output, CalledProcessError
import time
import select

from .connection import Connection
from .arguments import config, dump_config, SYSTEMD_PREINSTALL_FILE, SYSTEMD_POSTINSTALL_FILE, CONFIGURATION_FILE
from .systemd import systemd
from .filtering import Filters

LOG_FORMATTER = "%(asctime)s : %(levelname)s : %(message)s"

class DockerShield():
    """
    Main class.
    Typically this will be a singleton.
    """

    def __init__(self, args):
        """
        Constructor
            Input:
                args: An argparse.Namespace, see arguments.py for arguments definition
        """
        self.args = args
        self.filtered_socket = None
        self.connections = []
        self.restart_requested = False
        assert(isinstance(args, Namespace))

    class Exception(Exception):
        """
        Exception wrapper
        """
        pass

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()

    def close(self):
        """
        Close all active connections and stop listening for clients
        """
        i = 0
        while len(self.connections) > 0:
            logging.debug("Close connection number %d" % (i,))
            connection = self.connections.pop()
            connection.close()
            i += 1

        if self.filtered_socket is not None:
            logging.debug("Close filtered socket at %s" % (self.args.filtered_socket_path))
            self.filtered_socket.close()
            self.filtered_socket = None

        if os.path.exists(self.args.filtered_socket_path):
            logging.debug("Unlink filtered socket path at %s" % (self.args.filtered_socket_path,))
            os.unlink(self.args.filtered_socket_path)

    def connect_upstream(self):
        """
        Open a socket to the docker server
        """
        upstream_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        upstream_socket.connect(self.args.docker_socket_path)
        return upstream_socket

    def open(self):
        """
        Open the downstream socket for connections.
        Also does a test that the upstream socket exists and can be connected to.
        Handles some common errors and raises exceptions.
        """
        assert(self.filtered_socket is None)
        if not os.path.exists(self.args.docker_socket_path):
            raise DockerShield.Exception("docker_socket_path \"%s\" does not exist" % (self.args.docker_socket_path,))

        logging.debug("Test upstream socket at %s actually exists and accepts connections" % (self.args.docker_socket_path,))
        upstream_socket = self.connect_upstream()
        upstream_socket.close()

        logging.debug("Create filtered socket at %s" % (self.args.filtered_socket_path,))
        if os.path.isdir(self.args.filtered_socket_path):
            logging.warn("The filtered socket at %s is a directory; this could happen if you tried to mount the path as a volume before running this script." \
                % (self.args.filtered_socket_path,)
            )
            if not os.listdir(self.args.filtered_socket_path):
                logging.warn("Since the directory is empty, we will try to remove it")
                os.rmdir(self.args.filtered_socket_path)
            else:
                raise DockerShield.Exception("A non-empty directory exists at %s" % (self.args.filtered_socket_path,))

        if os.path.exists(self.args.filtered_socket_path):
            raise DockerShield.Exception("filtered_socket_path \"%s\" already exists" % (self.args.filtered_socket_path,))

        self.filtered_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        logging.debug("Listen for clients at %s" % (self.args.filtered_socket_path,))
        self.filtered_socket.bind(self.args.filtered_socket_path)
        self.filtered_socket.listen(1)

    def configure_logging(self):
        """
        Configure the Python built-in logging module
        """
        # Verbose means to log everything,
        # Silent means to log nothing,
        # Otherwise, we log at level INFO
        if self.args.verbose:
            assert(not self.args.silent)
            logging.basicConfig(format=LOG_FORMATTER, level=logging.DEBUG)
        elif not self.args.silent:
            assert(not self.args.verbose)
            logging.basicConfig(format=LOG_FORMATTER, level=logging.INFO)

    def configure_filters(self):
        filters_as_dictionary = {
            "method" : {
                "blacklist" : self.args.blacklist_method,
                "whitelist" : self.args.whitelist_method
            },
            "url" : {
                "include_version" : self.args.filter_includes_version,
                "blacklist" : self.args.blacklist,
                "whitelist" : self.args.whitelist
            }
        }
        self.filters = Filters(filters_as_dictionary)

    def file_has_changed(self, filename):
        return os.stat(filename).st_mtime >= self.start_time

    def accept_connection(self):
        """
        Accept a connection, spawn Connection instance and add to table
        """
        logging.debug("Waiting on connection...")
        connection, _ = self.filtered_socket.accept()
        connection_id = len(self.connections)
        logging.debug("Client[%d] connected to %s" % (connection_id, self.args.filtered_socket_path,))
        new_connection = Connection(connection, self.connect_upstream(), self, self.filters)
        self.connections += [new_connection]
        # The Connection is a Thread, so must be started
        new_connection.start()

    def inner_loop(self):
        if not self.args.watch_config:
            self.accept_connection()
            return

        if self.file_has_changed(CONFIGURATION_FILE):
            logging.info("Configuration file %s was modified, stopping..." % CONFIGURATION_FILE)
            self.restart_requested = True
            self.running = False
            return

        readable, _, _ = select.select([self.filtered_socket], [], [], 2.0)
        if self.filtered_socket in readable:
            self.accept_connection()



    def run(self):
        """
        Main loop
        """
        self.configure_logging()
        logging.info("Configuration is at:")
        logging.info(CONFIGURATION_FILE)
        logging.debug("Full Configuration Dump\n"+dump_config())

        if systemd.process_args(self.args):
            return

        if self.args.edit_config:
            editor = os.environ.get("EDITOR", "vi")
            os.execlp(editor, editor, CONFIGURATION_FILE)
            raise NotImplementedError("This should be unreachable")

        if self.args.dry_run:
            # FIXME: Is it really a dry run if it has side effects?
            logging.info("Dry run. Will check that sockets can be opened and then exit")

        self.configure_filters()

        self.open()
        self.running = not self.args.dry_run
        self.restart_requested = False
        self.start_time = time.time()
        while self.running:
            try:
                self.inner_loop()
            except KeyboardInterrupt:
                logging.info("Got KeyboardInterrupt, exiting...")
                self.running = False

        self.close()
        if self.args.dry_run:
            logging.info("Dry run. Success!")
        logging.debug("Clean exit.")
