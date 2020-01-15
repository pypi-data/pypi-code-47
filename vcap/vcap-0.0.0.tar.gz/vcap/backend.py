import abc
from queue import Queue
from typing import List, Dict, Any

import numpy as np

from vcap.ovens import Oven
from vcap.node_description import DETECTION_NODE_TYPE
from vcap.options import OPTION_TYPE
from vcap.stream_state import BaseStreamState


class BaseBackend(abc.ABC):
    """An object that provides low-level prediction functionality for batches
    of frames.
    """

    def __init__(self):
        self.oven = Oven(self.batch_predict)

    def send_to_batch(self, input: Any) -> Queue:
        """Sends the given object to the batch_predict method for processing.
        This call does not block. Instead, the result will be provided on the
        returned queue. The batch_predict method must be overridden on the
        backend this method is being called on.

        :param input: The input object to send to batch_predict
        :return: A queue where results will be stored
        """
        return self.oven.submit(input)

    @abc.abstractmethod
    def process_frame(
            self,
            frame: np.ndarray,
            detection_node: DETECTION_NODE_TYPE,
            options: Dict[str, OPTION_TYPE],
            state: BaseStreamState) -> DETECTION_NODE_TYPE:
        """A method that does the preprocessing, inference, and postprocessing
        work for a frame. It has the ability to call self.send_to_batch(frame)
        to send work for batching (eventually run in batch_predict)."""

    def batch_predict(self, inputs: List[Any]) -> List[Any]:
        """Runs prediction on a batch of frames (or objects). This method must
        be overridden for capsules that use send_to_batch.

        :param inputs: A list of objects. Whatever the model requires for
            each frame.
        """
        raise NotImplementedError(
            "Attempt to do batch prediction on a Backend that does not have "
            "the batch_predict method defined. Did you call send_to_batch on "
            "a backend that does not override batch_predict?")

    @abc.abstractmethod
    def close(self):
        """De-initializes the backend."""
        pass
