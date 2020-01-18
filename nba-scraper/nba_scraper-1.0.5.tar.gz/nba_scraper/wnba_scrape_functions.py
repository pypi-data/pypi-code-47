"""
Date: 2019-12-30
Contributor: Matthew Barlowe
twitter: @barloweanalytic
email: matt@barloweanalytics.com

This file contains the main functions to scrape and compile the WNBA api
"""
import sys
import json
import datetime
import requests
import time
import pandas as pd
import numpy as np


def get_pbp_api(game_id, quarter, season):
    """
    function gets both JSON requests from the two different APIs if both
    are available and only the stats.nba.com api if not.

    Inputs:
    game_id          - String representing game id
    quarter          - number representing what quarter you want
    season           - number in the format of YYYY representing what the season is

    Outputs:
    wnba_dict         - Dictionary of the JSON response from data.wnba.com api
    """
    wnba_api_url = f"https://data.wnba.com/data/5s/v2015/json/mobile_teams/wnba/{season}/scores/pbp/1{game_id}_{quarter}_pbp.json"

    try:
        wnba_rep = requests.get(wnba_api_url)
    except json.decoder.JSONDecodeError as ex:
        print(ex)
        print(f"This is the stats.nba.com API's output: {wnba_rep.text}")
        sys.exit()

    wnba_dict = wnba_rep.json()

    return wnba_dict
