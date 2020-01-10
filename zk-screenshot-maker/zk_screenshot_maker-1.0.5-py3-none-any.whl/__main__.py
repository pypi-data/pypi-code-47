#!/usr/bin/env python3
# -*- coding: utf-8 -*- #文件也为UTF-8
import sys
import os
from ezutils.files import readjson, readlines
from cfg import safe_get, load_cfg
from using import print_using
from drawer import make_screenshot
from theme_info import load_theme_infos, safe_get


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def find_theme_infos_by_screen_shot_info(screenshot_info, theme_infos):
    screenshot_type = screenshot_type = safe_get(
        screenshot_info, 'device_type')
    device_theme = None
    similar_theme = None
    themes = []
    for theme_info in theme_infos:
        theme_type = safe_get(theme_info, "device_type")
        if theme_type == screenshot_type:
            themes.append(theme_info)
        elif theme_type == "iphone65" and screenshot_type == "iphone55":
            themes.append(theme_info)

    return themes


def main():
    param_len = len(sys.argv)

    if param_len < 2:
        print_using()
        exit()

    screenshot_dir = sys.argv[1]
    theme_infos = load_theme_infos(brother_path('theme'))

    cfgs = load_cfg(screenshot_dir)
    screenshot_index = 0
    for screenshot_info in cfgs:
        use_theme_infos = find_theme_infos_by_screen_shot_info(
            screenshot_info, theme_infos)
        for use_theme_info in use_theme_infos:
            screenshot_filename = safe_get(
                screenshot_info, "screenshot_filename")
            screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
            screenshot_info["screenshot_path"] = screenshot_path
            screenshot_info["screenshot_dir"] = screenshot_dir
            make_screenshot(screenshot_info, use_theme_info, screenshot_index)
        screenshot_index += 1


if __name__ == "__main__":
    main()
