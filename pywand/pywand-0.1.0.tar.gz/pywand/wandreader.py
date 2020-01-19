#! /usr/bin/env python3

import configparser
import re
import signal
import subprocess

class WandInputReader:

    def __read_device(self):
        """
            This is a generator, returning lines from ir-ctl
        """

        self.popen = subprocess.Popen(self.irctl_cmd, stdout=subprocess.PIPE)
        for stdout_line in iter(self.popen.stdout.readline, ""):
            yield stdout_line.decode('UTF-8').strip().split()


    def get_codes(self):
        """
            This is a generator that interprets codes and returns a
            dictionary value.
        """
        pulses = []

        for ir_sig in self.__read_device():

            # we expect lines from irctl to come in an expected format
            # toss out anything that doesn't conform
            if len(ir_sig) != 2:
                continue
            if not ir_sig[1].isdigit():
                continue

            # separate code type and time, collect pulses, and wait for
            # timeout.  We ignore spaces, since we've set the timeout low
            # in the ir-ctl cli option
            codetype = ir_sig[0]
            codetime = int(ir_sig[1])

            if codetype == 'pulse':
                pulses.append(codetime)

            elif codetype == 'timeout':
                if len(pulses) == 56:

                    # compares pulse width to determine binary values
                    # from testing, 410 seems to be best.
                    bin_bits = map(
                        lambda x: int(pulses[x] >= self.pulse_time_thresh),
                        range(56),
                    )
                    bin_str = "".join([str(x) for x in bin_bits])

                    # each signal has three parts
                    yield {
                        "zero": bin_str[0:8],
                        "wand": bin_str[8:32],
                        "motion": bin_str[32:56],
                    }

                else:
                    print("bad code length, {}".format(len(pulses)))

                # clear out pulses before taking on a new one.
                pulses.clear()


    def handle_sigterm(self, signum, frame):
        """
            Terminate the child process on sigterm.
            Since everything else is a generator, everything will exit gracefully.
        """
        if self.popen:
            self.popen.terminate()


    def __init__(self, config_file_path="wand_config.ini"):

        config = configparser.ConfigParser()
        config.read(config_file_path)

        # pulse width used to determine 1 vs 0
        self.pulse_time_thresh = config.getint('IR', 'pulse_time_thresh', fallback=410)

        # define the ir-ctl command based on config values
        ir_device = config.get('IR', 'ir_device', fallback="/dev/lirc0")
        ir_timeout = config.getint('IR', 'ir_timeout', fallback=2000)
        self.irctl_cmd = ["ir-ctl", "-d", ir_device, "-r", "-t", str(ir_timeout)]

        self.pattern = re.compile(r"^(\w+)\s+(\d+)$")

        signal.signal(signal.SIGINT, self.handle_sigterm)
        signal.signal(signal.SIGTERM, self.handle_sigterm)

