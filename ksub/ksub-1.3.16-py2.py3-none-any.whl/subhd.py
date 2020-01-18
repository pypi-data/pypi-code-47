import json
import logging
import re
import bs4

from collections import Counter
from guessit import guessit
from ksub.subsearch import BaseSubSearch
from ksub.utils import init_log, get_alpha

log = logging.getLogger('main.subhd')


class Subhd(BaseSubSearch):

    def __init__(self, video_file, cache):
        super().__init__(video_file, cache)
        self.host = 'https://subhd.tv'
        self.search_uri = '/search0'

    def get_subtitle_list(self):
        # return
        search_keyword = self.create_keyword()
        cache_html = self.get_cache(search_keyword)
        if cache_html:
            list_html = cache_html
            log.info('读取缓存的html')
        else:
            db_url = ''
            # subhd首次搜索大概率失败，默认尝试两次
            for i in range(2):
                db_url = self._parse_search(search_keyword)
                if db_url:
                    break
            # db_url = self._parse_search()
            # 搜索无结果
            if not db_url:
                log.info('找不到db_url')
                return
            db_url = self.host + db_url
            log.info('获取到的db_url: {}'.format(db_url))

            # 请求获取html
            list_html = self.session.get(db_url).text
            self.put_cache(search_keyword, list_html)

        if self.video_info['type'] == 'episode':
            collection = self._parse_by_tr(list_html, '合集')
            log.debug('合集: {}'.format(collection))
            episode = self.video_info.get('episode', -1)
            log.debug('episode: {}'.format(episode))
            single = self._parse_by_tr(list_html, str(episode))
            log.debug('单集: {}'.format(single))
            self.sub_list = {
                'collection': collection,
                'single': single
            }
        else:
            single = self._parse_by_tr(list_html)
            log.debug('单集: {}'.format(single))
            self.sub_list = {
                'collection': [],
                'single': single
            }

    def _parse_by_tr(self, html, text=''):
        ret = []
        bs = bs4.BeautifulSoup(html, 'html.parser')
        table_list = bs.find_all('tr', class_='dt_ep')
        # 解析电视剧
        if table_list:
            current_tr = None
            for tr in table_list:
                if text in str(tr.td):
                    current_tr = tr
                    log.info('找到匹配的tr：{}'.format(tr.td.text))
                    break

            while current_tr:
                current_tr = current_tr.find_next('tr')
                if not current_tr or 'dt_ep' in str(current_tr):
                    break
                sub_info = self._parse_tr(current_tr)
                # log.debug('解析tr结果: ', sub_info)
                ret.append(sub_info)
        # 解析电影
        else:
            table_list = bs.find('tbody').findAll('tr')
            for tr in table_list:
                sub_info = self._parse_tr(tr)
                # log.debug('解析tr结果: ', sub_info)
                ret.append(sub_info)
        return ret

    def _parse_tr(self, tr):
        result = self.sub_info.copy()
        label = [x.text for x in tr.findAll('span')]
        result['label'] = ','.join(label).lower()
        if 'dt_ep' not in str(tr):
            edition = tr.td.select_one('div.dt_edition')
            result['link'] = edition.a.get('href').strip()
            result['title'] = edition.text
        dl_info = tr.find('td', class_='dt_count')
        if dl_info and dl_info.next_element:
            result['dl_count'] = int(dl_info.next_element.strip())
            if dl_info.select('b.red'):
                result['score'] = dl_info.select_one('b.red').text
        if tr.select_one('a.gray'):
            result['author'] = tr.select_one('a.gray').text.replace('字幕组', '')
        result['weight'] = self.def_weight(result)
        log.debug('解析tr结果: {}'.format(result))
        return result

    def _parse_search(self, keyword):
        log.info('尝试获取db_url...')
        """
        解析搜索页面，目的是获取db_url，该url下的字幕精确匹配视频
        :return:
        """
        db_url = []
        # keyword = self.create_keyword()
        search_url = self.host + self.search_uri + '/' + keyword
        log.debug('keyword: {}, search url: {}'.format(keyword, search_url))
        html = self.session.get(search_url).text
        bs = bs4.BeautifulSoup(html, 'html.parser')
        sub_list = bs.select('div.box')
        page = bs.select_one('ul.pagination')
        if page:
            page_size = len(page.findAll('li')) - 1
            log.info('page_size: {}'.format(page_size))
        for sub in sub_list:
            title = sub.select('div.d_title')
            a_href = sub.find('a').get('href')
            if self._is_match_title_and_season_or_year(title[0].a.get('title')) \
                    or self._is_match_title_and_season_or_year(title[0].a.text):
                if '/do0/' in a_href:
                    log.debug('匹配的do0, Title: {}, Link:{} '.format(title[0].a.text, a_href))
                    db_url.append(a_href)
        ret = Counter(db_url).most_common(1)
        if ret and ret[0]:
            return ret[0][0]
        return None

    def get_dl_link(self):
        dl_url = ''
        sub_url = self.host + self.target_sub['link']
        html = self.session.get(sub_url).text
        bs = bs4.BeautifulSoup(html, 'html.parser')
        dl_btn = bs.find('button', id='down')
        dtoken = dl_btn.get('dtoken')
        sid = dl_btn.get('sid')
        r = self.session.post(self.host + '/ajax/down_ajax', data={'sub_id': sid, 'dtoken': dtoken})
        log.debug('ajax 获取下载地址结果：{}'.format(r.text))
        if r.text:
            # 返回的json
            data = json.loads(r.text)
            # 如果成功则获取到URL
            if data.get('success', False):
                dl_url = data.get('url', '')
                if dl_url:
                    # log.info(dl_url)
                    return dl_url
        return dl_url

    def _is_match_title_and_season_or_year(self, sub_title):
        """
        :param sub_title: 字幕标题
        :return: 如果字幕匹配视频，则返回True
        """
        log.debug('filter subtitle {}'.format(sub_title))
        # 如果以.结尾, guessit有bug
        if sub_title.endswith('.'):
            sub_title = sub_title[:-1]
        # video_info = self.video_info
        sub_info = dict(guessit(sub_title))
        log.debug('--------guess sub info: ' + str(sub_info))
        log.debug('--------guess video info: ' + str(self.video_info))
        # 匹配 标题
        match_title = False
        video_title = self.video_info.get('title', '')
        for key, value in sub_info.items():
            if 'title' in key:
                log.debug('sub {}: [{}], video title: [{}]'.format(key, value, video_title))
                if re.search(get_alpha(video_title), get_alpha(str(value)), re.IGNORECASE):
                    match_title = True
                    log.debug('匹配标题 {}'.format(match_title))
        # log.debug(self.video_info.get('type', ''))
        if self.video_info.get('type', '') == 'episode':
            # 匹配 季
            if match_title and sub_info.get('season', 0) == self.video_info.get('season', -1):
                log.debug('匹配季')
                return True
        else:
            # 匹配 年份
            if match_title and str(sub_info.get('year', 0)) == str(self.video_info.get('year', -1)):
                log.debug('匹配年份')
                return True
        return False


if __name__ == '__main__':
    init_log('main', logging.DEBUG)
