#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : main.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 04.01.2020
# Last Modified Date: 06.01.2020
# Last Modified By  : JCHRYS <jchrys@me.com>
import platform
import time
import json
import os
from tqdm import tqdm
from nbs import settings
from nbs.core import utils
from nbs.core.requester import Request

from pprint import pprint

## os_validation ##
if (platform.system() != 'Darwin'):
    print('Your OS is not supported')
    exit()
##TODO header, params, url 
def main():
    request = Request(settings.default_headers, settings.default_params, settings.default_url)
    output_filename = input('output_filename: ')
    keyword_count = input('how many keywords? ')
    keywords = []
    for i in range(int(keyword_count)):
        keywords.append(input('keywords No.' + str(i+1) + ' '))
    res_json = []
    for keyword in tqdm(keywords, leave=True, desc='total', ncols=80):
        res = request.search(keyword).json()
        detail_ids = ['authorIntroContent', 'bookIntroContent', 'tableOfContentsContent']
        items = res['items']
        toc = 'tableOfContentsContent'

        for item in tqdm(items, desc=keyword, leave=False, ncols=80):
            detail_dict = utils.get_html_content_by_id(item['link'], detail_ids)
            item.update(detail_dict)
            for key in item.keys():
                item[key] = utils.drop_html_tag_all(item[key])
            if 'isbn' in item and len(item['isbn'].split()) == 2:
                isbn10, isbn13 = item['isbn'].split()
                item['isbn10'] = isbn10
                item['isbn13'] = isbn13
            if toc in item and item[toc]:
                item[toc] = item[toc].replace('\r', '\n\t')
        res_json.extend(items)

    with open(os.path.join(settings.path_to_output, output_filename + '.json'), 'w', encoding='utf8') as file:
        json.dump(res_json, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
