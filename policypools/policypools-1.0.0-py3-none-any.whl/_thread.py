from abc import ABC
from threading import Lock, Thread

from policypools.base import PolicyPool

__all__ = ['DiscardNewestThreadPool', 'DiscardOldestThreadPool', 'DiscardThisThreadPool']


class PolicyThreadPool(PolicyPool, ABC):

    def __init__(self, max_q_size: int, max_workers: int):
        super().__init__(lock=Lock(), max_q_size=max_q_size, max_workers=max_workers)

    def submit(self, target=None, name: str = None, args: tuple = (), kwargs: dict = None, *, daemon: bool = None):
        name = self._get_unique_name(name, prefix="Thread")  # Setting name to be unique since used as key for mapping

        def __wrapped_target(*args, **kwargs):
            """
            The wrapped target is how we look to replace a finished worker with a worker in the worker queue
            :return: None
            """
            target(*args, **kwargs)
            with self._rotation_lock:
                try:
                    worker = self._worker_queue.popleft()
                    self._active_workers[worker.getName()] = worker
                    self._active_workers[worker.getName()].start()
                except IndexError:
                    pass
                finally:
                    del self._active_workers[name]
                    self._total_workers -= 1

        worker = Thread(target=__wrapped_target, args=args, kwargs={} if kwargs is None else kwargs)
        worker.setName(name)
        worker.daemon = daemon if daemon is not None else worker.daemon
        self._execute(name, worker)

    submit.__doc__ = PolicyPool.submit.__doc__

    def close(self):
        with self._rotation_lock:
            self._worker_queue.clear()

    close.__doc__ = PolicyPool.close.__doc__


class DiscardOldestThreadPool(PolicyThreadPool):

    def _rotate_workers(self, thread: Thread):
        self._worker_queue.popleft()
        self._worker_queue.append(thread)

    _rotate_workers.__doc__ = PolicyPool._rotate_workers.__doc__


class DiscardNewestThreadPool(PolicyThreadPool):

    def _rotate_workers(self, thread: Thread):
        self._worker_queue.pop()
        self._worker_queue.append(thread)

    _rotate_workers.__doc__ = PolicyPool._rotate_workers.__doc__


class DiscardThisThreadPool(PolicyThreadPool):

    def _rotate_workers(self, thread: Thread):
        pass

    _rotate_workers.__doc__ = PolicyPool._rotate_workers.__doc__
