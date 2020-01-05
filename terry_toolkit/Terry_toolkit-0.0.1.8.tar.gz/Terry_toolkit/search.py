# -*- coding:utf-8 -*-
import os,json
from whoosh.qparser import QueryParser
from whoosh.index import create_in,open_dir
from whoosh.sorting import FieldFacet
from whoosh.fields import *
from whoosh.filedb.filestore import FileStorage
from jieba.analyse import ChineseAnalyzer

import Terry_toolkit as tkit

class Search:
    def __init__(self,name='Terry'):
        # 存储schema信息至'indexdir'目录下
        self.ix_path = 'indexdir/'
        self.ix_name = name

        pass
    def init_search(self):
        # 导入中文分词工具
        analyzer = ChineseAnalyzer()
        # 创建索引结构  stored为True表示能够被检索
        #https://www.osgeo.cn/whoosh/quickstart.html#the-index-and-schema-objects
        self.schema = Schema(
            title=TEXT(stored=True, analyzer=analyzer),
            path=TEXT(stored=True),
            id=ID(unique=True),
            content=TEXT(stored=True, analyzer=analyzer),
            # phone_name=TEXT(stored=True, analyzer=analyzer),
            # price=NUMERIC(stored=True),
            # phoneid=ID(stored=True)
        )

        if not os.path.exists(self.ix_path):
            os.mkdir(self.ix_path)
        # ix_path 为索引创建的地址，indexname为索引名称
        self.ix = create_in(self.ix_path, schema=self.schema, indexname=self.ix_name)
     
        # self.ix = self.storage.open_index(indexname=self.ix_name)
    def load(self):
        self.storage = FileStorage(self.ix_path)  # idx_path 为索引路径
        self.ix = self.storage.open_index(indexname=self.ix_name)



    def add(self,data):
        """
           data=[{'title'="www','content':'w2323','path':'https://www.osgeo.cn/whoosh/batch.html'}]

        """
        self.load()
        ttext=tkit.Text()
        # # ---------------------------------创建索引-------------------------------------

        # writer = self.ix.writer()
        # writer.add_document(phone_name='name', price=1, phoneid="id")  # 此处为添加的内容
        # print("建立完成一个索引")
        # writer.commit()
        # -----------------------------增加索引 -----------------------------------------
        # 增加索引   操作索引的行为，类似读写文件，需要用完close，或者使用with语句。
        # 按照schema定义信息，增加需要建立索引的文档，注意：字符串格式需要为unicode格式
        with self.ix.writer() as w:
            # from whoosh.writing import AsyncWriter
            # writer = AsyncWriter(ix,delay=0.25)
            for item in data:
                # print('item',item)
                text =str(item['title'])+str(item['content'])+str(item['path'])
                id=str(ttext.md5(text))
                # print('id',id)

                # string="在python存入数据库时，如果数据库的主键不是自增方式，那么我们可能需要自己生成一个唯一标识符，现在最好的方法就是md5加密生成的32位作为主键，本文将会介绍python的两种自动生成唯一标识的方式。"
                # print(ttext.md5(string))
                w.update_document(title=item['title'], path=item['path'],id=id,content=item['content'])
                # w.commit()
                # text="niudeeaswew" 
                # try:
                #     w.update_document(title=item['title'], path=item['path'],id=id,content=item['content'])
                 
                # except:
                #     print("add失败")
                #     pass
                # # w.add_document(title=u"第二篇文档，呵呵", path=u"/b", content=u"这是我们增加的第二篇文档，哈哈")
                # # w.add_document(title=u"帅哥，呵呵", path=u"/b", content=u"帅哥，哈哈")
            try:
                w.update_document()
                # w.commit()
            except:
                print("更新失败")
                pass
            
            # w.commit()
            # w.delete_document()

        # ix.close()

    def find(self,keyword):
        print("开始检索")
        self.load()
        #---------------------------------检索展示-----------------------------------------------
        with self.storage.open_index(indexname=self.ix_name).searcher() as searcher:
            # print("kais")
            # query = MultifieldParser(["symbol", "co_name"], ix.schema， group=syntax.OrGroup)
            # 检索标题中出现'文档'的文档
            results = searcher.find(u"content",keyword)
            # results = searcher.find(u"title",keyword,u"content",keyword)
            # 检索出来的第一个结果，数据格式为dict{'title':.., 'content':...}
            data=[]
            for r in results:
                # display(HTML('<h3>' + r.get('title') + '</h3>'))
                # display(HTML(r.highlights("content")))  # 高亮标题中的检索词
                # print(r.get('title'))
                # print(r.get('content'))
                # print(r.score)  # 分数
                # print(r.docnum)
                # print(r)
                one={'title':r.get('title'), 'content':r.get('content'),'path':r.get('path'),'score':r.score,'docnum':r.docnum}
                data.append(one)
            return data


                # doc = r.fields()
                # jsondoc = json.dumps(doc, ensure_ascii=False)
                # # display(jsondoc)  # 打印出检索出的文档全部内容
                # print(jsondoc)

        # #--------------------------------------------------------------------------------
        # new_list = []
        # index = open_dir(dirname=ix_path, indexname=ix_name)  # 读取建立好的索引
        # with index.searcher() as searcher:
        #     parser = QueryParser("要搜索的项目，比如“phone_name", index.schema)
        #     myquery = parser.parse("搜索的关键字")
        #     facet = FieldFacet("price", reverse=True)  # 按序排列搜索结果
        #     # limit为搜索结果的限制，默认为10
        #     results = searcher.search(myquery, limit=None, sortedby=facet)
        #     for result1 in results:
        #         print(dict(result1))
        #         new_list.append(dict(result1))
    def find_title(self,keyword):
        print("开始检索")
        self.load()
        #---------------------------------检索展示-----------------------------------------------
        with self.storage.open_index(indexname=self.ix_name).searcher() as searcher:
            # print("kais")
            # query = MultifieldParser(["symbol", "co_name"], ix.schema， group=syntax.OrGroup)
            # 检索标题中出现'文档'的文档
            results = searcher.find('title',keyword)
            # 检索出来的第一个结果，数据格式为dict{'title':.., 'content':...}
            data=[]
            for r in results:
                # display(HTML('<h3>' + r.get('title') + '</h3>'))
                # display(HTML(r.highlights("content")))  # 高亮标题中的检索词
                # print(r.get('title'))
                # print(r.get('content'))
                # print(r.score)  # 分数
                # print(r.docnum)
                # print(r)
                one={'title':r.get('title'), 'content':r.get('content'),'path':r.get('path'),'score':r.score,'docnum':r.docnum}
                data.append(one)
 

            return data
    def all(self):
        """
        所有
        """
        self.load()
        all_docs = self.ix.searcher().documents()
        for doc in all_docs:
            yield doc
# s=Search()
# # s.init_search()
# data=[{'title':'www','content':'223这是我们增加搜索的s第武器篇文档，哈哈 ','path':'https://www.osgeo.cn/whoosh/batch.html'}]
# s.add(data)
# print(s.find('宠物'))
# # print(s.find('文档'))
