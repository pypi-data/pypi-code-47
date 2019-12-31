import logging
import os
import sys
import typing as tp

try:
    import pwd
    import grp
except ImportError:
    # Windows?
    class L(object):  # always return UID=GID=0
        def __getattr__(self, item):
            return lambda q: 0


    pwd = grp = L()

logger = logging.getLogger(__name__)

DEVNULL = '/dev/null'

__all__ = ['daemonize']


def daemonize(exit_via: tp.Callable = sys.exit,
              redirect_std_to_devnull: bool = True,
              uid: tp.Optional[int] = None,
              gid: tp.Optional[int] = None):
    """
    Make this process into a daemon.

    This entails:

    - umask 0
    - forks twice
    - be the child of init
    - becomes session leader
    - changes root directory to /
    - closes stdin, stdout, stderr
    - (option) redirects stdin, stdout, stderr to /dev/null

    Refer - "Advanced Programming in the UNIX Environment" 13.3

    :param exit_via: callable used to terminate process
    :param redirect_std_to_devnull: whether to redirect stdin, stdout and
        stderr to /dev/null
    :param uid: User to set (via seteuid). Default - this won't be done. You
        can pass either user name as string or UID.
    :param gid: Same as UID, but for groups. These will be resolved too.
    :raises KeyError: uid/gid was passed as string, but getpwnam() failed
    """

    _double_fork(exit_via=exit_via)
    _close_descriptors()

    if redirect_std_to_devnull:
        _redirect_descriptors_to_null()

    _parse_ug(uid, pwd, 'pw_uid', os.seteuid)
    _parse_ug(gid, grp, 'gr_gid', os.setegid)


def _parse_ug(no, module, field_name, osfun):
    if no is not None:
        if isinstance(no, str):
            no = getattr(module.getpwnam(no), field_name)
        osfun(no)


def _redirect_descriptors_to_null():
    sys.stdin = open(DEVNULL, 'rb')
    sys.stdout = open(DEVNULL, 'wb')
    sys.stderr = open(DEVNULL, 'wb')


def _close_descriptors():
    for d in [sys.stdin, sys.stdout, sys.stderr]:
        d.close()


def _double_fork(exit_via):
    os.umask(0)

    if os.fork() > 0:
        exit_via()  # parent exits

    os.setsid()

    if os.fork() > 0:
        exit_via()  # parent exits
    os.chdir('/')
