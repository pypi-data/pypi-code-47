# -*- coding: utf-8 -*-

# @Author: kagura
# @Date  : 2019/12/10
# @Desc  :
import logging
import re
import bs4

from guessit import guessit
from ksub.subsearch import BaseSubSearch
from ksub.utils import get_alpha, num2cn, init_log

log = logging.getLogger('main.zimuku')


class Zimuku(BaseSubSearch):
    def __init__(self, video_file, cache):
        super().__init__(video_file, cache)
        self.host = 'http://www.zimuku.la'
        self.search_uri = '/search'
        self.dl_host = 'http://zmk.pw'

    def get_subtitle_list(self):
        # 获取list连接
        search_keyword = self.create_keyword()
        cache_html = self.get_cache(search_keyword)
        if cache_html:
            list_html = cache_html
            log.info('读取缓存的html')
        else:
            sub_list_url = self._parse_search(search_keyword)
            if not sub_list_url:
                log.info('找不到sub_list_url')
                return
            # log.info('获取到的sub_list_url: {}'.format(sub_list_url))

            # 获取列表页面html
            list_url = self.host + sub_list_url
            list_html = self.session.get(url=list_url).text
            self.session.headers.update({'Referer': list_url})
            self.put_cache(search_keyword, list_html)
        # 解析列表
        self._parse_list(list_html)
        # log.info('字幕列表: {}'.format(json.dumps(self.sub_list)))

    def get_dl_link(self):
        url = self.host + self.target_sub['link']
        dl_page_html = self.session.get(url)
        self.session.headers.update({'Referer': dl_page_html.url})
        soup = bs4.BeautifulSoup(dl_page_html.text, 'html.parser')
        ele_a_list = soup.select('a.btn.btn-sm')
        if not ele_a_list:
            return None
        ele_a = ele_a_list[1]
        download_link = ele_a.get('href')
        if not download_link.startswith('http'):
            download_link = self.dl_host + download_link
        return download_link

    def _parse_search(self, keyword):
        log.info('尝试获取sub_list_url...')
        sub_list_url = ''
        # keyword = self.create_keyword()
        url = self.host + self.search_uri
        self.session.headers.update({'Referer': self.host})
        search_html = self.session.get(url=url, params={'q': keyword}).text
        self.session.headers.update({'Referer': url})
        bs = bs4.BeautifulSoup(search_html, 'html.parser')

        group_list = bs.select('div.item.prel.clearfix')
        for group in group_list:
            title = group.select_one('p.tt.clearfix')
            sub_list_url = title.a.get('href')
            group_title = title.a.b.text
            log.debug('搜索页字幕标题: {}'.format(group_title))
            group_size = len(group_list)
            if self._is_match_title_and_season_or_year(group_title, group_size):
                log.info('找到匹配的列表: {}，URL：{}'.format(group_title, sub_list_url))
                return sub_list_url
            else:
                log.debug('仍在尝试...')
                sub_list = group.select('tbody > tr')
                for sub in sub_list:
                    sub_title = sub.select('a')[0].text
                    if self._is_match_title_and_season_or_year(sub_title, group_size):
                        log.debug('匹配的sub_list_url: {}'.format(sub_list_url))
                        return sub_list_url
        return sub_list_url

    def _parse_list(self, html):
        collection = []
        single = []
        bs = bs4.BeautifulSoup(html, 'html.parser')
        # 获取各个tr
        table_list = bs.find('tbody').findAll('tr')
        # 遍历tr
        for tr in table_list:
            # 解析tr
            sub_info = self._parse_tr(tr)
            # 匹配
            sub_title = sub_info.get('title', '')
            if self._is_all_season(sub_title):
                sub_info['weight'] = self.def_weight(sub_info)
                log.debug('匹配全季: {}'.format(sub_info))
                collection.append(sub_info)
                continue

            if self.video_info.get('type', '') == 'episode':
                if self._match_episode(sub_title):
                    sub_info['weight'] = self.def_weight(sub_info)
                    log.debug('匹配单集: {}'.format(sub_info))
                    single.append(sub_info)
            else:
                sub_info['weight'] = self.def_weight(sub_info)
                single.append(sub_info)
        self.sub_list['collection'] = collection
        self.sub_list['single'] = single

    def _parse_tr(self, tr):
        sub_info = self.sub_info.copy()
        td = tr.find('td', class_='first')
        if td:
            # 字幕标题
            sub_info['title'] = td.a.get('title').strip()
            # 链接
            sub_info['link'] = td.a.get('href').strip().replace('detail', 'dld')
            # 格式
            label_info_list = td.select('span.label.label-info')
            for label_info in label_info_list:
                ext = label_info.get_text().strip().lower()
                ext = ext.split('/')
                sub_info['label'] = ','.join(ext)

            # 作者
            label_author = td.select('span > a > span.label.label-danger')
            if label_author:
                sub_info['author'] = label_author[0].get_text().strip().replace('字幕组', '')
            # 语言
            lang_list = tr.select('td.tac.lang > img')
            if lang_list:
                langs = []
                for lang in lang_list:
                    l = lang.get('title', lang.get('alt'))
                    langs.append(l.replace('字幕', ''))
                sub_info['label'] = sub_info.get('label', '') + ',' + ','.join(langs)
            dl_count = tr.select('td.tac.hidden-xs')[1].get_text()
            if '万' in dl_count:
                dl_count = float(dl_count.replace('万', '')) * 10000
            sub_info['dl_count'] = int(dl_count)
            # sub_info['weight'] = self.def_weight(sub_info)
        log.debug('解析tr结果: {}'.format(sub_info))
        return sub_info

    def _is_match_title_and_season_or_year(self, sub_title, size):

        title = self.video_info.get('title', '')
        # 匹配标题
        match_title = get_alpha(title) in get_alpha(sub_title)

        if self.video_info.get('type', '') == 'episode':
            season = self.video_info.get('season', -1)
            # 匹配季
            if match_title and '第' + num2cn(season) + '季' in sub_title:
                log.debug('匹配季')
                # log.debug('========')
                return True
            elif match_title and size == 1 and season == 1:
                # 如果电视剧只有一季zimuku不会标出"第一季"
                # log.debug('---------------')
                return True
        else:
            # 匹配年份
            if match_title and str(self.video_info.get('year', -1)) in sub_title:
                return True
        return False

    @staticmethod
    def _create_keyword(video_info):
        keywords = []
        if video_info['type'] == 'episode':
            keywords.append(video_info['title'] + '.S' + "%02d" % video_info['season'])
        keywords.append(video_info['title'])
        return keywords

    def _match_episode(self, title):
        video_info = self.video_info
        sub_info = dict(guessit(title))
        sub_episode = sub_info.get('episode', -1)
        video_episode = video_info.get('episode', -2)
        if sub_episode == video_episode:
            return True
        return False

    @staticmethod
    def _is_all_season(text):
        log.debug('要匹配全季的标题: {}'.format(text))
        re_collection = re.compile(r'.*全((.*)(\d+)(.*)(\d+)(.*))?集.*')
        # ALL2 = re.compile(r'.*[1].*[0-9]{1,2}.*集')
        if re_collection.search(text):
            log.debug('标题[%s]匹配全季' % text)
            return True
        return False


if __name__ == '__main__':
    init_log('main', logging.DEBUG)
