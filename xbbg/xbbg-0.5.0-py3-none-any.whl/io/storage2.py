import pandas as pd

import re
import inspect
import inflection

from functools import wraps
from collections import namedtuple

from xbbg.core import utils
from xbbg.io import files, logs

from infkit.core import config, valid

LOGGER = logs.get_logger(__file__.split('/')[-1], level='warning')

CachedFile = namedtuple('CachedFile', [
    # location to read the cached data
    'read_file',
    # location to save new data
    'write_file',
])


def with_cache(*dec_args, **dec_kwargs):
    """
    Wraps function to load cache data if available

    Default path will be: DefaultDataPath/Module(s)Name/FunctionName
    """
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            scope = func_path(func=func)
            exc_keys = kwargs.pop('exc_keys', [])
            if isinstance(exc_keys, str): exc_keys = [exc_keys]

            param = inspect.signature(func).parameters
            all_kw = {
                k: args[n] if n < len(args) else v.default
                for n, (k, v) in enumerate(param.items())
                if k not in ['kwargs'] + exc_keys
            }
            all_kw.update(kwargs)

            if t_1:
                prev_dt = valid.get_dt(offset=-1, **all_kw)
                if 'end_date' in all_kw:
                    all_kw['end_date'] = min(valid.fmt_dt(
                        all_kw['end_date'], fmt=all_kw.get('fmt', 'human')
                    ), prev_dt)

            use_incr = incr_calc and ('end_date' in all_kw)
            read_file, data_file = cached_data_file(
                data_path=config.data_path(module=scope, data_root=data_root),
                use_incr=use_incr, ext=ext, **all_kw
            )

            # Recalculate and override previous results
            if not kwargs.get('_recalc_', False):
                data = load_file(data_file=read_file)
                if data is not None:
                    if not (use_incr and require_update(data_file=data_file, **kwargs)):
                        return data
                    all_kw['_cache_data_'] = data
                    all_kw['_prev_end_'] = \
                        extract_info(field='end_date', data_file=data_file)

            data = func(**all_kw)

            lets_save = True
            if not_today and 'dt' in all_kw:
                # Compare with earliest open market
                if pd.Timestamp('today', tz='Australia/Sydney').date() <= \
                        pd.Timestamp(all_kw['dt']).date():
                    lets_save = False
            if lets_save: save_file(data=data, data_file=data_file)

            return data
        return wrapper

    # whether cached data is incremental
    incr_calc = dec_kwargs.get('incr_calc', False)
    # Trim date range to T - 1
    t_1 = dec_kwargs.get('t_1', False)
    # Whether to ignore data from today
    not_today = dec_kwargs.get('not_today', True)
    # Data root path
    data_root = dec_kwargs.get('data_root', None)
    # Data default format
    ext = dec_kwargs.get('ext', 'pkl')

    return decorator(dec_args[0]) if dec_args and callable(dec_args[0]) else decorator


def extract_info(field, data_file):
    """
    Extract info from data file with specified format

    Args:
        field: info to extract
        data_file: data file

    Returns:
        str: found string or empty string if not found
    """
    r = re.match(rf'.*{field}=(.*?)[, |.].*', data_file)
    return '' if r is None else r.group(1)


def require_update(data_file, **kwargs) -> bool:
    """
    Check current kwargs to see if

    Args:
        data_file: current cached data file

    Returns:
        bool
    """
    s_dt = extract_info(field='start_date', data_file=data_file)
    e_dt = extract_info(field='end_date', data_file=data_file)
    if not e_dt: return True
    if 'end_date' not in kwargs: return True

    prev_end = pd.Timestamp(valid.fmt_dt(dt=e_dt, **kwargs)).date()
    cur_end = pd.Timestamp(kwargs['end_date']).date()

    # ToReview: how to include start date into consideration
    # In prev step, if we look for file name with start_date
    # in it, the file was excluded in the file list
    if not s_dt: return prev_end < cur_end

    if 'start_date' not in kwargs: return True

    prev_start = pd.Timestamp(valid.fmt_dt(dt=s_dt, **kwargs)).date()
    cur_start = pd.Timestamp(kwargs['start_date']).date()

    return (prev_start > cur_start) or (prev_end < cur_end)


