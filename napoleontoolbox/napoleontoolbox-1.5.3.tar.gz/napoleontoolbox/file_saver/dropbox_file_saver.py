"""Upload the contents of your Downloads folder to Dropbox.
This is an example app for API v2.
"""

from __future__ import print_function

import contextlib
import datetime
import os
import time
import pandas as pd
import numpy as np
import dropbox

@contextlib.contextmanager
def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

class NaPoleonDropboxConnector(object):
    def __init__(self, drop_token):
        self.drop_token = drop_token
        self.dbx = dropbox.Dropbox(self.drop_token)

    def local_supervision_npy_save_and_upload(self, data=None, rebal = None, local_root_directory='', user='', supervision_npy_file_suffix=''):
        supervision_file_name = user + '_' + str(rebal) + supervision_npy_file_suffix
        local_supervision_npy_path = local_root_directory + supervision_file_name
        np.save(local_supervision_npy_path, data)
        self.upload(fullname=local_supervision_npy_path, folder='', subfolder='', name = supervision_file_name, overwrite=False)

    def local_overwrite_and_load_pickle(self, folder='', subfolder='', returns_pkl_file_name='', local_root_directory = ''):
        res = self.dbx.download(folder = folder,subfolder= subfolder, name = returns_pkl_file_name)
        local_returns_pkl_path = local_root_directory + returns_pkl_file_name
        print('overwriting local file '+local_returns_pkl_path+' with dropbox file')
        f = open(local_returns_pkl_path, 'wb')
        f.write(res)
        f.close()
        print('loading overwritting local returns pickle file reading ' + local_returns_pkl_path)
        df = pd.read_pickle(local_returns_pkl_path)
        return df

    def list_folder(self, folder, subfolder):
        """List a folder.
        Return a dict mapping unicode filenames to
        FileMetadata|FolderMetadata entries.
        """
        path = '/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'))
        while '//' in path:
            path = path.replace('//', '/')
        path = path.rstrip('/')
        try:
            with stopwatch('list_folder'):
                res = self.dbx.files_list_folder(path)
        except dropbox.exceptions.ApiError as err:
            print('Folder listing failed for', path, '-- assumed empty:', err)
            return {}
        else:
            rv = {}
            for entry in res.entries:
                rv[entry.name] = entry
            return rv

    def upload(self, fullname, folder, subfolder, name, overwrite=False):
        """Upload a file.
        Return the request response, or None in case of error.
        """
        path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)
        while '//' in path:
            path = path.replace('//', '/')
        mode = (dropbox.files.WriteMode.overwrite
                if overwrite
                else dropbox.files.WriteMode.add)
        mtime = os.path.getmtime(fullname)
        with open(fullname, 'rb') as f:
            data = f.read()
        with stopwatch('upload %d bytes' % len(data)):
            try:
                res = self.dbx.files_upload(
                    data, path, mode,
                    client_modified=datetime.datetime(*time.gmtime(mtime)[:6]),
                    mute=True)
            except dropbox.exceptions.ApiError as err:
                print('*** API error', err)
                return None
        print('uploaded as', res.name.encode('utf8'))
        return res

    def download(self, folder, subfolder, name):
        """Download a file.
        Return the bytes of the file, or None if it doesn't exist.
        """
        path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)
        while '//' in path:
            path = path.replace('//', '/')
        with stopwatch('download'):
            try:
                md, res = self.dbx.files_download(path)
            except dropbox.exceptions.HttpError as err:
                print('*** HTTP error', err)
                return None
        data = res.content
        print(len(data), 'bytes; md:', md)
        return data


