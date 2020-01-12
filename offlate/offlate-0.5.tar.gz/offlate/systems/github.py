#   Copyright (c) 2018 Julien Lepiller <julien@lepiller.eu>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
####
""" The gitlab system connector. """

from .git import GitProject

from urllib.parse import urlparse
from github import Github
from pathlib import Path

class GithubProject(GitProject):
    def __init__(self, conf, name, lang, data = {}):
        GitProject.__init__(self, conf, name, lang, data)

    def updateURI(self):
        repo = self.data['repo']
        if repo.startswith('https://github.com/'):
            self.uri = repo
        elif repo.startswith('github.com/'):
            self.uri = 'https://' + repo
        else:
            self.uri = 'https://github.com/' + repo
        self.branch = self.data['branch']

    def send(self, interface):
        gh = Github(self.conf['token'])

        currentUser = gh.get_user().login
        projectname = self.uri.split('/')[-1]
        projectfullname = urlparse(self.uri).path[1:]

        originproject = gh.get_repo(projectfullname)
        try:
            project = gl.get_repo(currentUser + "/" + projectname)
        except:
            project = gh.get_user().create_fork(originproject)

        try:
            sha = project.get_git_ref('heads/' + self.data['branch']).object.sha
            project.create_git_ref('refs/heads/translation', sha)
        except:
            interface.githubBranchError('translation')
            return

        translationfiles = []
        for mfile in self.translationfiles:
            translationfiles.extend(mfile['format'].translationFiles())

        for mfile in translationfiles:
            mfile = mfile[len(self.basedir + '/current/'):]
            try:
                # workaround a bug, where we cannot get the content hash of a single file, by looking
                # for every file in the parent directory.
                contents = project.get_dir_contents(str(Path(mfile).parent), ref='translation')
                for c in contents:
                    if c.path == mfile:
                        sha = c.sha
                        break
                project.update_file(path=mfile, message='Update ' + self.lang + ' translation',
                        content=open(self.basedir + '/current/' + mfile).read(),
                        sha=sha, branch='translation')
            except:
                project.create_file(path=mfile, message='Add ' + self.lang + ' translation',
                        content=open(self.basedir + '/current/' + mfile).read(),
                        branch='translation')
        originproject.create_pull(title='Update ' + self.lang + ' translation',
                body='Automatically submitted using Offlate. Report translation issues to the submitter, and Offlate issues to @roptat, thanks!',
                head=currentUser+':translation',
                base=self.data['branch'],
                maintainer_can_modify=True)

    @staticmethod
    def isConfigured(conf):
        res = GitProject.isConfigured(conf)
        res = res and 'token' in conf and conf['token'] != ''
        return res
