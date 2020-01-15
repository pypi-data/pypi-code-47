from dataclasses import dataclass


@dataclass
class RunnerIdsField:
    '''
    The unique id for the market.
    '''
    runner_ids: list = None
