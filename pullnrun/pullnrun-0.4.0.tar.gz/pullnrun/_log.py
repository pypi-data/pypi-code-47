from os import getenv
from uuid import uuid4

from requests import request

from pullnrun._utils import as_list, get_log_entry, timestamp

def _status(output_dict):
    status = output_dict.get('status')
    if status == 'SUCCESS':
        return '\u2714'
    if status in ('FAIL', 'ERROR', ):
        return '\u2718'
    if status == 'STARTED':
        return '\u25B6'
    return ' '

def _duration(output_dict):
    start = output_dict.get('meta', {}).get('start')
    end = output_dict.get('meta', {}).get('end')

    if not start or not end:
        return ''

    duration = end - start

    if duration >= 1000:
        return f'{duration/1000:.3f} s'
    return f'{duration} ms'

def _main_text(output_dict):
    if output_dict.get('status') == 'STARTED':
        id_ = output_dict.get('data', {}).get('id')
        return f'Started pullnrun execution with id {id_}'

    if output_dict.get('status') in ('SUCCESS', 'ERROR'):
        success = output_dict.get('data', {}).get('success')
        fail = output_dict.get('data', {}).get('fail')
        duration = _duration(output_dict)

        return f'Finished pullnrun execution in {duration}: {success} out of {success + fail} actions succeeded.'

def _http_details(output_dict):
    type_ = output_dict.get('type', '')
    status_code = str(output_dict.get('data', {}).get('status_code', '')).rjust(4)

    file_ = output_dict.get('data', {}).get('file', '')
    direction = 'to' if 'push' in type_ else 'from'
    url = output_dict.get('data', {}).get('url', '')

    detail = f'{file_} {direction} {url}'

    return (status_code, detail, )

def _s3_details(output_dict):
    type_ = output_dict.get('type', '')

    filename = output_dict.get('data', {}).get('filename', '')
    bucket = output_dict.get('data', {}).get('bucket', '')
    object_name = output_dict.get('data', {}).get('object_name', '')

    if 'push' in type_:
        direction = 'to'
        source, target = filename, object_name
    else:
        direction = 'from'
        source, target = object_name, filename

    target = f' as {target}' if source != target else ''
    detail = f'{source} {direction} S3 bucket {bucket}{target}'

    return detail

def log_to_console(output_dict):
    type_ = output_dict.get('type', '')
    if type_ == 'main':
        print(_main_text(output_dict))
        return

    status = _status(output_dict)
    stage = type_.upper()[:4].ljust(4)

    status_code = ''.rjust(4)
    detail = ''
    output = None

    if type_ in ('pull_http', 'push_http'):
        status_code, detail = _http_details(output_dict)
    elif type_ in ('pull_s3', 'push_s3'):
        detail = _s3_details(output_dict)
    elif type_ == 'run':
        status_code = str(output_dict.get('data', {}).get('exit_code', '')).rjust(4)
        detail = ' '.join(output_dict.get('data', {}).get('command', []))
        output = output_dict.get('data', {}).get('output')

    duration = _duration(output_dict)
    duration = f'({duration})' if duration else ''

    print(f'{status} {status_code} {stage} {detail} {duration}')

    if output:
        end = '\n' if output[-1] != '\n' else ''
        print(f'\n{output}{end}')

def log_to_url(url, id_, log_entry, method=None):
    data = {
        'id': id_,
        'entry': log_entry,
    }
    request(method or 'POST', url, json=data)
    # TODO: communicate errors

class Log:
    def __init__(self, quiet=False, targets=None):
        self._start = None
        self._end = None
        self._id = getenv('PULLNRUN_ID', str(uuid4()))
        self._to_console = not quiet
        self._targets = as_list(targets)

    def _log(self, log_entry):
        if self._to_console:
            log_to_console(log_entry)
        for target in self._targets:
            if target.get('to') == 'url':
                log_to_url(target.get('url'), self._id, log_entry, target.get('method'))

    def __call__(self, log_entry):
        self._log(log_entry)

    @property
    def id(self):
        return self._id

    def start(self):
        self._start = timestamp()
        self._log(
            get_log_entry('main', 'STARTED', start=self._start, id=self._id)
        )

    def end(self, success, fail):
        self._end = timestamp()
        status = 'SUCCESS' if success > 0 and fail == 0 else 'ERROR'
        self._log(
            get_log_entry('main', status, start=self._start, end=self._end, success=success, fail=fail)
        )
