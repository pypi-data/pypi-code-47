# Created by by Bart Cox - 2019
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import git
import os
from pathlib import Path
import click


def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()


def ensure_path(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]


def get_branch_name(branch):
    # print(branch)
    if len(branch.split('->')) is 2:
        branch = branch.split('->')[1]
    return branch.split('origin/')[1].strip(), branch.strip()


def clone_branch(url, branchName, branch, root_dir, progress):
    print('%s Cloning branch \'%s\'' % (progress, branchName))
    try:
        git.Repo.clone_from(url, os.path.join(root_dir, branchName), branch=branchName)
    except:
        rmdir(Path(os.path.join(root_dir, branchName)))
        git.Repo.clone_from(url, os.path.join(root_dir, branchName), branch=branchName)


@click.command()
@click.option('-d', '--target-dir',
              default='./repos',
              show_default=True,
              help="Target directory to run the command from")
@click.option('-c', '--cache-dir',
              default='./.cache',
              show_default=True,
              help="Cache directory")
@click.argument('url')
def main(target_dir, cache_dir, url):
    """
    Clones all the branches of a git repository using the given url.
    It uses the local ssh key of the current user to authenticate while running git commands.
    """
    print('Fetching from %s' % url)
    repo_name = get_repo_name_from_url(url)
    cache_master_dir = os.path.join(cache_dir, repo_name)
    target_repo_dir = os.path.join(target_dir, repo_name)

    ensure_path(target_repo_dir)
    ensure_path(cache_dir)

    try:
        git.Git(cache_dir).clone(url)
    except:
        pass
    r = git.Repo(cache_master_dir)
    cleanBranchNames = list(set([get_branch_name(r) for r in r.git.branch('-r').split('\n')]))
    numberOfBranches = len(cleanBranchNames)
    print('Found %i branches' % numberOfBranches)
    for idx, branch in enumerate(cleanBranchNames):
        progress_str = '[' + (' '*(len(str(numberOfBranches)) - len(str(idx+1)))) + str(idx+1) + '/' + str(numberOfBranches) + ']'
        clone_branch(url, branch[0], branch[1], target_repo_dir, progress_str)


if __name__ == '__main__':
    main()