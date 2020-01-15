from dataclasses import dataclass
from . import CustomerStrategyRefsField


@dataclass
class StrategyRefs(CustomerStrategyRefsField):
    '''
    :param partition_matched_by_strategy_ref: If you ask for orders,
     returns the breakdown of matches by strategy for
     each selection. Defaults to false if unspecified.
    '''

    partition_matched_by_strategy_ref: bool = None
