import gitlab
import git

# url = 'https://gitlab.com'
# token = 'KaPY7CR2Fsu4dm_71Zro'

# gl = gitlab.Gitlab(url, token)


# projects = gl.projects.list(owned=True)
# for pro in projects:
#     print(pro.name, pro.ssh_url_to_repo)
# #     hook = pro.hooks.create({'url': 'http://my/action/url?project=' + pro.name, 'push_events': 1})
# #     print(hook)

# # gl.projects.create({'name': 'project1', 'namespace_id': '6883967'})


#     # print('git clone %s (%s)...' % (self.name, self.version))
#     # self.repo = git.Repo.init(self.path)
#     # origin = self.repo.create_remote(name='origin', url=http2git(self.repo_url))
#     # origin.fetch()

#     # self.repo.create_head(self.version, origin.refs.master)  # create local branch "master" from remote "master"
#     # self.repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
#     # self.repo.heads.master.checkout()  # checkout local "master" to working tree



class Repo:
    def __init__(self):
        pass

    def create_project(self, name):
        pass



class RepoGitlab(Repo):
    def __init__(self):
        Repo.__init__(self)
        url = 'https://gitlab.com'
        token = 'KaPY7CR2Fsu4dm_71Zro'

        self.gl = gitlab.Gitlab(url, token)

    def create_project(self, name, path, version):
        try:
            project = self.gl.projects.create({'name': name, 'namespace_id': '6883967'})
            print(project.name, project.ssh_url_to_repo)
        except gitlab.GitlabCreateError as e:
            print(e.error_message)
            project = self.gl.projects.get('occ-thead/'+ name)
            print(project.name, project.ssh_url_to_repo)
            # project.delete()

        repo = git.Repo.init(path)

        origin = repo.create_remote(name='origin', url=project.ssh_url_to_repo)
        repo.a
        # print(origin)
        # origin.fetch()

        # head = repo.create_head(version, origin.refs.master)  # create local branch "master" from remote "master"
        print(head)
        # repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
        # repo.heads.master.checkout()  # checkout local "master" to working tree


if __name__ == "__main__":
    repo = RepoGitlab()

    repo.create_project('xxxx', 'abc', 'master')