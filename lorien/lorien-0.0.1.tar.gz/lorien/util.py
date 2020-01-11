"""
Utility functions
"""
import os
import time

from git import Repo


def get_tvm_commit() -> str:
    """Get the TVM repo commit in this environment.

    Returns
    -------
    commit: Optional[str]
        The commit hash, or None if TVM is invalid.
    """
    try:
        import tvm
        tvm_repo_path = os.path.join(tvm.__path__[0], '../../')
        repo = Repo(tvm_repo_path)
        return str(repo.active_branch._get_commit())
    except Exception:  # pylint: disable=broad-except
        pass
    return 'unknown'


def get_time_str() -> str:
    """Generate a string using the current time.

    Returns
    -------
    ret: str
        A string in <year><month><day>-<hour><min> format.
    """
    curr_time = time.gmtime()
    return '{y:04d}{M:02d}{d:02d}-{h:02d}{m:02d}'.format(y=curr_time.tm_year,
                                                         M=curr_time.tm_mon,
                                                         d=curr_time.tm_mday,
                                                         h=curr_time.tm_hour,
                                                         m=curr_time.tm_min)
