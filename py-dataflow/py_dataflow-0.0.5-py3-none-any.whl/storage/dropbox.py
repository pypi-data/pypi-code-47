# -*- coding: utf-8 -*-
"""Upload the contents of your Downloads folder to Dropbox.

This is an example app for API v2.
"""

from __future__ import print_function
from datetime import datetime
import dropbox
import argparse
import os, glob
import fnmatch
import time

app_dropbox = 'Aplicativos/%s' % os.environ.get('APPLICATION_NAME')
now = datetime.now()
url_dropbox = 'https://www.dropbox.com/home/%s' % app_dropbox
local = '%s/%s/%s/' % (now.year, now.month, now.day)
folder_dropbox = '/Downloads/%s' % local

# OAuth2 access token.  TODO: login etc.
parser = argparse.ArgumentParser(description='Sync ~/Downloads to Dropbox')
parser.add_argument('folder', nargs='?', default='Downloads/%s' %
                    local, help='Folder name in your Dropbox')
parser.add_argument('--yes', '-y', action='store_true',
                    help='Answer yes to all questions')
parser.add_argument('--no', '-n', action='store_true',
                    help='Answer no to all questions')
parser.add_argument('--default', '-d', action='store_true',
                    help='Take default answer on all questions')


def remove_files_path(type_file='*.xls'):
    # import ipdb; ipdb.set_trace()
    for file in get_all_files(type_file):
        os.remove(file[1])

def get_all_files(pattern='*.xls', path=None):
    # import ipdb; ipdb.set_trace()
    datafiles = []
    path = path or os.environ.get('DIR_LOCAL_DATA') #settings.DIR_LOCAL
    # path = path or '/data'
    for root,dirs,files in os.walk(path):
        for file in fnmatch.filter(files, pattern):
            pathname = os.path.join(root, file)
            filesize = os.stat(pathname).st_size
            datafiles.append([file, pathname, filesize])
    if len(datafiles) > 0:
        return datafiles
    else:
        return []

def get_preview_dropbox(path):
    file_name = path.split('/')[-1]
    preview = path.replace('/' + file_name, '?preview=')
    return preview + file_name

def download_dropbox(path):
    """Download a file.
    Return the bytes of the file, or None if it doesn't exist.
    """
    # import ipdb
    dbx = dropbox.Dropbox(os.environ.get('DROPBOX_ACCESS_TOKEN'))

    # path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)
    # while '//' in path:
    #   path = path.replace('//', '/')
    # with stopwatch('download'):
    try:
        md, res = dbx.files_download(path)
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        # return None
    # import ipdb; ipdb.set_trace()
    data = res.content
    # data = res.readlines()
    print(len(data), 'bytes; md:', md)
    return data

def send_dropbox(file=None, folder_dropbox=None):
    """
    send all files folder upload or file to dropbox
    Parse command line, then iterate over files and directories under
    rootdir and upload all files.  Skips some temporary files and
    directories, and avoids duplicate uploads by comparing size and
    mtime with the server.
    """
    dbx = dropbox.Dropbox(os.environ.get('DROPBOX_ACCESS_TOKEN'))
    if file:
        # folder_dropbox = '/Downloads/%s' %local
        resp = upload_file(dbx, file, folder_dropbox)
        return resp

def upload_file(dbx, _file, folder_dropbox, overwrite=True):
    """Upload a file.
    Return the request response, or None in case of error.
    """
    # import ipdb; ipdb.set_trace()
    mode = (dropbox.files.WriteMode.overwrite
            if overwrite
            else dropbox.files.WriteMode.add)

    data = _file.read()
    # with stopwatch('upload %d bytes' % len(data)):
    try:
        # mtime = os.path.getmtime(_file.path)
        mtime = 100
        folder = folder_dropbox + _file.name
        res = dbx.files_upload(data, folder, mode,
                               client_modified=datetime(
                                   *time.gmtime(mtime)[:6]),
                               mute=True)
    except dropbox.exceptions.ApiError as err:
        print('*** API error', err)
        return None
    print('uploaded as', res.name.encode('utf8'))
    return res