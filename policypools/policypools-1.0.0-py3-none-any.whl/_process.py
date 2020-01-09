from abc import ABC
from multiprocessing import Lock, Process, Queue
from threading import Thread

from policypools.base import PolicyPool

__all__ = ['DiscardNewestProcessPool', 'DiscardOldestProcessPool', 'DiscardThisProcessPool']


class PolicyProcessPool(PolicyPool, ABC, metaclass=PolicyPool.__class__):

    def __init__(self, max_q_size: int, max_workers: int):
        super().__init__(lock=Lock(), max_q_size=max_q_size, max_workers=max_workers)
        self.__completed_workers_queue = Queue()
        self.__replace_completed_workers_thread = Thread(target=self.__replace_completed_workers)
        self.__replace_completed_workers_thread.start()

    def submit(self, target=None, name: str = None, args: tuple = (), kwargs: dict = None, *, daemon: bool = None):
        name = self._get_unique_name(name, prefix="Process")  # Setting name to be unique since used as key for mapping

        def __wrapped_target(*args, **kwargs):
            """
            The wrapped target is how we look to replace a finished worker with a worker in the worker queue
            :return: None
            """
            target(*args, **kwargs)
            self.__completed_workers_queue.put(name)

        worker = Process(target=__wrapped_target, args=args, kwargs={} if kwargs is None else kwargs)
        worker.name = name
        worker.daemon = daemon if daemon is not None else worker.daemon
        self._execute(name, worker)

    submit.__doc__ = PolicyPool.submit.__doc__

    def close(self):
        # Acquiring this lock prevents any race conditions of a process that will attempt to rotate itself out
        with self._rotation_lock:
            self.__completed_workers_queue.put(None)  # Kills the replace_completed_workers_thread
            for worker in self._active_workers.values():
                worker.terminate()
            self._worker_queue.clear()
        self.__replace_completed_workers_thread.join()

    def __replace_completed_workers(self):
        while True:
            name = self.__completed_workers_queue.get()
            if name is None:  # None should only be present if we want to stop this loop
                while not self.__completed_workers_queue.empty():
                    del self._active_workers[self.__completed_workers_queue.get()]
                break
            with self._rotation_lock:
                try:
                    worker = self._worker_queue.popleft()
                    self._active_workers[worker.name] = worker
                    self._active_workers[worker.name].start()
                except IndexError:
                    continue
                finally:
                    del self._active_workers[name]
                    self._total_workers -= 1


class DiscardNewestProcessPool(PolicyProcessPool):

    def _rotate_workers(self, process: Process):
        self._worker_queue.pop()
        self._worker_queue.append(process)

    _rotate_workers.__doc__ = PolicyPool._rotate_workers.__doc__


class DiscardOldestProcessPool(PolicyProcessPool):

    def _rotate_workers(self, process: Process):
        self._worker_queue.popleft()
        self._worker_queue.append(process)

    _rotate_workers.__doc__ = PolicyPool._rotate_workers.__doc__


class DiscardThisProcessPool(PolicyProcessPool):

    def _rotate_workers(self, process: Process):
        pass

    _rotate_workers.__doc__ = PolicyPool._rotate_workers.__doc__
