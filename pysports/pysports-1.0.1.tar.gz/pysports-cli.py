import argparse
from pysports.cricapi import CricAPI
import credits

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apikey", help="API Key is offered by API providers.")
    parser.add_argument("--host", help="API Key is offered by API providers.")
    parser.add_argument("--operation", help="What do you want to access from pysports.")
    parser.add_argument("--match_id", help="Enter match_id/unique_id offered by API providers.")
    parser.add_argument("--player_id", help="Enter player_id offered by API providers.")
    arg = parser.parse_args()

    arg.apikey = credits.APIKEY
    arg.host = credits.HOST

    if arg.apikey and arg.host:
        cric = CricAPI(arg.apikey, arg.host)
        if arg.operation == "upcoming_matches":
            print(cric.upcoming_matches())

        elif arg.operation == "historical_matches":
            print(cric.historical_matches())

        elif arg.operation == "match_summary":
            print(cric.match_summary(arg.match_id))

        elif arg.operation == "live_score":
            print(cric.live_score(arg.match_id))

        elif arg.operation == "about_player":
            print(cric.about_player(arg.player_id))
        else:
            print("This operation is not available.")
    else:
        print("This is CLI interface for pysports software.")
