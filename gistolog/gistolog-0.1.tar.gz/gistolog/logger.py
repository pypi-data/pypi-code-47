from github import Github, InputFileContent

from gistolog.log import log


class Logger:
    _FILL_CHAR = '.'

    def __init__(self, token):
        self.g = Github(token)
        log.info('init GitHub api for user @{}'.format(self.g.get_user().login))
        self.gist = None
        self.name = None

    def create_gist(self, name):
        self.gist = self.g.get_user().create_gist(True, {name: InputFileContent(Logger._FILL_CHAR)})
        self.name = name
        log.info('use gist {}@{}'.format(self.name, self.gist.id))

    def use_gist(self, id):
        self.gist = self.g.get_gist(id)
        self.name = list(self.gist.files.keys())[0]
        log.info('use gist {}@{}'.format(self.name, self.gist.id))

    def log(self, log):
        content = self._get_gist_content()
        new_content = InputFileContent(content + '\n' + log)
        self._update_gist_content(new_content)

    def clear(self):
        self._update_gist_content(InputFileContent(Logger._FILL_CHAR))

    def _get_gist_content(self):
        content = list(self.gist.files.values())[0].content
        # since github gists require at least one alphanumeric character within gist content to be present while
        # creating, we remove it, replacing it with the fist line of "real" content
        if content == Logger._FILL_CHAR:
            return ''
        return content

    def _update_gist_content(self, new_content):
        self.gist.edit(files={self.name: new_content})
