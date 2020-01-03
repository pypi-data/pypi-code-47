import sys
import time
import argparse
import logging
import threading
import subprocess

from . import rrlogger, __version__
from .constants import *
from .lib import AttemptResults


def run():
    parser = _get_parser()
    # ---
    # version
    f = sys.argv.index('--') if '--' in sys.argv else len(sys.argv)
    if '-v' in sys.argv[1:f] or '--version' in sys.argv[1:f]:
        print('retry version {v}'.format(v=__version__))
        exit(0)
    # ---
    # parse arguments
    parsed = parser.parse_args()
    # ---
    # configure logger
    if parsed.verbose:
        rrlogger.setLevel(logging.DEBUG)
    # sanitize arguments
    parsed.tries = max(1, parsed.tries)
    parsed.min = max(MIN_TIMEOUT, parsed.min)
    parsed.max = max(MAX_TIMEOUT, parsed.max) if parsed.max is not None else parsed.min * parsed.tries
    command = ' '.join(parsed.command) if isinstance(parsed.command, list) else parsed.command
    # run command
    res = AttemptResults(parsed.tries)
    for attempt in range(parsed.tries):
        # compute timeout
        timeout = _get_timeout(parsed, attempt)
        rrlogger.info('Attempt #{a} [timeout: {t}]'.format(a=attempt, t=timeout))
        rrlogger.debug('Running "{c}"...'.format(c=command))
        stdin = None if parsed.interactive else subprocess.PIPE
        # spin process
        process = subprocess.Popen(command, shell=True, stdin=stdin)
        # create process monitor
        monitor = threading.Thread(name='process_monitor', target=_process_monitor, args=(process, timeout, res, attempt))
        monitor.start()
        monitor.join()
        assert res[attempt] != 'ND'
        rrlogger.debug('The attempt #{a} finished with code: {c}'.format(a=attempt, c=res[attempt]))
        # check what happened
        if res[attempt] == 0:
            rrlogger.info('Attempt #{a} succeeded!'.format(a=attempt))
            # the command succeeded
            break
        # the command failed or timed-out
        if parsed.on_retry:
            rrlogger.info('Executing on-retry command')
            try:
                subprocess.check_call(parsed.on_retry, shell=True)
            except:
                pass
        if res[attempt] is None:
            # process timed out, try again (or die)
            rrlogger.info('Attempt #{a} timed out!'.format(a=attempt))
        else:
            # process failed, try again (if requested)
            rrlogger.info('Attempt #{a} failed with exit code: {c}'.format(a=attempt, c=res[attempt]))
            if parsed.no_retry_on_error:
                break
    succeeded = len(list(filter(lambda r: r == 0, res))) > 0
    if not succeeded:
        rrlogger.info('All attempts exhausted, no success reported!')
        # run on-failure command (if given)
        if parsed.on_fail:
            rrlogger.info('Executing on-fail command')
            try:
                subprocess.check_call(parsed.on_fail, shell=True)
            except:
                pass
    # ---
    rrlogger.info('Done!')


def _get_timeout(parsed, attempt):
    return min(parsed.min * (attempt + 1), parsed.max)

def _process_monitor(process, timeout, results, attempt):
    start = time.time()
    while (process.poll() is None) and ((time.time() - start) < timeout):
        time.sleep(1.0 / PROCESS_MONITOR_HEARTBEAT_HZ)
    # process ended, return its exit code
    if process.poll() is not None:
        results[attempt] = process.returncode
        return
    # process timed out
    rrlogger.debug('The process is taking too long to finish. It will be terminated.')
    start = time.time()
    escalated_to_sigkill = False
    while process.poll() is None:
        if (time.time() - start > 10):
            if not escalated_to_sigkill:
                escalated_to_sigkill = True
                rrlogger.info('Escalating to SIGKILL')
            process.kill()
        else:
            process.terminate()
        # sleep
        time.sleep(1)
    # indicate that the process was killed
    results[attempt] = None

def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--min',
        type=int,
        required=True,
        help="Minimum timeout (in seconds)"
    )
    parser.add_argument(
        '-M', '--max',
        type=int,
        default=None,
        help="Maximum timeout (in seconds)"
    )
    parser.add_argument(
        '-n', '--tries',
        type=int,
        default=3,
        help="Maximum number of retries"
    )
    parser.add_argument(
        '--no-retry-on-error',
        dest='no_retry_on_error',
        action='store_true',
        default=False,
        help="Do not retry when the command fails (as opposed to time out)"
    )
    parser.add_argument(
        '-', '--on-fail',
        default=None,
        help="Command to run after last failure"
    )
    parser.add_argument(
        '-c', '--on-retry',
        default=None,
        help="Command to run after every failed attempt"
    )
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        default=False,
        help="Whether to run the commands in interactive mode"
    )
    parser.add_argument(
        '-D', '--dry-run',
        action='store_true',
        default=False,
        help="Performs a dry-run. It shows which commands would run"
    )
    parser.add_argument(
        '--verbose', '--debug',
        dest='verbose',
        action='store_true',
        default=False,
        help="Run in verbose mode"
    )
    parser.add_argument(
        'command',
        nargs='+'
    )
    return parser
