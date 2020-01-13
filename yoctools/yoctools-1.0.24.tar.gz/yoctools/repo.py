import gitlab
from git import Repo


class RepoGitlab:
    def __init__(self):
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

        repo = Repo.init(path)
        # print(repo.bare)
        repo.git.add([])

        origin = repo.create_remote(name='origin', url=project.ssh_url_to_repo)
        # print(origin)
        # origin.fetch()

        head = repo.create_head(version, origin.refs.master)  # create local branch "master" from remote "master"
        # repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
        # repo.heads.master.checkout()  # checkout local "master" to working tree


if __name__ == "__main__":
    repo = RepoGitlab()

    repo.create_project('xxxx', 'abc', 'master')