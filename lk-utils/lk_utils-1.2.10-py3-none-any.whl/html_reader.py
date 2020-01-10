"""
DEL: this module is going to be removed.
"""
from lxml import etree


class HTML():
    """
    REF:
        http://www.zvon.org/xxl/XPathTutorial/General_chi/examples.html
    """
    
    def __init__(self, html, ftype='file'):
        if ftype == 'file':
            from .read_and_write import read_file
            html = read_file(html)
        self.dom = etree.HTML(html)
    
    def find(self, path):
        pass
    
    def xpath(self, path):
        pass
    
    
def find_following_siblings(node, q, snippet=False):
    """
    ARGS:
        node
        q
        snippet:
            假设:
                tree:
                    <AAA/>  # <- e1 (focus)
                    <BBB/>  # <- e2
                    <BBB/>  # <- e3
                    <CCC/>  # <- e4
                    <BBB/>  # <- e5
                q = './following-sibling::BBB'
            则有:
                snippet = True: 获取 e1 下面的, 同级的且连续的 BBB 标签.
                    -> [e2, e3]
                snippet = False: 获取 e1 下面的, 同级的所有 BBB 标签.
                    -> [e2, e3, e5]
    """
    elements = node.xpath(q)
    if snippet:
        stub = elements[0].name
        for index, e in enumerate(elements):
            if e.name != stub:
                return elements[:index]
    return elements
