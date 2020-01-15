from dataclasses import dataclass


@dataclass
class CustomerStrategyRefsField:
    '''
    :param customer_strategy_refs: If you ask for orders, restricts
    the results to orders matching any of the specified set of
     customer defined strategies. Also filters which matches by
     strategy for selections are returned, if
     partitionMatchedByStrategyRef is true. An empty set will
     be treated as if the parameter has been omitted (or null passed).

    '''
    customer_strategy_refs: str = None
