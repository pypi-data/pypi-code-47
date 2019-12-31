from __future__ import unicode_literals
import os, sys

if sys.version_info < (3, 0):
    print(
        "Are you using Python 2.x? Byexample no longer runs in that version. Please upgrade your Python environment."
    )
    sys.exit(1)

from .cache import RegexCache
from .jobs import Jobs, Status, allow_sigint
from .log import init_log_system


def execute_examples(filename, sigint_handler):
    global cache, harvester, executor, options, dry
    from .common import human_exceptions

    with human_exceptions("processing the file '%s'" % filename) as exc, \
            cache.synced(label=filename), \
            allow_sigint(sigint_handler):
        examples = harvester.get_examples_from_file(filename)
        if dry:
            return executor.dry_execute(examples, filename)
        else:
            return executor.execute(examples, filename)

    user_aborted = isinstance(exc.get('exc'), KeyboardInterrupt)
    error = not user_aborted
    return True, True, user_aborted, error


def main(args=None):
    global cache, harvester, executor, options, dry

    init_log_system()

    cache_disabled = os.getenv('BYEXAMPLE_CACHE_DISABLED', "1") != "0"
    cache_verbose = os.getenv('BYEXAMPLE_CACHE_VERBOSE', "0") != "0"
    cache = RegexCache('0', cache_disabled, cache_verbose)

    with cache.activated(auto_sync=True, label="0"):
        from .cmdline import parse_args
        from .common import human_exceptions
        from .init import init

        args = parse_args(args)

        dry = args.dry
        with human_exceptions('initializing byexample') as exc:
            testfiles, harvester, executor, options = init(args)

        if exc:
            sys.exit(Status.error)

        jobs = Jobs(args.jobs)
        return jobs.run(execute_examples, testfiles, options['fail_fast'])
