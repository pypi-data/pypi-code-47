from abc import abstractmethod, ABC
from collections import deque
from typing import Tuple, Dict
from uuid import uuid4


class PolicyPool(ABC):

    def __init__(self, lock, max_q_size: int, max_workers: int):
        """
        Initializes a policy pool
        :param lock: an instantiation of a locking mechanism, corresponds to whether we are using threads or processes
        :param max_q_size: the maximum size of the worker backlog queue
        :param max_workers: the maximum number of active concurrent workers
        """
        self._worker_queue = deque(maxlen=max_q_size)
        self._rotation_lock = lock
        self._total_workers: int = 0
        self._active_workers: dict = {}
        self.__max_workers: int = max_workers
        self.__max_q_size: int = max_q_size

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        while self._total_workers != 0:
            pass
        self.close()
        return False

    def __del__(self):
        self.close()

    def map(self, target, *iterable: iter):
        """
        Maps a target function across the iterable args using the specified policy pool
        :param target: the function that we want to run and map across
        :param iterable: contains the arguments for the corresponding target
        :return: None
        """
        for args in zip(*iterable):
            self.submit(target=target, args=args)

    def _get_unique_name(self, name: str, prefix: str):
        """
        Given a name and prefix for the worker type generate a unique name
        :param name: the provided name for the worker
        :param prefix: corresponds to the worker type
        :return: a unique identifier for the worker
        :rtype: str
        """
        if name is None:
            return prefix + "-" + PolicyPool.__generate_random_string()
        elif name in self._active_workers.keys():
            return name + PolicyPool.__generate_random_string()
        else:
            return name

    def _execute(self, name, worker):
        """
        Attempts to start the provided worker if size of active workers in under max workers
        if we are at max workers we look to append to worker queue
        if worker queue is full we rotate in the worker based on the corresponding policy
        :param name: identifier that corresponds to the provided worker
        :param worker: instance of the worker that we want to execute
        :return: None
        """
        with self._rotation_lock:
            if len(self._active_workers) < self.__max_workers:
                self._total_workers += 1
                self._active_workers[name] = worker
                self._active_workers[name].start()
            else:
                if len(self._worker_queue) < self.__max_q_size:
                    self._total_workers += 1
                    self._worker_queue.append(worker)
                else:
                    self._rotate_workers(worker)

    @staticmethod
    def __generate_random_string():
        """
        Helper function for generating a random string
        :return: random string
        :rtype: str
        """
        return uuid4().hex[:6].upper()

    @abstractmethod
    def close(self):
        """
        Closes a policy pool to prevent leaks, if possible this will terminate active workers
        """
        raise NotImplementedError

    @abstractmethod
    def _rotate_workers(self, worker):
        """
        Rotates a worker from the worker queue to the active workers according to the corresponding policy
        :param worker: the worker the rotate into being active
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def submit(self, target=None, name: str = None, args: Tuple = (), kwargs: Dict = None, *, daemon: bool = None):
        """
        Submits for background execution of a supplied target
        :param target: the function to execute in the background
        :param name: the name for the worker that will execute the target
        :param args: the standard arguments to pass to the target for execution
        :param kwargs: the keyword arguments to pass to the target for execution
        :param daemon: indicates if the worker should be a daemon
        :return: None
        """
        raise NotImplementedError
