# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from abc import ABC
import os
from pathlib import Path
import time


class Simulator(ABC):
    """Defines methods for interacting with run-time simulator instances.

    Simulators are processes that run on a compute target and listen on a process specific port.
    Instances of this class hold the information necessary to connect to a simulator during execution of
    a reinforcement learning experiment.
    This class is typically referenced and used during experiment execution and not during control plane operations
    in the SDK.

    :param simulator_id: The system assigned id for an instance of a simulator.
    :type simulator_id: str
    :param ip_address: The IP address where the simulator instance is running.
    :type ip_address: str
    :param port: The port where the simulator instance is listening for connections.
    :type port: str
    """

    # The file extension used in simulator match making
    FILE_EXTENSION = ".sim"

    def __init__(self, simulator_id, ip_address, port):
        """Initializes a simulator reference with its id, IP address and port.

        :param simulator_id: The system assigned id for an instance of a simulator.
        :type simulator_id: str
        :param ip_address: The IP address where the simulator instance is running.
        :type ip_address: str
        :param port: The port where the simulator instance is listening for connections.
        :type port: str
        """
        self.id = simulator_id
        self.ip_address = ip_address
        self.port = port

    def __repr__(self):
        return "<Simulator id:%s ip_address:%s port:%s>" % (self.id, self.ip_address, self.port)

    @staticmethod
    def get_simulators(min_count=1, timeout_seconds=None, raise_on_timeout=True):
        """Get the list of simulators that are running for the currently executing run.

        By specifying `min_count`, the method will not return until `min_count` number of simulators are running
        or until `timeout_seconds` has elapsed.

        :param min_count: When this parameter is specified, the method will not return until `min_count`
        simulators have started running.
        :type min_count: int
        :param timeout_seconds: If `min_count` is set, the number of seconds to wait until `min_count` simulators
        are running. After `timeout_seconds` has expired, the set of running simulators will be returned unless
        `raise_on_timeout` is set.
        :param raise_on_timeout: If set, will raise an exception if `timeout_seconds` has elapsed before `min_count`
        simulators have started.
        :type timeout_seconds: int
        :return: The list of currently running Simulators.
        :rtype: list
        """

        start = time.time()
        while True:
            sim_count = Simulator.get_running_simulator_count()
            if timeout_seconds and time.time() - start > timeout_seconds:
                if raise_on_timeout:
                    raise Exception("Timeout has occurred waiting for {} simulators to start. "
                                    "A total of {} started before the timeout occurred.".format(min_count, sim_count))
                break
            if min_count is None or sim_count >= min_count:
                break
            else:
                print("{} simulators have started so far; waiting for {} simulators total."
                      .format(sim_count, min_count))
                time.sleep(10)

        sims = []
        for item in Simulator._get_simulator_files():
            sim = Simulator._create_from_file(item)
            if sim:
                sims.append(sim)

        return sims

    @staticmethod
    def get_simulator_by_id(simulator_id, block=True, timeout_seconds=None):
        """Get a simulator given an id.

        By default, the method will block until the simulator is running.

        :param simulator_id: The id of the simulator.
        :type simulator_id: str
        :param block: When set the method will block until the simulator is running or `timeout_seconds' has elapsed.
        :param timeout_seconds: If `block' is set to True, the number of seconds to wait before failing.
        :type timeout_seconds: int
        :return: A simulator with the given id. If the simulator doesn't start within `timeout_seconds`,
        None is returned.
        :rtype: azureml.contrib.train.rl._rl_simulator.Simulator
        """
        path = Simulator._get_file_share_path()
        file_path = path.joinpath(Path(simulator_id + Simulator.FILE_EXTENSION))
        start = time.time()
        while block and not file_path.exists():
            print("Waiting for simulator {} to start.".format(simulator_id))
            if timeout_seconds and time.time() - start > timeout_seconds:
                break
            time.sleep(10)

        if file_path.exists():
            return Simulator._create_from_file(file_path)

    @staticmethod
    def get_running_simulator_count():
        """Get the count of currently running simulators.

        :return: The count of current running simulators.
        :rtype: int
        """

        return len([f for f in Simulator._get_simulator_files()])

    @staticmethod
    def get_simulator_count():
        """Get the number of simulators requested to run.

        :return: The number of simulators.
        :rtype: int
        """
        count = os.getenv("AZUREML_NUMBER_OF_SIMULATORS")
        if not count:
            raise Exception("The methods in the Simulator class can only be used from AmlCompute nodes.")
        elif not count.isdigit():
            raise Exception("AZUREML_NUMBER_OF_SIMULATORS should be an integer.")

        return int(count)

    @staticmethod
    def _get_file_share_path():
        path = os.getenv("AZUREML_SIMULATOR_CONTROL_PATH")
        if not path:
            raise Exception("The methods in the Simulator class can only be used from AmlCompute nodes.")

        path = os.path.expandvars(path)
        return Path(path)

    @staticmethod
    def _get_simulator_files():
        path = Simulator._get_file_share_path()
        if not path.exists():
            print("Simulator control path '{}' does not exist.".format(path))
            return

        for item in path.iterdir():
            if item.is_file() and item.suffix == Simulator.FILE_EXTENSION:
                yield item

    @staticmethod
    def _create_from_file(file):
        sim_id = file.stem
        with file.open() as f:
            address = f.readline()
            if address:
                ip_port = address.split(":")
                return Simulator(sim_id, ip_port[0], ip_port[1])
            else:
                raise Exception("Invalid sim file for simulator id: {}. IP address and port not present."
                                .format(sim_id))
