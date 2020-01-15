import datetime
import sys
import requests
import re
import json
import time
from catscore.http.request import CatsRequest
from catscore.lib.logger import CatsLogging as logging
from catscore.lib.time import get_today_date, get_current_time
import logging
from bs4 import BeautifulSoup
from kakaku_robot.model.item import RankedItem
import itertools
import pandas as pd
from dataclasses import asdict

class Ranking:
    base_url = "https://kakaku.com"
    
    def __init__(self, proxy=None):
        """[summary]
        
        Arguments:
            headless {[type]} -- [description]
        
        Keyword Arguments:
            proxy {[type]} -- [description] (default: {None})
        """
        self.proxy = proxy
        self.request = CatsRequest()
        
    def top(self):
        """[https://kakaku.com/rankingにアクセス]
        
        Returns:
            [type] -- [description]
        """
        url = f"{self.base_url}/ranking"
        logging.info(f"request to {url}")
        response = self.request.get(url=url, response_content_type="html")
        return response

    @property
    def category_ranking_menu(self):
        """[ランキング一覧(カテゴリ別)を取得]
        
        Returns:
            [type] -- [description]
        """
        soup = self.top().content.find("ul", {"class": "category"}).findAll("li")
        r = dict(map(lambda s: (s.text, s.find("a").get("href")), soup))
        return r

    def category_ranking(self, folder):
        """[指定されたフォルダのランク付きアイテムを取得]
        
        Arguments:
            folder {[type]} -- [folder format like '/ranking/pc/']
        
        Returns:
            [type] -- [description]
        """
        top_soup = self.request.get(f"{self.base_url}{folder}", response_content_type="html").content
        rank_category = top_soup.find("div", {"class": "h3box clearfix"}).find("h3").text
        gathered_date = top_soup.find("p", {"class": "daytime"}).text
        logging.info(rank_category)
        logging.info(gathered_date)
        ranking_urls = dict(map(lambda s: (s.text, s.get("href")), top_soup.find("span", {"class": "pagingborder"}).findAll("a")))

        def _parse_page(soup):
            def _parse_item(i):
                    ranking_rate = i.find("td", {"class": "rankingRate"})
                    ranking_photo = i.find("td", {"class": "rankingPhoto"})
                    detail = i.find("td", {"class": "Detail"})
                    try:
                        raking_num = ranking_rate.find("span").text
                        img_src = ranking_photo.find("img").get("src")
                        maker = detail.find("span", {"class": "rank3BarMaker"}).text
                        item_name = detail.find("span", {"class": "rank3BarItem"}).text
                        category = detail.find("p", {"class": "rankingCate"}).text
                        item_url = detail.find("div", {"class": "rank3Bar rank3Bar-2"}).find("a").get("href")
                        item_id = item_url.split("/")[2]
                        ranking_sup_info = detail.find("ul", {"class": "rankingSupInfo"})
                        item_min_price = ranking_sup_info.find("li", {"class": "rankingSupInfoItemPrice"}).find("a").text
                        item_review_rate = ranking_sup_info.find("li", {"class": "rankingSupInfoItem rankingSupInfoItemReview"}).find("a").text
                        item_bbs_num = ranking_sup_info.find("li", {"class": "rankingSupInfoItemBbs"}).find("a").text
                        item = RankedItem(
                                    item_id=item_id,
                                    ranking_url=f"{self.base_url}{folder}",
                                    item_name=item_name,
                                    item_img_src=img_src,
                                    item_maker=maker,
                                    item_category=category,
                                    item_rank=int(raking_num),
                                    rank_category=rank_category,
                                    rank_gathered_date=gathered_date,
                                    item_url=f"{self.base_url}{item_url}",
                                    item_min_price=item_min_price,
                                    item_review_rate=item_review_rate,
                                    item_bbs_num=item_bbs_num)
                        return item
                    except:
                        return None
            ranking_items = soup.find("div", {"class": "itemElements"}).findAll("tr")
            r = list(filter(lambda s: s != None, map(lambda s: _parse_item(s), ranking_items)))
            return r
        # 1位～20位
        head_ranking = _parse_page(top_soup)
        logging.info(head_ranking)
        # 21位以下
        tail_ranking = list(map(lambda ranking_url: _parse_page(self.request.get(f"{self.base_url}{ranking_url}", response_content_type="html").content), ranking_urls.values()))
        logging.info(tail_ranking)
        tail_ranking.append(head_ranking)
        result = list(itertools.chain.from_iterable(tail_ranking))
        logging.info(result)
        return result

    def all_category_ranking(self, pandas=False):
        """[summary]
        """
        menu = self.category_ranking_menu
        r = list(map(lambda m: self.category_ranking(m), menu.values()))
        result = list(itertools.chain.from_iterable(r))
        if pandas:
            return pd.DataFrame([asdict(x) for x in result])
        else:
            return result