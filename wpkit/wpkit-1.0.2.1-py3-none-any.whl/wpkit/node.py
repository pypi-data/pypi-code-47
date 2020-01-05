import re
from collections import deque

class NodeMetaClass(type):
    __not_found__='not_found'
    def __new__(cls, name, bases, attrs):
        if attrs.get('__open_node__',cls.__not_found__)==cls.__not_found__:
            attrs['__open_node__']=bases[-1].__open_node__
        if attrs.get('__node_type__',cls.__not_found__)==cls.__not_found__:
            attrs['__node_type__']=name.lower()
        return type.__new__(cls, name, bases, attrs)

def parse_selector(sel):
    s=sel
    # s = '.div.blue[name=big]  #test,div'
    res={}
    pos = 0
    while True:
        if pos >= len(s) - 1:
            break
        reg_el = re.compile("[a-zA-Z0-9]+")
        match = reg_el.match(s, pos=pos)
        if match:
            pos += len(match.group())
            res['__node_type__']=match.group()
            continue

        reg_cls = re.compile('\.[a-zA-Z0-9_\-]+')
        match = reg_cls.match(s, pos=pos)
        if match:
            pos += len(match.group())
            if '_class' in res.keys():res['_class']+=' '+match.group().lstrip('.')
            else:res['_class']=match.group().lstrip('.')
            continue

        reg_id = re.compile('#[a-zA-Z0-9_\-]+')
        match = reg_id.match(s, pos=pos)
        if match:
            pos += len(match.group())
            res['id']=match.group().lstrip('#')
            continue

        reg_attr = re.compile('\[[a-zA-Z0-9_\-]+=[a-zA-Z0-9_\-]+\]')
        match = reg_attr.match(s, pos=pos)
        if match:
            pos += len(match.group())
            k,v=match.group().lstrip('[').rstrip(']').split('=')
            res[k.strip()]=v.strip()
            continue
    return res
class Node(metaclass=NodeMetaClass):
    __indent__=' '*4
    __open_node__=True
    def __init__(self,**kwargs):
        self.__dict__['__children__'] = deque([])
        self.__dict__['__attrs__']=kwargs
    def attrs(self):
        return self.__dict__['__attrs__']
    def children(self):
        return self.__dict__['__children__']
    def append(self,item):
        self.__dict__['__children__'].append(item)
    def appendleft(self,item):
        return self.__dict__['__children__'].appendleft(item)
    def count(self, x):
        return self.__dict__['__children__'].count(x)
    def extend(self,iterable):
        return self.__dict__['__children__'].extend(iterable)
    def extendleft(self,iterable):
        return self.__dict__['__children__'].extendleft(iterable)
    def insert(self,i,x):
        return self.__dict__['__children__'].insert(i,x)
    def index(self,x,start,stop):
        return self.__dict__['__children__'].index(x,start,stop)
    def pop(self,i):
        return self.__dict__['__children__'].pop(i)
    def popleft(self):
        return self.__dict__['__children__'].popleft()
    def remove(self,value):
        return self.__dict__['__children__'].remove(value)
    def reverse(self):
        return self.__dict__['__children__'].reverse()
    def rotate(self, n: int) -> None:
        return self.__dict__['__children__'].rotate(n)
    def __getitem__(self, item):
        return self.children()[item]
    def __setitem__(self, key, value):
        return self.__dict__['__children__'].__setitem__(key,value)
    def __call__(self, *args):
        if not len(args):return self.children()
        args=list(args)
        for i in range(len(args)):
            if isinstance(args[i],str):
                s=args[i].strip()
                if s.startswith('<!--') and s.endswith('-->'):
                    args[i]=Comment(s.lstrip('<!--').rstrip('-->'))
                else:
                    args[i]=Text(s)
        self.__dict__['__children__'] = deque(args)
        return self

    def __getattr__(self, key):
        return self.__dict__['__attrs__'].get(key, None)

    def __setattr__(self, key, value):
        self.__dict__['__attrs__'][key] = value

    def set_attribute(self, key, value):
        self.__dict__[key] = value

    def get_attribute(self, *args, **kwargs):
        return self.__dict__.get(*args, **kwargs)

    def seta(self, **kwargs):
        for k, v in kwargs.items():
            self.set_attribute('__%s__' % (k), v)

    def geta(self, key, *args, **kwargs):
        return self.get_attribute('__%s__' % (key), *args, **kwargs)
    def match(self,**kwargs):
        if '__node_type__' in kwargs.keys():
            if not self.__node_type__==kwargs['__node_type__']:return False
            kwargs.pop('__node_type__')
        if '_class' in kwargs.keys():
            if (not self._class) or (not set(kwargs['_class'].split()).issubset(set(self._class.split()))):return False
            kwargs.pop('_class')
        for k,v in kwargs.items():
            if not self.__getattr__(k)==v:return False
        return True
    def find(self, sel=None,kws=None, res_list=None):
        if sel:kws=parse_selector(sel);
        if not res_list:res_list={'list':FindResult()}
        if self.match(**kws):res_list['list'].append(self)
        for ch in self.children():
            ch.find(kws=kws,res_list=res_list)
        return res_list['list']
    def __str__(self):
        return self.to_string()
    def to_string(self, depth=0):
        def to_string(ch,depth=0):
           return ch.to_string(depth=depth) if isinstance(ch,Node) else '\n'+self.__indent__*depth+str(ch)

        attrs = ' '.join(['%s="%s"' % ('class' if k == '_class' else k, v) for k, v in self.attrs().items()])
        attrs = ' ' + attrs if len(attrs) else attrs
        if self.__open_node__:
            mid='\n'+self.__indent__ * depth if len(self.__dict__['__children__']) else ''
            content=''.join([to_string(ch,depth=depth + 1) for ch in self.__dict__['__children__']])
            return '\n%s<%s%s>%s%s</%s>' % (self.__indent__ * depth,self.__node_type__,attrs,
                                               content,mid,self.__node_type__)
        else:
            return '\n%s<%s %s/>' % (self.__indent__ * depth,self.__node_type__,attrs)
    def print(self):
        print(self)

class FindResult(list):
    pass


class CloseNode(Node):
    __open_node__=False

class Text(Node):
    def __init__(self,content='',**kwargs):
        self.__dict__['content']=content
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+str(self.__dict__['content'])

class Comment(Node):
    def __init__(self, content='', **kwargs):
        self.__dict__['content'] = content
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+'<!--'+str(self.__dict__['content'])+'-->'

class Html(Node):pass
class Head(Node):pass
class Title(Node):pass
class Meta(CloseNode):pass
class Link(CloseNode):pass
class Style(Node):pass
class Script(Node):pass
class Body(Node):pass
class Div(Node):pass
class Span(Node):pass
class H(Node):pass
class P(Node):pass
class A(Node):pass
class Img(CloseNode):pass
