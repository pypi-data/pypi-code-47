from dataclasses import dataclass


@dataclass
class TimeGranularityField:
    '''
    The granularity of time periods that correspond to
     markets selected by the market filter.
     The possible options listed in TimeGranularity enum
    '''
    time_granularity: str
