# -*- coding:utf-8 -*-
import re
import argparse
d = {"#": 1, "##": 2, "###": 3, "####": 4, "#####": 5, "######": 6}
pattern = '#+\s'


def gan_menu(filename):
    headId = 0
    targetname = filename.split('.')[0] + "_bak.md"
    with open(targetname, 'w+') as f2:
        with open(filename, 'r') as f:
            for i in f.readlines():
                if not re.match(pattern, i.strip(' \t\n')):
                    continue
                i = i.strip(' \t\n')
                head = i.split(' ')[0]
                f2.write(' ' * (len(head) - 1) + '- ' +
                         '[' + i[len(head):].strip(' \t\n') + '](#id' + str(headId) + ')   \n')
                headId += 1
        headId = 0
        with open(filename, 'r') as f:
            for i in f.readlines():
                if not re.match(pattern, i.strip(' \t\n')):
                    f2.write(i)
                else:
                    i = i.strip(' \t\n')
                    head = i.split(' ')[0]
                    if head in list(d.keys()):
                        menu = ''.join(['<h', str(len(head)), ' id=id', str(headId), '>', i[
                                       len(head):].strip(' \t\n'), '</h', str(len(head)), '>   \n'])
                        f2.write(menu)
                        f2.write('\n')
                        headId += 1


if __name__ == '__main__':
    description = """
    Generate markdown Menu automatically/自动生成markdown 目录
    Eg:
        norepeat gen_markdown_menu -n=sample.md  
    then you will get a sample_back.md with contents
    sample_back.md is new generated file including menu
    """

    parser = argparse.ArgumentParser(description=description,
                                     prog='gen_markdown_menu',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     )
    parser.add_argument('-n', '--name', help='file name')
    args = parser.parse_args()

    try:
        gan_menu(args.name)
    except Exception as e:
        print(str(e))