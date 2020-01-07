# -*- coding: utf-8 -*-
import git
import re
import sys
import argparse


def print_release_doc(prev, head):
    repo = git.Repo(get_git_root('./'))
    lines = []
    for item in repo.iter_commits(prev + '..' + head, min_parents=2):
        if ('Merged in' in item.message and 'pull request #' in item.message and 'Approved-by:' in item.message) or ('Merge pull request #' in item.message):
            message = item.message.splitlines()[2]
            result = re.search('#\d+', item.message.splitlines()[0])
            pullreq_no = result.group()[1:]
            author = item.author.name
            if sys.version_info.major == 2:
                message = message.encode('utf-8')
                author = author.encode('utf-8')
            lines.append(
                '- [{0}](https://bitbucket.org/uzabase/newspicks-server/pull-requests/{1}) @{2}'.format(message,
                                                                                                        pullreq_no,
                                                                                                        author))

    GREEN = '\033[34m'
    END = '\033[0m'
    print(GREEN + prev + '..' + head + END)
    for line in lines:
        print(line)
    print('\n')


def get_git_root(path):
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def main():
    parser = argparse.ArgumentParser(description='display commit message',
                                     usage='reldoc [--max-count=<num> | -m=<num>]')
    parser.add_argument('-m', '--max-count', action='store', help='maximum number of tags to display. default is 2')
    args = parser.parse_args()
    max_count = 1 if args.max_count is None else int(args.max_count)

    g = git.Git('./')
    tags = g.execute(['git', 'tag', '--sort=-taggerdate']).splitlines()
    prev = ''
    head = 'HEAD'
    for i, tag in enumerate(tags):
        prev = tag
        print_release_doc(prev, head)
        head = prev
        if i >= max_count - 1:
            break


if __name__ == '__main__':
    main()
