import partial_web_file.file_util
import partial_web_file.zip_util


def get_partial_web_file(url, start_position, length):
    return partial_web_file.file_util.get_partial_web_file(url, start_position, length)


def get_file_content_from_web_zip(zip_url, path_to_file_in_zip):
    return partial_web_file.zip_util.get_file_content_from_web_zip(zip_url, path_to_file_in_zip)
