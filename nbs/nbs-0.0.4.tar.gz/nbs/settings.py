#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : settings.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 04.01.2020
# Last Modified Date: 06.01.2020
# Last Modified By  : JCHRYS <jchrys@me.com>
#################################
##### NAVER BOOK API PARSER #####
#################################
import os

# Ouput Folder
path_to_output = os.path.join(os.getcwd(), 'nb')


# API_URLS
default_url = "https://openapi.naver.com/v1/search/book.json"

# API KEYS
client_id = 'dnDZOXWtoDfDYS0zPt10'
client_secret = 'fYGT4Tfb8C'

default_headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
}

query: str = ""
item_per_page : int = 100
page_num : int = 1

default_params = {
    "query": query,
    "display": item_per_page,
    "start": page_num,
    #sort: "sim",
}
