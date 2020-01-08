from pathlib import Path


def get_all_files_in_directory(directory):
    '''
    Function to pull files in a directory
    :param directory: path to the directory
    :return: list of files with whole path
    '''
    dirpath = Path(directory)
    assert(dirpath.is_dir())
    file_list = []
    for x in dirpath.iterdir():
        print(x)
        if x.is_file():
            file_list.append(x)
        elif x.is_dir():
            file_list.extend(get_all_files_in_directory(x))

    return file_list
