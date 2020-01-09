from policypools.base import PolicyPool
from policypools._process import DiscardNewestProcessPool, DiscardOldestProcessPool, DiscardThisProcessPool
from policypools._thread import DiscardNewestThreadPool, DiscardOldestThreadPool, DiscardThisThreadPool

__all__ = ['Policies', 'PolicyPool', 'PolicyPoolFactory']


class Policies:
    """
    Class that holds all of the possible policies for the pools
    """

    discard_newest = "DiscardNewest"
    discard_oldest = "DiscardOldest"
    discard_this = "DiscardThis"


class PolicyPoolFactory:
    """
    Factory class for providing different policy pools
    """

    __process_policy_mapping = {Policies.discard_oldest: DiscardOldestProcessPool,
                                Policies.discard_newest: DiscardNewestProcessPool,
                                Policies.discard_this: DiscardThisProcessPool}

    __thread_policy_mapping = {Policies.discard_oldest: DiscardOldestThreadPool,
                               Policies.discard_newest: DiscardNewestThreadPool,
                               Policies.discard_this: DiscardThisThreadPool}

    @staticmethod
    def get_policy_pool(policy: str, pool_type: str = "thread", max_q_size: int = 1, max_workers: int = 1):
        """
        Factory method for getting an instance of a policy pool
        :param policy: the policy to use for the desired pool
        :param pool_type: the backend to use for the pool (only two options: thread or process)
        :param max_q_size: the max size of the queue for workers waiting to be run
        :param max_workers: the maximum number of concurrent running workers
        :return: instance of a policy pool
        :rtype: PolicyPool
        """
        if pool_type == "thread":
            return PolicyPoolFactory.__thread_policy_mapping[policy](max_q_size, max_workers)
        elif pool_type == "process":
            return PolicyPoolFactory.__process_policy_mapping[policy](max_q_size, max_workers)
        else:
            raise ValueError("%s is not a valid pool type, the valid options are thread or process" % pool_type)
