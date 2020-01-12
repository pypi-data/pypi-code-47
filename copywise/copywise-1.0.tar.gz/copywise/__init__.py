import shutil
import os
import glob

from copywise import parallel
from copywise import morsels


def assert_is_iter(ext):
    """ Make sure an object is an iterable. """
    if not parallel.is_iter(ext):
        ext = [ext]
    return ext


def find_files(path, include=None, exclude=None):
    """ Find files from selected extensions. """
    # If no extension is selected, use the wild card.
    if include is None:
        include = '*'
    # Make sure it is an iterable,
    include = assert_is_iter(include)
    # Find files and flatten.
    files = [glob.glob(f'{path}/**/*.{ext}', recursive=True) for ext in include]
    # The return of deep_flatten is an generator.
    files = list(morsels.deep_flatten(files))
    # Exclude files that the user does not want.
    if exclude is not None:
        # Make sure it is an iterable,
        exclude = assert_is_iter(exclude)
        # The slice is used to remove the dot from the beginning of the extension.
        files = [file for file in files if not os.path.splitext(file)[-1][1:] in exclude]
    return files


def copy(src, dst):
    """ Simple copy creating necessary folders. """
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def copy_ext(src, dst, include=None, exclude=None):
    """
    Copy all files from certain extensions.

    Args:
        src: Source folder.
        dst: Destination folder.
        include: Extensions to copy. Do not include the point. If None copy all files.
        exclude: Extensions to not copy. Only relevant when include = None.
    """
    # Find files from the specified extensions.
    files = find_files(src, include)
    # Transform all file paths in relative.
    rel = [os.path.relpath(file, src) for file in files]
    # Concatenate the relative path to the destination folder.
    dst = [f'{dst}\\{rel}' for rel in rel]
    # Run in a thread pool.
    parallel.run(copy, list(zip(files, dst)), thread=True)


if __name__ == '__main__':
    try:
        shutil.rmtree('Copied')
    except FileNotFoundError:
        pass
    copy_ext(src='Mock Files', dst='Copied', include='pdf', exclude=None)
