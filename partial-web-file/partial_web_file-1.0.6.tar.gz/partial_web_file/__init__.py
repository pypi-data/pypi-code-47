import argparse
import os

import partial_web_file.file_util
import partial_web_file.zip_util


def get_partial_web_file(url, start_position, length):
    return partial_web_file.file_util.get_partial_web_file(url, start_position, length)


def get_file_content_from_web_zip(zip_url, path_to_file_in_zip):
    return partial_web_file.zip_util.get_file_content_from_web_zip(zip_url, path_to_file_in_zip)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url to zip')
    parser.add_argument('filename', help='file in zip to download to current folder')
    return parser.parse_args()


def main():
    args = _parse_args()

    url = args.url
    filename = args.filename
    save_to = os.path.basename(filename)

    print('Saving %s:%s to %s...' % (url, filename, save_to))
    content = get_file_content_from_web_zip(url, filename)
    with open(save_to, 'wb') as f:
        f.write(content)
    print('Done.')


if __name__ == '__main__':
    main()
