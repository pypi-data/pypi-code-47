from requests import request

try:
    import boto3
except ImportError:
    pass

from ._utils import timestamp, filter_dict, get_log_entry, void_fn, prefix_object

def _push_http(filename, url, method='PUT', data=None, headers=None, log=void_fn):
    status = 'STARTED'
    status_code = None

    start = timestamp()
    log(get_log_entry('push_http', status, start=start, url=url, filename=filename))
    errors = []

    try:
        with open(filename, 'rb') as f:
            files = {'file': (filename, f)}
            r = request(method, url, data=data, headers=headers, files=files)
            status_code = r.status_code
            r.raise_for_status()
            status = 'SUCCESS'
    except Exception as e:
        errors.append(f'Uploading the file failed. ({type(e).__name__})')
        status = 'ERROR'
    end = timestamp()

    log(get_log_entry('push_http', status, start=start, end=end, url=url, filename=filename, status_code=status_code, errors=errors))
    return status == 'SUCCESS'

def _push_s3(bucket, filename, object_name=None, prefix=None, log=void_fn):
    if not object_name:
        object_name = filename
    if prefix:
        object_name = prefix_object(prefix, object_name)

    status = 'STARTED'

    start = timestamp()
    log(get_log_entry('push_s3', status, start=start, filename=filename, bucket=bucket, object_name=object_name))
    errors = []

    try:
        s3 = boto3.client('s3')
        s3.upload_file(filename, bucket, object_name)
        status = 'SUCCESS'
    except NameError:
        status = 'ERROR'
        errors.append('boto3 library not found. (NameError)')
    except Exception as e:
        errors.append(f'Uploading the file failed. ({type(e).__name__})')
        status = 'ERROR'
    end = timestamp()

    log(get_log_entry('push_s3', status, start=start, end=end, filename=filename, bucket=bucket, object_name=object_name, errors=errors))
    return status == 'SUCCESS'


def push(log, **kwargs):
    to = kwargs.get('to')
    if to == 'url':
        keys = ('filename', 'url', 'method', 'data', 'headers', )
        return _push_http(**filter_dict(kwargs, keys), log=log)
    if to == 's3':
        prefix = kwargs.get('id') if kwargs.get('prefix') != False else None
        keys = ('bucket', 'object_name', 'filename', )
        return _push_s3(**filter_dict(kwargs, keys), prefix=prefix, log=log)
