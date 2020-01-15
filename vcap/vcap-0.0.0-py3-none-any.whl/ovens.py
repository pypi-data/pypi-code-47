"""Defines ovens.

Ovens are classes that know how to do some kind of generic work in batches.
"""
import logging
import queue
from collections import namedtuple
from threading import Thread
from typing import List, Callable

_OvenRequest = namedtuple("ObjectDetectionRequest", [
    "output_queue",
    "input"
])
_OvenRequest.__doc__ = \
    """A request that is sent to an oven to do some work on an image, and
    push predictions into the output_queue

    output_queue: The queue for the oven to put the results in
    img_bgr: An OpenCV BGR image to run detection on
    """


class Oven:
    """This class simplifies receiving work from a multitude of sources and
    running that work in a batched predict function, then returning that
    work to the respective output queues."""

    MAX_BATCH_SIZE = 40

    def __init__(self, batch_fn: Callable[[List[object]], List[object]],
                 num_workers=1):
        """Initialize a new oven.
         that the oven will wait between running a batch regardless of batch
         size
        """
        self.batch_fn = batch_fn
        self._request_queue = queue.Queue()
        self.workers = [Thread(target=self._worker, name="OvenThread")
                        for _ in range(num_workers)]

        # The number of images currently in the work queue or being processed
        self._imgs_selected_for_processing = 0

        self._running = True

        for worker in self.workers:
            worker.start()

    @property
    def total_imgs_in_pipeline(self) -> int:
        return self._request_queue.qsize() + self._imgs_selected_for_processing

    def submit(self, input, output_queue=None):
        """Creates an OvenRequest for you and returns the output queue"""
        output_queue = output_queue if output_queue else queue.Queue()
        self._request_queue.put(_OvenRequest(
            output_queue=output_queue,
            input=input))
        return output_queue

    def _on_requests_ready(self, batch: List[_OvenRequest]):
        """Push images through the given prediction backend

        :param batch: A list of requests to work on
        """
        # Extract the images from the requests
        inputs = [req.input for req in batch]
        output_queues = [req.output_queue for req in batch]

        # Route the results to each request
        response_count = 0
        predictions = self.batch_fn(inputs)
        for response_count, output in enumerate(predictions, start=1):
            output_queues[response_count - 1].put(output)

        if response_count != len(inputs):
            logging.error(f"CRITICAL ERROR: Backend returned {response_count} "
                          f"responses. Expected {len(inputs)}")

    def _worker(self):
        self._running = True

        while self._running:
            # Get a new batch
            batch = self._get_next_batch()

            # If no batch was able to be retrieved, restart the loop
            if not len(batch):
                continue

            # Check to make sure the thread isn't trying to end
            if not self._running:
                break

            self._imgs_selected_for_processing += len(batch)
            self._on_requests_ready(batch)
            self._imgs_selected_for_processing -= len(batch)

        self._running = False

    def _get_next_batch(self):
        """A helper function to help make the main thread loop more readable
        :returns:A list, WHICH CAN BE EMPTY, or full of collected items"""
        batch = []
        while len(batch) < self.MAX_BATCH_SIZE:
            # Check if there's a new request
            try:
                # Try to get a new request. Have a timeout to check if closing
                new_request = self._request_queue.get(timeout=.1)
            except queue.Empty:
                # If the thread is being requested to close, exit early
                if not self._running:
                    return []
                continue

            batch.append(new_request)

            # If the queue is now empty, go ahead and run everything in it
            if self._request_queue.empty():
                break

        return batch

    def close(self):
        """Stop the oven gracefully."""
        self._running = False
        for worker in self.workers:
            worker.join()

    def clear(self):
        """Clear any pending operations in the request queue."""
        while not self._request_queue.empty():
            try:
                self._request_queue.get(False)
            except queue.Empty:
                continue
            self._request_queue.task_done()
