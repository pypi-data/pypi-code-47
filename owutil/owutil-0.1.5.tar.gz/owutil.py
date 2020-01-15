import click
import os
import subprocess


def validateParams(version, tag):
    tag_type, tag_version_number = tag.split("/")
    os.system("git fetch --all")
    os.system("git pull --all")
    os.system("git branch --track {tag_name} origin/{tag_name}".format(tag_name=tag))
    path = os.path.join(os.getcwd(), ".git", "refs", "heads", tag_type)
    try:
        branches = os.listdir(path)
    except FileNotFoundError as e:
        print("{} not found in your git branches".format(tag))
        exit()
    if (version not in ["major", "minor", "patch"]):
        print("Error: Invalid choice: {}. (choose from major, minor, patch)".format(version))
        exit()
    if (tag_version_number not in branches):
        print("Current {} is not in your git versions".format(tag))
        exit()
    

@click.group()
def main():
    """ 
        Merge branches
    """
    pass

@main.command()
@click.argument("tag")
@click.argument("version")
def merge(tag, version):
    print("Starting merge")
    tag_type, tag_version_number = tag.split("/")
    validateParams(version, tag)
    os.system("git checkout master")
    os.system("git pull origin master")
    os.system("git merge {}".format(tag))
    os.system("npm version {}".format(version))
    os.system("git push origin master")
    os.system("git branch -d {}".format(tag))


if __name__=="__main__":
    main()
