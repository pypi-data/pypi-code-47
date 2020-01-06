#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : utils.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 04.01.2020
# Last Modified Date: 04.01.2020
# Last Modified By  : JCHRYS <jchrys@me.com>
import re
import requests
from bs4 import BeautifulSoup


re_all = re.compile('<[^>]*>')
def drop_html_tag_all(html):
    if html == None:
        return None
    #print(type(html))
    return re.sub(re_all, '', html)

def get_drop_html_tag_but(tag):
    regex = '(?!</?' + tag + '>)<.*?>'
    #print(regex)
    _re = re.compile(regex)
    def drop_html_tag(html):
        return re.sub(_re, '', html)
    return drop_html_tag 



def get_html_content_by_id(url, ids=[]) -> dict:
    if not isinstance(ids, list):
        raise Exception("not a list")
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return { id: soup.find(id=id).text if soup.find(id=id) else None for id in ids }

if __name__ == '__main__':
    print(drop_html_tag_all("<strong> Hello World!</strong>"))
    br_cleaner = get_drop_html_tag_but('all')
    print(br_cleaner("<br>GOOODDADSAD<br>>"))
    detail_url = 'http://book.naver.com/bookdb/book_detail.php?bid=15433261'
    print(get_html_content_by_id(detail_url, 
        ['authorIntroContent', 'bookIntroContent', 'tableOfContentsContent']))
