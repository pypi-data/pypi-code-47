import subprocess

from ._utils import timestamp, get_log_entry

def run(log, command, directory=None, **_):
    kwargs = {
        'stdout': subprocess.PIPE,
        'stderr': subprocess.STDOUT,
        'text': True,
    }

    status = 'STARTED'
    returncode = None
    stdout = None
    errors = []

    start = timestamp()
    log(get_log_entry('run', status, command=command, start=start))

    try:
        cp = subprocess.run(command, cwd=directory, check=False, **kwargs)
        returncode = cp.returncode
        status = 'SUCCESS' if returncode == 0 else 'FAIL'
        stdout = str(cp.stdout)
    except Exception as e:
        errors.append(f'Executing the command failed. ({type(e).__name__})')
        status = 'ERROR'
    end = timestamp()

    log(get_log_entry('run', status, command=command, exit_code=returncode, output=stdout, start=start, end=end, errors=errors))
    return status == 'SUCCESS'
