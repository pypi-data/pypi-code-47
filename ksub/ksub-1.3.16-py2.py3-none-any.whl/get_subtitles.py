# -*- coding: utf-8 -*-

# @Author: kagura
# @Date  : 2019/12/10
# @Desc  :
import argparse
import json
import logging
import mimetypes
import os

from ksub.subhd import Subhd
from ksub.utils import init_log, notify
from ksub.zimuku import Zimuku
from ksub import __version__, config

log = logging.getLogger('main')


class GetSubtitles(object):
    def __init__(self, args):
        self.video_ext_list = ['.avi', '.flv', '.mkv', '.mp4', '.mpv', '.wmv', '.3gp', '.mov', '.iso']
        self.sub_ext_list = ['.ass', '.srt', '.ssa', '.sub']
        self.path = args.path
        self.bluray = args.bluray
        self.overwrite = args.overwrite

    def start(self):
        video_files = self._get_video_files()
        if video_files:
            log.info('找到 {} 个视频文件.'.format(len(video_files)))
        else:
            log.error('找不到视频文件')
            return

        cache = {}
        for video_file in video_files:
            video_name, _ = os.path.splitext(video_file)
            # ret = list(filter(os.path.exists, map(lambda e: video_name + e, self.sub_ext_list)))
            if not self.overwrite and self._exist_sub(video_file):
                log.info('视频[{}]已存在字幕'.format(os.path.basename(video_file)))
                notify('ksub', '已存在字幕: [{}]'.format(os.path.basename(video_file)))
                continue
            log.info('-'*5 + '开始搜索 [{}]'.format(os.path.basename(video_file)) + '-'*5)
            # sub_path = ''
            subhd = Subhd(video_file, cache)
            sub_path = subhd.find_match_subtitle()
            cache = subhd.get_cache_dict()
            if sub_path:
                log.info('下载的字幕： {}'.format(sub_path))
                # break

            if not sub_path:
                zimuku = Zimuku(video_file, cache)
                sub_path = zimuku.find_match_subtitle()
                cache = zimuku.get_cache_dict()
                if sub_path:
                    log.info('下载的字幕： {}'.format(sub_path))

    def _get_video_files(self):
        """
        根据参数path，获取视频文件
        :return: 视频文件列表 [video_file1, video_file2,....]
        """
        result = []
        for path in self.path:
            log.debug('当前文件: {}'.format(path))
            if self._is_video_file(path):
                result.append(path)
            else:
                if self.bluray:
                    result.append(path + '.mkv')
                else:
                    for root, _, files in os.walk(path):
                        result.extend(filter(self._is_video_file, map(lambda f: os.path.join(root, f), files)))
        log.debug('文件去重...')
        result = list(set(result))
        return result

    def _exist_sub(self, video_file):
        video_name, _ = os.path.splitext(os.path.basename(video_file))
        root = os.path.dirname(video_file)
        for f in os.listdir(root):
            if self._is_file(os.path.join(root, f)):
                f_name, ext = os.path.splitext(f)
                if video_name in f_name and ext in self.sub_ext_list:
                    return True
        return False

    def _is_video_file(self, file):
        """
        判断是不是视频文件
        :param file: 文件
        :return:
        """
        if self._is_file(file):
            types = mimetypes.guess_type(file)
            if (types[0] and 'video' in types[0]) or (os.path.splitext(file)[1] in self.video_ext_list):
                log.debug('找到一个视频文件: {}'.format(file))
                return True
        return False

    @staticmethod
    def _is_file(file):
        """
        F.O. MacOS's ._file
        :param file:
        :return:
        """
        return os.path.isfile(file) and not os.path.basename(file).startswith('._')


def main():
    parser = argparse.ArgumentParser(prog='sub', epilog='epilog', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('path',
                        nargs='+',
                        help='the videos filename or the folder contains video files')
    parser.add_argument('-l', '--lang',
                        nargs='+',
                        help="the lang of subtitle")
    parser.add_argument('-e', '--extension',
                        nargs='+',
                        help="the extension of subtitle")
    parser.add_argument('-f', '--favorite',
                        nargs='+',
                        help="favorite author of subtitle")
    parser.add_argument('-b', '--blacklist',
                        nargs='+',
                        help="author of subtitle in blacklist")
    parser.add_argument('-c', '--config', default='~/.ksub.json',
                        help='path to config file')
    parser.add_argument('-v', '--version',
                        action='version', version='ksub {}'.format(__version__),
                        help="show ksub's version")
    parser.add_argument('--bluray', action='store_true', default=False, help='blury? search by directory name')
    parser.add_argument('--debug', action='store_true', default=False, help='logging debug level')
    parser.add_argument('-o', '--overwrite', action='store_true', default=False, help='overwrite exist subtitle')
    args = parser.parse_args()
    log.debug('args: {}'.format(args))

    if args.debug:
        config.debug = True
        init_log('main', logging.DEBUG)
    else:
        init_log('main')

    if args.lang:
        config.lang = args.lang
    if args.blacklist:
        config.blacklist = args.blacklist
    if args.extension:
        config.extension = args.extension
    if args.favorite:
        config.favorite = args.favorite

    args.config = os.path.expanduser(args.config)
    if os.path.exists(args.config):
        with open(args.config, 'r') as f:
            try:
                config_json = json.loads(f.read())
                log.debug('读取到的配置文件: {}'.format(config_json))
                config.lang = config_json.get('lang', [])
                config.blacklist = config_json.get('blacklist', [])
                config.extension = config_json.get('extension', [])
                config.favorite = config_json.get('favorite', [])
            except json.JSONDecodeError as _:
                log.error("配置文件格式错误！")
                return

    log.info('lang: {}'.format(config.lang))
    log.info('blacklist: {}'.format(config.blacklist))
    log.info('extension: {}'.format(config.extension))
    log.info('favorite: {}'.format(config.favorite))

    get_sub = GetSubtitles(args)
    get_sub.start()
    # os.system("pause")


if __name__ == '__main__':
    main()
