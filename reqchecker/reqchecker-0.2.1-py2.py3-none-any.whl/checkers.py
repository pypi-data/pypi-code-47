
import os
import re
from collections import Counter
from subprocess import Popen, PIPE
from github import Github
import requests
import base64

def check_sources(check_list, requirements, logger):
    """Gather requirements from all of the given sources. """

    if [*check_list.keys()][0] == "local":
        logger.info(" Will check source: local...")
        requirements = check_local(check_list, requirements, logger)

    if [*check_list.keys()][0] == "github":
        logger.info(" Will check source: github...")
        requirements = check_github(check_list, requirements, logger)

    return requirements

def check_local(check_list, requirements, logger):
    """Collect requirements from "local" source."""

    source = [*check_list.keys()][0]
    packages = [*check_list[source].keys()]

    # Gather for all packages
    for package in packages:

        location = check_list[source][package]

        # Check that location is a valid file or directory
        if not os.path.isdir(location) and not os.path.isfile(location):
            logger.error(" Given location {} not a valid directory "
                "or file".format(location))
            exit()

        req_file = os.path.join(location, 'requirements.txt')

        if os.path.isfile(req_file):
            f = open(req_file, "r")
            reqs = [x.strip() for x in f.readlines()]
            f.close()

        if os.path.isfile(location):
            f = open(location, "r")
            reqs = [x.strip() for x in f.readlines()]
            f.close()

        requirements[source][package] = reqs

    return requirements


def check_github(check_list, requirements, logger):
    """Check github."""

    source = [*check_list.keys()][0]
    packages = [*check_list[source].keys()]
    user = check_list["user"]

    gh = Github(check_list["credentials"])

    for package in packages:
        branch = check_list[source][package]
        try:
            repo = gh.get_repo("{}/{}".format(user,package))

        except:
            logger.error(" One or both of user: {}, package: {} not valid "
                "on GitHub".format(user, package))
            exit()

        try:
            repo.get_branch(branch=branch)
        except:
            logger.error(" Branch '{}' not available on "
                "{}".format(branch, package))
            exit()

        contents = repo.get_contents("requirements.txt")
        req = requests.get(contents.download_url)

        try:
            reqs = list(req.text.split('\n'))

        except:
            logger.error(" Failed accessing {} requirements.txt "
                "{}".format(package, branch))
            exit()

        requirements[source][package] = reqs

    return requirements


def print_conflicts(requirements, check_list):
    """Print package requirement conflicts to the terminal."""

    source = [*requirements.keys()][0]
    packages = [*requirements[source].keys()]
    name_only = []

    # First, get a single list of all package requirements, this will
    # duplicates if they exist
    for package in packages:

        for req in requirements[source][package]:
            name_only.append(re.sub(r"[^A-Za-z]+", '', req))

    duplicates = [k for k,v in Counter(name_only).items() if v>1]

    dash = '-'*100

    if duplicates != [] and not (len(duplicates) == 1 and duplicates[0] == ''):
        print('\n     Duplicate packages:')
        dash = '-'*100
        print(dash)

        line = ''
        for package in packages:
            if len(check_list[source][package]) > 10:
                src = '...' + check_list[source][package][-10:]
            else:
                src = check_list[source][package]

            m = '{} - {}'.format(package, src)
            line += '{:<25s}'.format(m)

        print(line)
        print(dash)
        line = ''

        # Check unique duplicates
        for dupe in list(set(duplicates)):
            dupe_list = []

            # Make list for each package
            for package in packages:
                flag = False

                # Check that package's requirements
                for req in requirements[source][package]:

                    if dupe in req and dupe != '':
                        dupe_list.append(req)
                        flag = True
                        break

                if not flag:
                    dupe_list.append(' ')

            for pkg in dupe_list:
                line += '{:<25s}'.format(pkg)

            print(line)
            line = ''

        print(dash, '\n')

    else:
        print('\n     No duplicate packages!')
        print(dash)

    # Only exact matches
    if duplicates != [] and not (len(duplicates) == 1 and duplicates[0] == ''):
        print('\n     Mismatched versions:')
        dash = '-'*100
        print(dash)

        line = ''
        for package in packages:

            if len(check_list[source][package]) > 10:
                src = '...' + check_list[source][package][-10:]
            else:
                src = check_list[source][package]

            m = '{} - {}'.format(package, src)
            line += '{:<25s}'.format(m)

        print(line)
        print(dash)
        line = ''

        # Check unique duplicates
        for dupe in list(set(duplicates)):
            dupe_list = []

            # Make list for each package
            for package in packages:
                flag = False

                # Check that package's requirements
                for req in requirements[source][package]:

                    if dupe in req and dupe != '':
                        dupe_list.append(req)
                        flag = True
                        break

                if not flag:
                    dupe_list.append(' ')

            if len(dupe_list) == len(set(dupe_list)):
                for pkg in dupe_list:
                    line += '{:<25s}'.format(pkg)

                print(line)
                line = ''

        print(dash, '\n')

    else:
        print('\n     No mismatched versions!')
        print(dash)
