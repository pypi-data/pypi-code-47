#!/usr/bin/env python3
from ezutils.files import readjson, writelines
import os
import sys
import shutil


def safe_get(from_map, with_key, default=''):
    if from_map.__contains__(with_key):
        return from_map[with_key]
    else:
        return default


def get_infos(cfg, key):
    if not cfg.__contains__(key):
        return []

    infos = cfg[key]
    new_info = []
    for info in infos:
        info["device_type"] = key
        new_info.append(info)
    return new_info


def load_cfg(screen_shot_dir):
    cfg = readjson(f"{screen_shot_dir}/cfg.json")
    iphone_infos = get_infos(cfg, "iphone55")
    ipad_infos = get_infos(cfg, "ipad")
    return ipad_infos+iphone_infos


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def gen_default_cfg(screen_shot_dir):
    dst_file_name = os.path.join(screen_shot_dir, 'cfg.json.default')
    src_file_name = brother_path("cfg.temple.json")
    shutil.copyfile(src_file_name, dst_file_name)


def print_using():
    print("Give me a screen_shot_dir to put the 'cfg.json.default'.")


if __name__ == "__main__":
    param_len = len(sys.argv)

    if param_len < 2:
        print_using()
        exit()

    screenshot_dir = sys.argv[1]

    gen_default_cfg(screenshot_dir)
