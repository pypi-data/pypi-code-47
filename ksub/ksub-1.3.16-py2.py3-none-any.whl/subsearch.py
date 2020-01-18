# -*- coding: utf-8 -*-

# @Author: kagura
# @Date  : 2019/12/10
# @Desc  :
import json
import os
import re
import cgi
import logging
import requests

from abc import ABCMeta, abstractmethod
from guessit import guessit
from six.moves.urllib.parse import urlparse

from ksub import config
from ksub.decompress import Decompress
from ksub.utils import lang_ext_weight, notify

log = logging.getLogger('main.base')


class BaseSubSearch(object):
    __metaclass__ = ABCMeta

    def __init__(self, video_file, cache):
        self.RE_SEASON_EPISODE = re.compile(r'[Ss](?P<season>\d+).*[Ee](?P<episode>\d+)')
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.181 Safari/537.36'
        }
        self.session.headers.update(self.headers)
        self.video_file = video_file
        self.video_name = self._get_video_name()
        self.video_info = dict(guessit(video_file))
        self.dl_url = None
        self.all_season = False
        self.sub_info = {
            'title': '',
            'link': '',
            'author': '',
            'label': '',
            'weight': -999999,
            'dl_count': -1,
            'score': 0,
            'lang': ''
        }

        # 要下载的字幕
        self.target_sub = None

        # 这两个存的是与视频匹配的字幕
        # 最基本信息：（名字与【年份（电影）或季集（剧集）】）
        self.sub_list = {
            'collection': [],
            'single': []
        }
        self._cache = cache

    @abstractmethod
    def get_subtitle_list(self):
        pass

    @abstractmethod
    def get_dl_link(self):
        pass

    def _sub_filter(self):
        log.info('开始过滤...')
        """
        自动选择器 😁
        选择权重最大的字幕
        :return:
        """
        # single = list(filter(lambda x: self._match_video(x.get('title', '')), self.sub_list.get('single')))
        single = self.sub_list.get('single')
        single.sort(key=lambda x: (x['weight']), reverse=True)

        # collection = list(filter(lambda x: self._match_video(x.get('title', '')), self.sub_list.get('collection')))
        collection = self.sub_list.get('collection')
        collection.sort(key=lambda x: (x['weight']), reverse=True)

        # log.debug('已过滤列表：{}'.format(self.sub_list))

        # 选取权重最大的
        if collection and len(collection) > 0 and collection[0].get('weight', 0) > 10000:
            self.target_sub = collection[0]
            self.all_season = True
        else:
            if single and len(single) > 0:
                self.target_sub = single[0]

    # def _match_video(self, sub_title):
    #     """
    #     匹配source，release_group
    #     :return:
    #     """
    #     subtitle_info = dict(guessit(sub_title))
    #     log.debug('  sub_info: {}'.format(subtitle_info))
    #     log.debug('video_info: {}'.format(self.video_info))
    #     # if self.video_info.get('release_group', ''):
    #     #     if self.video_info.get('release_group').lower() not in subtitle_info.get('release_group', '').lower() \
    #     #             and subtitle_info.get('release_group', '').lower() not in self.video_info.get('release_group').lower():
    #     #         return False
    #     return subtitle_info.get('source', None) == self.video_info.get('source', '')

    def find_match_subtitle(self):
        video_dir = os.path.dirname(self.video_file)
        local_sub_all_season = os.path.join(video_dir, self.creat_name_with_season())
        all_season_sub = ''
        if os.path.exists(local_sub_all_season + '.rar'):
            all_season_sub = local_sub_all_season + '.rar'
        if os.path.exists(local_sub_all_season + '.zip'):
            all_season_sub = local_sub_all_season + '.zip'
        # 本地已下载的整季字幕
        if all_season_sub:
            log.info('已下载的整季字幕：{}'.format(os.path.basename(all_season_sub)))
            sub_path = all_season_sub
            self.all_season = True
        else:
            # 获取字幕列表[sub_info1, sub_info2, ...]
            # 解析网页的字幕列表
            self.get_subtitle_list()
            log.debug('未过滤的列表：{}'.format(json.dumps(self.sub_list)))

            # 过滤
            self._sub_filter()
            if not self.target_sub:
                notify(self.__class__.__name__, '找不到匹配的字幕')
                log.error('找不到匹配的字幕')
                # 找不到匹配的字幕，清空缓存
                self.clear_cache()
                # raise RuntimeError('找不到匹配的字幕')
                return
            log.info('要下载的字幕：{}'.format(self.target_sub))
            notify(self.__class__.__name__, '找到字幕：{}'.format(self.target_sub.get('title', '')))

            # 获取真正的下载地址
            self.dl_url = self.get_dl_link()
            log.info('获取到的下载地址: {}'.format(self.dl_url))

            # 下载
            sub_path = self._download_sub()

        # 解压
        decompress = Decompress()
        # 判断是不是压缩文件
        if decompress.is_compressed(sub_path):
            sub_name = self._name_sub_file()
            # sub_name, _ = os.path.splitext(sub_path)
            ext_sub_path = decompress.extract(sub_path, sub_name, self.all_season)
            if ext_sub_path:
                # 移除压缩包
                if not self.all_season:
                    os.remove(sub_path)
                log.debug('Extract success.')
                sub_path = ext_sub_path
            else:
                # 解压失败
                sub_path = ''
                return sub_path
        # 最终完成
        log.debug('已下载的字幕：{}'.format(os.path.basename(sub_path)))
        notify(self.__class__.__name__, '已下载的字幕：{}'.format(os.path.basename(sub_path)))
        return sub_path

    # 下载字幕，按照视频名字命名
    def _download_sub(self):
        log.info('开始下载字幕...')
        url = self.dl_url
        video_file = self.video_file
        log.debug('Start download sub: ' + url)
        root = os.path.dirname(video_file)
        # video_name, _ = os.path.splitext(os.path.basename(video_file))
        sub_ext = ''
        resp = self.session.get(url)
        content_disposition = resp.headers.get('Content-Disposition', '')
        if content_disposition:
            _, params = cgi.parse_header(content_disposition)
            filename = params.get('filename', '')
            if filename:
                _, ext = os.path.splitext(filename)
                sub_ext = ext[1:]
        if sub_ext == '':
            link_path = urlparse(resp.url).path
            if link_path:
                _, ext = os.path.splitext(link_path)
                sub_ext = ext[1:]

        if self.all_season:
            sub_name = self.creat_name_with_season()
        else:
            sub_name = self._name_sub_file()

        sub_full_name = '{}.{}'.format(sub_name, sub_ext)
        sub_path = os.path.join(root, sub_full_name)
        with open(sub_path, 'wb') as f:
            f.write(resp.content)
        return sub_path

    def _name_sub_file(self):
        sub_name = self.video_name
        if self.target_sub:
            if self.target_sub['author']:
                sub_name += '.' + self.target_sub['author']
            # if self.target_sub['lang']:
            #     sub_name += '.' + self.target_sub['lang']
        return sub_name

    def _get_video_name(self):
        video_name, _ = os.path.splitext(os.path.basename(self.video_file))
        return video_name
        # return os.path.basename(self.video_file)

    def put_cache(self, keyword, content):
        """
        根据搜索的关键字keyword缓存字幕列表html
        :param keyword: 搜索的关键字
        :param content: 字幕列表html
        :return:
        """
        self._cache[self._creat_cache_key(keyword)] = content

    def get_cache(self, keyword=None):
        """
        获取搜索的关键字keyword字幕列表html
        :param keyword: 搜索的关键字
        :return: 字幕列表html
        """
        key = self._creat_cache_key(keyword)
        if self._cache and key in self._cache:
            return self._cache[key]
        return None

    def _creat_cache_key(self, keyword):
        if not keyword:
            keyword = self.create_keyword()
        else:
            keyword.replace(' ', '')
        key = self.__class__.__name__ + '_' + keyword
        return key

    def get_cache_dict(self):
        return self._cache

    def clear_cache(self):
        """
        如果获取不到字幕则清空缓存
        :return:
        """
        self._cache = {}

    def creat_name_with_season(self):
        """
        :Input: Seven.Worlds.One.Planet.S01E01.Antarctica.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTb.mkv
        :return: Seven.Worlds.One.Planet.S01
        """
        match = self.RE_SEASON_EPISODE.search(self.video_name)
        season_title = 'all_season'
        if match:
            s, e = match.span('season')
            season_title = self.video_name[0:e].strip('.')
        return season_title.lower()

    def def_weight(self, sub_dict):
        """
        根据喜好配置定义权重
        :param sub_dict:
        :return:
        """
        weight = 0
        sub_guess_info = dict(guessit(sub_dict.get('title', '')))
        v_group = self.video_info.get('release_group', '').lower()
        s_group = sub_guess_info.get('release_group', '').lower()
        log.debug('视频GP: {}, 字幕GP: {}'.format(v_group, s_group))
        log.debug('视频source: {}, 字幕source: {}'.format(self.video_info.get('source', ''), sub_guess_info.get('source', None)))

        # if v_group:
        if sub_guess_info.get('source', None) == self.video_info.get('source', ''):
            if v_group and (v_group in s_group or s_group in v_group):
                weight += 10000
            else:
                weight += max(1000, len(config.favorite) * 100)

        author = sub_dict.get('author', '').lower()
        log.debug('字幕author: {}'.format(author))
        for index, a in enumerate(config.favorite):
            if config.author_alias.get(a, ''):
                for alias in config.author_alias.get(a):
                    if alias in author:
                        weight += (len(config.favorite) - index) * 100
                        break
            else:
                if a in author:
                    weight += (len(config.favorite) - index) * 100
            if weight != 0:
                break

        if author in config.blacklist:
            weight += -20000

        weight_lang_ext, _ = lang_ext_weight(sub_dict.get('label', '').lower())
        log.debug('weight_lang_ext: {}'.format(weight_lang_ext))
        weight += weight_lang_ext
        return weight

    def create_keyword(self):
        # keywords = []
        if self.video_info['type'] == 'episode':
            return self.creat_name_with_season()
        return self.video_info['title']
        # return keywords


if __name__ == '__main__':
    pass
