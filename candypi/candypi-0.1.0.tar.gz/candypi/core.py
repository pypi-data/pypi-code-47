# -*- coding: utf-8 -*-


from pathlib import Path


def check_directory(dir_path: str):
    """create git instance
    
    Args:
        dir_path (str): fullpath of git root directory
    
    Raises:
        FileExistsError: dir_path does not exist
        FileExistsError: dir_path does not have .git directory
    
    Returns:
        string: directory path
    """

    p = Path(dir_path)

    # exsist check
    if p.exists():
        pass
    else:
        raise FileExistsError('the directory does not exist.')

    # .git directory check
    git_p = p / '.git'
    if git_p.exists():
        pass
    else:
        raise FileExistsError('the directory does not have .git directory')

    return dir_path
