#!/usr/bin/env python

import argparse
import subprocess


def main():
    services = {}
    try:
        from pullrequest import gitlab
        services['gitlab'] = gitlab.create
    except ImportError:
        pass
    try:
        from pullrequest import github
        services['github'] = github.create
    except ImportError:
        pass
    try:
        from pullrequest import bitbucket_cloud
        services['bitbucket'] = bitbucket_cloud.create
    except ImportError:
        pass
    default_service = next(iter(services))

    try:
        current_branch = str(subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']))
        if ' ' in current_branch:
            current_branch = None
    except subprocess.CalledProcessError:
        current_branch = None

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Create pullrequest to git service')
    parser.add_argument('--key', help='private key/token or oauth2 client id')
    parser.add_argument('--secret', help='oauth secret')
    parser.add_argument('--head', default=current_branch, help='Name of args.head branch that is the source of changes')
    parser.add_argument('--base', default='master', help='Name of base branch that is the target of changes')
    parser.add_argument('--title')
    parser.add_argument('--description')
    parser.add_argument('--repository', help='Repository or project slug / name')
    parser.add_argument('--reviewer', nargs='+', help='Users that should be set as reviewer or assignee')
    parser.add_argument('--label', nargs='+', help='Labels to apply (not supported by all services)')
    parser.add_argument('--url', help='Url of the service (not supported by all services)')
    parser.add_argument('--close_source_branch', action='store_true',
                        help='Close source branch on merge (not supported by all services)')
    parser.add_argument('--commit', action='store_true', help='Commit all changes')
    parser.add_argument('--remote', default='origin', help='Name of remote repo to push to')
    parser.add_argument('--service', help=', '.join(services.keys()))
    args = parser.parse_args()

    if not args.service:
        try:
            remote_url = str(subprocess.check_output(['git', ' remote', 'get-url', '--push', args.remote]))
        except subprocess.CalledProcessError:
            remote_url = None
        if not args.service:
            args.service = default_service
            if not args.url:
                args.url = 'https://gitlab.com/'
        elif remote_url:
            for service in services.keys():
                if service in remote_url:
                    args.service = service
            if not args.service:
                args.service = default_service

    print('Using service <{}>'.format(args.service))

    if args.head:
        if current_branch != args.head:
            print('Creating branch <{}>'.format(args.head))
            subprocess.check_call(['git', 'checkout', '-b', args.head])
    else:
        args.head = current_branch
    assert args.head and args.head != args.base

    if args.commit:
        print('Committing changes')
        subprocess.check_call(['git', 'commit', '-A', '.', '-m', args.title])
    elif not args.title:
        try:
            args.title = subprocess.check_output(['git', 'log', '-1', '--pretty=%B'])
        except subprocess.CalledProcessError:
            pass

    print('Pushing branch <{}> to remote <{}>'.format(args.head, args.remote))
    subprocess.check_call(['git', 'push', '-u', args.remote, args.head])

    print('Creating pull request')
    create = services[args.service]
    create(**vars(args))


if __name__ == '__main__':
    main()
