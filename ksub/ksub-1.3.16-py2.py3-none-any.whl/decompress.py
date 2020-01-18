# -*- coding: utf-8 -*-

import logging
import os
import platform
import re
import zipfile
import rarfile
from collections import OrderedDict
from io import BytesIO

from ksub.utils import decode_file_name, lang_ext_weight, init_log, notify

log = logging.getLogger('main.extract')


class Decompress(object):

    def __init__(self):
        self.RE_SEASON_EPISODE = re.compile(r'[Ss](?P<season>\d+).*[Ee](?P<episode>\d+)')
        self.compress_ext_list = ['.zip', '.rar', '.7z']

    def extract(self, file, sub_name, all_season=False):
        sub_path = ''
        if file.endswith('.zip'):
            zip_file = zipfile.ZipFile(file, 'r')
        elif file.endswith('.rar'):
            if platform.system() == 'Windows':
                rarfile.UNRAR_TOOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unrar.exe')
                zip_file = rarfile.RarFile(file)
                log.debug(rarfile.UNRAR_TOOL)
            # ！！！mac下"自动操作-右键快捷键，解压rar报错"
            elif platform.system() == 'Darwin':
                try:
                    from unrar import rarfile as unrar_rarfile
                    zip_file = unrar_rarfile.RarFile(file)
                except OSError as e0:
                    log.error('import unrar_rarfile error')
            else:
                try:
                    rarfile.UNRAR_TOOL = os.path.join('/usr/bin/unrar')
                    # zip_file = rarfile.RarFile(file)
                except Exception as e:
                    log.error('unrar not found')
                zip_file = rarfile.RarFile(file)
        else:
            log.error('不支持的压缩文件格式: ' + file)
            notify(self.__class__.__name__, '不支持的压缩文件格式：{}'.format(file))
            return sub_path

        keyword = ''
        if all_season:
            m = self.RE_SEASON_EPISODE.search(sub_name)
            if m:
                keyword = 's%02de%02d' % (int(m.group('season')), int(m.group('episode')))
                log.debug('Start extract zipfile.')
                inner_zips = list(filter(lambda x: self.is_compressed(x) and keyword in x.lower(), zip_file.namelist()))
                if inner_zips:
                    inner_zip = inner_zips[0]
                    if inner_zip.endswith('.zip'):
                        zip_file = zipfile.ZipFile(BytesIO(zip_file.read(inner_zip)), 'r')
                    elif inner_zip.endswith('.rar'):
                        zip_file = rarfile.RarFile(BytesIO(zip_file.read(inner_zip)), 'r')
                    else:
                        log.error('不支持的压缩文件格式[inner]: ' + file)

                    all_season = False
        sub_dict = {}
        for name in zip_file.namelist():
            decoded_name = decode_file_name(name).lower()
            #  跳过目录                        包含整季的季集要匹配                            F.O. __MACOSX
            if self._is_dir(zip_file, name) or (all_season and keyword not in decoded_name) or '__MACOSX' in name:
                continue
            weight, lang = lang_ext_weight(os.path.basename(decoded_name))
            log.debug('{} weight is {}'.format(decoded_name, weight))
            sub_dict[weight] = name + '__' + lang
        ordered_sub_dict = OrderedDict(sorted(sub_dict.items()))
        log.debug('ordered_sub_dict {}'.format(ordered_sub_dict))
        target_sub = ordered_sub_dict.popitem()[1]
        log.info('要解压的字幕：{}'.format(str(target_sub)))
        target, lang = target_sub.split('__')
        # if target:
        log.debug('要解压的字幕语言: {}'.format(lang))
        if lang:
            sub_name += '.' + lang

        f = zip_file.open(target)
        _, ext = os.path.splitext(target)
        sub_ext = ext[1:]
        sub_name = '{}.{}'.format(sub_name, sub_ext)
        log.debug('字幕名: {}'.format(sub_name))
        sub_path = os.path.join(os.path.dirname(file), sub_name)
        with open(sub_path, 'wb') as sub_f:
            sub_f.write(f.read())
        # if not isinstance(zip_file, unrar_rarfile.RarFile):
        #     zip_file.close()
        if isinstance(zip_file, zipfile.ZipFile) or isinstance(zip_file, rarfile.RarFile):
            zip_file.close()
        return sub_path

    def is_compressed(self, file):
        _, ext = os.path.splitext(file)
        return ext.lower() in self.compress_ext_list

    @staticmethod
    def _is_dir(zip_file, name):
        info = zip_file.getinfo(name)
        try:
            return info.isdir()
        except Exception as _:
            # log.debug('Catch isdir error: ' + str(e))
            try:
                return name.endswith(os.path.sep) or name.endswith(os.path.altsep)
            except Exception as _:
                pass
                # log.debug('Catch sep error: ' + str(e))


if __name__ == '__main__':
    init_log('main', logging.DEBUG)
    pass
