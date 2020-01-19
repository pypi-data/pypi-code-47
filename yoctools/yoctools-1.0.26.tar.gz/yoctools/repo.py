#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import shutil
import github
import gitlab
import git


class simpleProgressBar(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        # text = "%3d%% (%d/%d)" % (cur_count/(max_count or 100.0), cur_count, max_count)
        sys.stdout.write(self._cur_line)
        sys.stdout.flush()
        if op_code & self.END:
            sys.stdout.write('\n')
        else:
            sys.stdout.write('\r')


class pullProgressBar(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        sys.stdout.write(self._cur_line)
        sys.stdout.flush()
        if op_code & self.END:
            sys.stdout.write('\n')
        else:
            sys.stdout.write('\r')


class GitProject:
    def __init__(self, repo_url, path, version):
        self.repo_url = repo_url
        self.path = path
        self.version = version
        git_path = os.path.join(path, '.git')

        if not os.path.exists(git_path):  # 如果未下载，则 git clone 下来
            self.repo = git.Repo.init(path)
        else:
            self.repo = git.Repo(path)

    def pull(self, progress=pullProgressBar()):
        origin = None
        for remote in self.repo.remotes:
            if remote.url == self.repo_url:
                origin = remote
        if not origin:
            origin = self.repo.create_remote(name='origin', url=self.repo_url)

        if self.version not in self.repo.heads:
            if self.version not in origin.refs:
                origin.fetch(progress=progress)
            if self.version in origin.refs:
                branch = self.repo.create_head(
                    self.version, origin.refs[self.version])
                branch.checkout()
            elif self.version in self.repo.tags:
                branch = self.repo.create_head(
                    self.version, self.repo.tags[self.version])
                branch.checkout()

    def push(self, path):
        files = os.listdir(self.repo.working_dir)
        for f in files:
            if f != '.git':
                fn = os.path.join(self.repo.working_dir, f)
                if os.path.isdir(fn):
                    shutil.rmtree(fn)
                else:
                    os.remove(fn)

        for dirpath, _, filenames in os.walk(path):
            if dirpath.find(os.path.join(path, '.git')) < 0:
                for f in filenames:
                    p1 = os.path.join(dirpath, f)
                    p2 = os.path.relpath(p1, path)
                    p2 = os.path.join(self.repo.working_dir, p2)
                    try:
                        p = os.path.dirname(p2)
                        os.makedirs(p)
                    except:
                        pass

                    shutil.copy2(p1, p2)

        if self.repo.is_dirty(untracked_files=True):
            self.repo.git.add(self.repo.untracked_files)
            self.repo.git.commit('-m', 'init version', '-a')

            branch = self.repo.create_head(self.version)
            branch.checkout()

            self.repo.git.push(
                "--set-upstream", self.repo.remotes.origin, self.repo.head.ref)


class RepoGithub:
    def __init__(self, token=None):
        self.gl = github.Github(token, timeout=30)
        self.organization = self.gl.get_organization('yoc-components')

    def projects(self):
        for repo in self.organization.get_repos():
            print(repo.name, repo)
        # projects = self.gl.projects.list(owned=True, all=True, namespace_id='6883967')
        # for p in projects:
        #     print(p.name, p.ssh_url_to_repo)

    def create_project(self, name, path, version):
        try:
            project = self.organization.create_repo(name)
            ssh_url = project.ssh_url
        except github.GithubException as e:
            ssh_url = 'git@github.com:yoc-components/' + name + '.git'
            # print(e)
        prj = GitProject(ssh_url, '/tmp/' + name, version)
        prj.pull()
        prj.push(path)
        shutil.rmtree('/tmp/' + name)

    def branch_to_tag(self, name, branch, tag_name):
        project = self.organization.get_repo(name)
        print(project)

        for tag in project.get_tags():
            if tag.name == tag_name:
                return

        for br in project.get_branches():
            if br.name == branch:
                print(br)
                tag = project.create_git_tag(
                    tag_name, 'Created from tag %s' % br.name, br.commit.sha, 'commit')
                if tag:
                    project.create_git_ref('refs/tags/%s' % tag_name, tag.sha)
                break


class RepoGitlab:
    def __init__(self):
        url = 'https://gitlab.com'
        token = 'KaPY7CR2Fsu4dm_71Zro'

        self.gl = gitlab.Gitlab(url, token)

    def projects(self):
        repo = git.Repo('.')

        projects = self.gl.projects.list(
            owned=True, all=True, namespace_id='6883967')
        for p in projects:
            print(p.name, p.ssh_url_to_repo)

    def projects_xxx(self):
        repo = git.Repo('.')

        projects = self.gl.projects.list(owned=True, namespace_id='6883967')
        for p in projects:
            if p.name not in ['yoc', ]:
                repo.git.submodule(
                    'add', '--force', p.ssh_url_to_repo, 'components/' + p.name)
            print(p.name, p.ssh_url_to_repo)

    def download(self, name, path, version):
        try:
            project = self.gl.projects.get('occ-thead/' + name)
            print(project.name, project.ssh_url_to_repo)
            self.clone(project.ssh_url_to_repo, path, version)
        except gitlab.GitlabGetError as e:
            print(e.error_message)
            return

    def create_project(self, name, path, version):
        try:
            project = self.gl.projects.create(
                {'name': name, 'namespace_id': '6883967'})
            prj = GitProject('git@github.com:yoc-components/aos.git',
                             os.path.join('tmp', path), 'v7.2-dev')
            prj.upload(path)
        except gitlab.GitlabCreateError as e:
            print(e.error_message)
            project = self.gl.projects.get('occ-thead/' + name)
            print(project.name, project.ssh_url_to_repo)
