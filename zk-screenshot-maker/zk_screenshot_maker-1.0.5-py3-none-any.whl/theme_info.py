#!/usr/bin/env python3
import os
from ezutils.files import readjson


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def safe_get(from_map, with_key, default=''):
    if from_map.__contains__(with_key):
        return from_map[with_key]
    else:
        return default


def get_infos(cfg, key):
    if not cfg.__contains__(key):
        return []

    infos = cfg[key]
    infos['device_type'] = key
    return infos


def load_theme_infos(theme_dir):
    cfg = readjson(f"{theme_dir}/info.json")
    # print(f"cfg from file:{cfg}")
    iphone65 = get_infos(cfg, "iphone65")
    iphone55 = get_infos(cfg, "iphone55")
    ipad_infos = get_infos(cfg, "ipad")
    return [ipad_infos, iphone65, iphone55]
