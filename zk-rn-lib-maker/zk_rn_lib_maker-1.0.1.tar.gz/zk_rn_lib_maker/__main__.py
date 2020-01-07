#!/usr/bin/env python3
# 编写自己的脚本
# react-native-create-library --module-prefix "@zhike-private/rn" --package-identifier "com.smartstudy.protocalview" protocal-view

import sys
import re
import os
lib_name_re = re.compile(r'^[a-z][a-z0-9|\-]*[a-z|0-9]$')


def check_lib_name(lib_name):
    return lib_name_re.match(lib_name)


def print_lib_name():
    print('''组件名称要求:
        1. 非数字开头
        2. 小写字母或数字
        3. 以中横线作为单词间的分割。
    ''')


def print_using():
    print(f'''
    {__file__} lib-name
    lib-name:
    1. 非数字开头
    2. 小写字母或数字
    3. 以中横线(-)作为单词间的分割。

    例如:
    "{__file__} protocal-view"
    将会在当前目录下创建名为protocal-view的lib库工程.
    ''')


def result_of_cmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def is_rn_create_lib_installed():
    result = result_of_cmd('npm ls react-native-create-library|grep empty')
    return len(result) == 0


def print_install_rn_create_lib():
    print('''请先安装react-native-create-library：\n
    npm install -g react-native-create-library
    ''')


def main():
    if not is_rn_create_lib_installed():
        print_install_rn_create_lib()
        return

    arg_count = len(sys.argv)
    if arg_count < 2:
        print_using()
        return

    lib_name = sys.argv[1]
    if not check_lib_name(lib_name):
        print_lib_name()
    android_id = f"com.smartstudy.{lib_name.replace('-','')}"
    cmd = f'react-native-create-library {lib_name} '\
        '--module-prefix "@zhike-private/rn" '\
        f'--package-identifier "{android_id}" '\
        f'&& rm -rf ./{lib_name}/windows'

    os.system(cmd)


if __name__ == "__main__":
    main()
