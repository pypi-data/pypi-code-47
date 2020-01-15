from datetime import datetime
from dataclasses import dataclass
from .events_and_event_type_ids import EventAndEventTypeIds


@dataclass
class MarketFilter(EventAndEventTypeIds):
    '''
    List of params of MarketFilter below.
        :param text_query: string, Restrict markets by any text associated
        with the market such as the Name, Event, Competition, etc.
        You can include a wildcard (*) character as long as
         it is not the first character.

        :param competitions_ids: list of strings, Restrict markets by the competitions
        associated with the market.

        :param market_ids: list of strings, Restrict markets by the market id associated
        with the market.

        :param venues: list of strings, Restrict markets by the venue associated
        with the market. Currently only Horse Racing markets have venues.

        :param bsp_only: boolean, Restrict to bsp markets only, if True or
        non-bsp markets if False. If not specified then returns both
        BSP and non-BSP markets

        :param in_play_enabled: boolean, Restrict to markets that will turn in play
        if True or will not turn in play if false. If not specified, returns both.

        :param in_play_only: boolean, Restrict to markets that are currently
        in play if True or are not currently in play if
        false. If not specified, returns both.

        :param market_betting_types: set of string. Restrict to markets that match
        the betting type of the market from MarketBettingType
         enum (i.e. Odds, Asian Handicap Singles, Asian Handicap Doubles or Line)

        :param market_countries: list of strings. Restrict to markets that are
        in the specified country or countries

        :param market_type_codes: list of strings.
        Restrict to markets that match the type of
        the market (i.e., MATCH_ODDS, HALF_TIME_SCORE). You should
        use this instead of relying on the market name as the market
        type codes are the same in all locales. Please note: All marketTypes
        are available via the listMarketTypes operations.

        :param market_start_time: dict, Restrict to markets with a
        market start time before or after the specified date.
         Should be contain two keys (from and to) with dates

        :param with_orders: Restrict to markets that I have
        one or more orders in these status. The variables listed in OrderStatus enum

        :param race_types: list of strings.	Restrict by race
        type (i.e. Hurdle, Flat, Bumper, Harness, Chase)
    '''
    text_query: str = None
    competitions_ids: list = None
    market_ids: list = None
    venues: list = None
    bsp_only: bool = None
    in_play_enabled: bool = None
    in_play_only: bool = None
    market_betting_types: list = None
    market_countries: list = None
    market_type_codes: list = None
    market_start_time: datetime.time = None
    with_orders: bool = None
    race_types: list = None

    @property
    def market_filter_data(self):
        data = {
            'textQuery': self.text_query, 'eventTypeIds': self.event_type_ids,
            'eventIds': self.event_ids, 'competitionIds': self.competitions_ids,
            'marketIds': self.market_ids, 'venues': self.venues, 'bspOnly': self.bsp_only,
            'turnInPlayEnabled': self.in_play_enabled, 'inPlayOnly': self.in_play_only,
            'marketBettingTypes': self.market_betting_types, 'marketCountries': self.market_countries,
            'marketTypeCodes': self.market_type_codes, 'marketStartTime': self.market_start_time,
            'withOrders': self.with_orders, 'raceTypes': self.race_types
        }
        return data
