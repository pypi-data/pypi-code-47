import zipfile

from partial_web_file.remote_stream import RemoteStream


def get_file_content_from_web_zip(zip_url, path_to_file_in_zip):
    stream = RemoteStream(zip_url)
    with zipfile.ZipFile(stream, 'r') as zf:
        return zf.read(path_to_file_in_zip)
