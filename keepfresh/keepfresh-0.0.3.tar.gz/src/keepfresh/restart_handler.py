#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger(__name__)

class RestartHandler:
    def __init__(self, observer, interval, command):
        self.observer = observer
        self.interval = interval
        self.command = command

    def run(self):
        logger.info("Running restart handler")
        command_process = subprocess.Popen(self.command)

        while True:
            events = self.observer.observe_and_update()

            if events:
                logger.info("Restarting the process")
                command_process.terminate()
                command_process.wait()
                command_process = subprocess.Popen(self.command)
