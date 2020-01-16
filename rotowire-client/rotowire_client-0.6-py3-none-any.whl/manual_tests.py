from pprint import pprint
from datetime import date
from roto_wire_client import RotoWireClient

rw_client = RotoWireClient()

start_date = date(2020, 1, 13)
end_date = date(2020, 1, 13)

print("\n Testing get_nba_injured_players \n")

data_players = rw_client.get_nba_injured_players()
pprint(data_players)

print("\n Testing get_injuries_report \n")
data_news = rw_client.get_injuries_report(start_date, end_date)
pprint(data_news)
