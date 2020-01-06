# -*- coding: utf-8 -*-


import argparse
import datetime

import git
from flask import Flask, request

from candypi import check_directory


parser = argparse.ArgumentParser()
parser.add_argument('arg1', help='the full path of the git directory')
parser.add_argument('-b', '--branch', default='master', help='target branch (Default is the master)')
parser.add_argument('-p', '--port', default=50000, type=int, help='port')
args = parser.parse_args()


app = Flask(__name__)


def print_candypi(text):
    dt_now = datetime.datetime.now()
    print('[CanDyPi] {time} {statement}'.format(time=dt_now.strftime('%Y-%m-%d %H:%M:%S'), statement=text))


@app.route('/', methods=['POST'])
def gitpull():
    data = request.get_json()
    ref = data.get('ref')
    
    target_branch = args.branch

    if ref.find(target_branch) > 0:
        git_repo.git.checkout(target_branch)
        git_repo.git.pull()
        print_candypi('RUN pull command')
        return 'complete pull action'
    else:
        return 'not target branch'


def main():
    global git_repo
    git_repo = git.Repo(check_directory(args.arg1))

    target_branch = args.branch
    print_candypi('target branch is {}'.format(target_branch))

    app.run(port=args.port, debug=False)


if __name__ == '__main__':
    main()
