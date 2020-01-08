from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class VuetifyTreeProcessor(Treeprocessor):
    def run(self, root):
        for elem in root:
            if elem.tag == 'h1':
                elem.set('class', 'display-4')
            elif elem.tag == 'h2':
                elem.set('class', 'display-3')
            elif elem.tag == 'h3':
                elem.set('class', 'display-2')
            elif elem.tag == 'h4':
                elem.set('class', 'display-1')
            elif elem.tag == 'h5':
                elem.set('class', 'headline')
            elif elem.tag == 'h6':
                elem.set('class', 'title')
            elif elem.tag == 'p':
                elem.set('class', 'body-1')


class PythonVuetifyMarkdown(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.add('pythonvuetifymarkdown', VuetifyTreeProcessor(), '>prettify')
