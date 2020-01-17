"""
This module provides functionality to work with files and folders.
"""
import math
import os
import fnmatch
import re


def create_dir_if_doesnt_exist(folderpath):
    """
    Creates a folder if it doesn't exist.

    :param folderpath:
    :return: True if folder was created, else False

    """
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        return True
    return False


def delete_file(filepath):
    """
    Deletes the specified file if the file exists.

    :param filepath: Path of the file to be deleted
    :return: True if the file was deleted, else False

    """
    if os.path.isfile(filepath):
        os.remove(filepath)
        return True
    else:
        print("Error: %s file not found" % filepath)
        return False


def delete_dir(dirpath):
    """
    Deletes the specified directory if it exists.

    :param dirpath: Path to the directory
    :return: True if the directory was deleted, else False

    """
    if os.path.isdir(dirpath):
        os.rmdir(dirpath)
        return True
    else:
        print("Error: %s directory not found" % dirpath)
        return False


def count_files_in_dir(dirpath):
    """
    Counts the number of files contained in the specified
    directory.

    :param dirpath: Path to the directory
    :return: Number of files

    """
    return len(
        [
            name
            for name in os.listdir(dirpath)
            if os.path.isfile(os.path.join(dirpath, name))
        ]
    )


def gen_find_files_wildcard(filepat, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern.

    :param filepat: The pattern to find
    :param top: Top level directory to find in
    :return: Generator of found filepaths

    Example
        filenames = gen_find_files_wildcard("*.py", ".")

    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_open_files(filepaths):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    :param filenames: List of filepaths to open
    :return: Generator of opened files

    Example:
        files = gen_opener(filenames)
    """

    for filepath in filepaths:
        f = open(filepath, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Chain iterators together into a single sequence.
    :param iterators: Iterators to iterate over sequentially
    :return: Generator that iterates over all given iterators.

    Example:
        lines = gen_open_files(files)
    """
    for it in iterators:
        yield from it


def gen_write_file(out_filepath, generator_source):
    """
    Writes generator output to a file.
    :param out_filepath: File to write
    :param generator_source: Generator to consume from
    :return: None
    """
    with open(out_filepath, 'w') as f:
        for item in generator_source:
            f.write(str(item))


def lines_from_dir(filepat, dirname):
    """
    Creates a generator for all lines of all files matching a pattern
    in a given directory and its subdirectories
    :param filepat:
    :param dirname:
    :return:
    """
    filenames = gen_find_files_wildcard(filepat, dirname)
    files = gen_open_files(filenames)
    lines = gen_concatenate(files)
    return lines


def concatenate_files(top, pattern, out_file):
    """
    Writes files found by pattern to a single concatenated file
    :param top: Directory to search files in
    :param pattern: Pattern to find files by
    :return: True if file is written
    """
    lines = lines_from_dir(pattern, top)
    gen_write_file(out_file, lines)
    return os.path.isfile(out_file)



def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    :param regex: The pattern to find
    :param lines: Lines to be matched
    :return: Lines with the matching pattern
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


def convert_size_bytes_to_human_readable_format(size_bytes):
    """
    Converts a size in bytes to a human readable format.

    :param size_bytes: The size in bytes
    :return: Bytes converted to readable format
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"