def cached_data_file(data_path, use_incr, **kwargs) -> CachedFile:
    """
    Cached file info

    Args:
        data_path: data path
        use_incr: use incremental data

    Returns:
        CachedFile
    """
    # Default extension as pickle to be safe
    ext = kwargs.pop('ext', 'pkl')
    file_kw = dict([
        clean_path(key=k, val=v, **kwargs)
        for k, v in kwargs.items()
        if (k not in ['log', 'refresh']) and (k[0] != '_') and (v is not None)
    ])

    if use_incr:
        # Rearrange orders of kwargs
        end_date = file_kw.pop('end_date')
        file_kw['end_date'] = end_date

    if file_kw: file_name = utils.to_str(file_kw)[1:-1].replace(', ', '/', 1)
    else: file_name = 'ovrd=None'
    data_file = f'{data_path}/{file_name}.{ext}'

    if use_incr:
        file_kw.pop('end_date')
        search = utils.to_str(file_kw)[1:-1].replace(', ', '/', 1)
        r = re.compile(rf'.*end_date=(.*)\.{ext}')
        all_f = sorted(filter(
            r.match, files.all_files(data_path, keyword=search, ext=ext)
        ), reverse=True)
        read_file = all_f[0] if all_f else ''
    else:
        read_file = data_file

    return CachedFile(read_file=read_file, write_file=data_file)


def clean_path(key, val, **kwargs) -> tuple:
    """
    Clean key / value pairs to generate path name

    Args:
        key: key
        val: value

    Returns:
        tuple of formatted key / value

    Examples:
        >>> clean_path(key='ticker', val='RDS/A US')
        ('ticker', 'RDS_A US')
        >>> clean_path(key='tickers', val='RDS/B US')
        ('tickers', 'RDS_B US')
        >>> clean_path(key='tickers', val=['SPY US', 'RDS/B US'])
        ('tickers', 'SPY US+RDS_B US')
        >>> clean_path(key='start_date', val=pd.Timestamp('20181231'))
        ('start_date', '2018-12-31')
        >>> clean_path(key='end_date', val='20181231')
        ('end_date', '20181231')
        >>> clean_path(key='dt', val='2019-01-02')
        ('dt', '2019-01-02')
        >>> clean_path(key='flds', val='px_last')
        ('flds', 'px_last')
    """
    if key == 'ticker':
        return key, val.replace('/', '_')

    if key == 'tickers':
        if hasattr(val, '__iter__') and (not isinstance(val, str)):
            return key, '+'.join([v.replace('/', '_') for v in val])
        else:
            return key, str(val).replace('/', '_')

    key_arr = key.lower().split('_')
    if ('date' in key_arr) or ('dt' in key_arr):
        return proper_date_str(key=key, val=val, **kwargs)

    return key, val


def proper_date_str(key, val, **kwargs) -> tuple:
    """
    Proper date string
    """
    key_arr = key.lower().split('_')
    if ('date' not in key_arr) and ('dt' not in key_arr):
        return key, val

    if hasattr(val, 'strftime'):
        return key, val.strftime('%Y-%m-%d')

    elif val == 'today':
        if 'ticker' in kwargs:
            return key, valid.get_dt(ticker=kwargs['ticker'])
        elif 'tickers' in kwargs:
            if isinstance(kwargs['tickers'], str):
                return key, valid.get_dt(ticker=kwargs['tickers'])
            else:
                return key, valid.get_dt(ticker=kwargs['tickers'][0])
        else:
            # If no other information is given, use latest timezone
            return key, valid.get_dt(ticker='SPY US Equity')

    elif key == 'dt':
        return key, pd.Timestamp(val).strftime('%Y-%m-%d')

    return key, str(val)


def func_path(func) -> str:
    """
    Proper function path
    """
    if not callable(func):
        LOGGER.warning(f'{str(func)} is not a function')
        return ''

    return '/'.join(map(
        inflection.camelize, utils.func_scope(func=func).split('.')[1:]
    ))


def load_file(data_file: str):
    """
    Load data
    """
    if data_file: LOGGER.debug(f'reading from {data_file} ...')
    if not data_file or not files.exists(data_file): return
    ext = data_file.split('.')[-1]

    load_methods = {
        'pkl': pd.read_pickle, 'parq': pd.read_parquet, 'csv': pd.read_csv
    }

    LOGGER.debug(f'loading data from {data_file}')
    if ext not in load_methods: return
    return load_methods[ext](data_file)


def save_file(data, data_file: str, **kwargs):
    """
    Save data
    """
    if not data_file: return
    ext = data_file.split('.')[-1]
    if ext == 'csv': kwargs['index'] = False

    save_methods = {
        'pkl': 'to_pickle', 'parq': 'to_parquet', 'csv': 'to_csv'
    }
    save_func = save_methods.get(ext, '___nothing___')
    if not hasattr(data, save_func): return

    LOGGER.debug(f'saving data to {data_file} ...')
    files.create_folder(data_file, is_file=True)
    getattr(data, save_func)(data_file, **kwargs)
