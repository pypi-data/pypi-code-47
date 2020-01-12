from shutil import unpack_archive
from requests import get

try:
    import boto3
except ImportError:
    pass

from ._utils import timestamp, get_log_entry, filter_dict, void_fn

def _write_to_file(response, filename):
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1<<20): # 1 MB
            if chunk: f.write(chunk)

def _pull_http(url, headers=None, filename=None, extract=False, log=void_fn):
    if not filename:
        filename = url.split('/')[-1]

    status = 'STARTED'
    status_code = None

    start = timestamp()
    log(get_log_entry('pull_http', status, url=url, filename=filename, start=start))
    errors = []

    try:
        with get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            status_code = r.status_code
            ok = r.ok
            _write_to_file(r, filename)

        if extract:
            unpack_archive(filename)
        status = 'SUCCESS'
    except Exception as e:
        status = 'ERROR'
        errors.append(f'Downloading or unpacking the file failed. ({type(e).__name__})')

    end = timestamp()

    log(get_log_entry('pull_http', status, url=url, filename=filename, status_code=status_code, extracted=extract, start=start, end=end, errors=errors))
    return status == 'SUCCESS'

def _pull_s3(bucket, object_name, filename=None, log=void_fn):
    if not filename:
        filename = object_name

    status = 'STARTED'

    start = timestamp()
    log(get_log_entry('pull_s3', status, bucket=bucket, object_name=object_name, filename=filename, start=start))
    errors = []

    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket, object_name, filename)
        status = 'SUCCESS'
    except NameError:
        status = 'ERROR'
        errors.append('boto3 library not found. (NameError)')
    except Exception as e:
        status = 'ERROR'
        errors.append(f'Downloading the file from S3 failed. ({type(e).__name__})')
    end = timestamp()

    log(get_log_entry('pull_s3', status, bucket=bucket, object_name=object_name, filename=filename, start=start, end=end, errors=errors))
    return status == 'SUCCESS'

def pull(log, **kwargs):
    from_ = kwargs.get('from')

    if from_ == 'url':
        keys = ('url', 'headers', 'filename', 'extract')
        return _pull_http(**filter_dict(kwargs, keys), log=log)
    if from_ == 's3':
        keys = ('bucket', 'object_name', 'filename')
        return _pull_s3(**filter_dict(kwargs, keys), log=log)
