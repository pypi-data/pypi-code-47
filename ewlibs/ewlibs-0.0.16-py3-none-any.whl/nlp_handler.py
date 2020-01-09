import re
import jieba.posseg as jp, jieba
import os
sys.path.append(os.getcwd())
from ewlibs.char_handler import is_other


class Pre_Process:
    #文档-正则剔除
    @staticmethod
    #re_list格式[(pattern,replace_str)...]
    def doc_regular(re_list):
        def decorator(fn):
            def objectMethod(
                    doc,
                    corpus,
                    *args,
            ):
                # print(f"doc_regular")
                for pattern, replace_str in re_list:
                    doc = re.sub(pattern, replace_str, doc)
                #执行方法
                return fn(
                    doc,
                    corpus,
                    *args,
                )

            return objectMethod

        return decorator

    #文档-去掉符号
    @staticmethod
    def doc_remchar():
        def decorator(fn):
            def objectMethod(
                    doc,
                    corpus,
                    *args,
            ):
                # print(f"doc_remchar")
                datas = doc.split("\n")
                temp_lines = []
                for line in datas:
                    temp_line = []
                    for char in line:
                        if is_other(char):
                            temp_line.append(" ")
                        else:
                            temp_line.append(char)
                    temp_lines.append(
                        re.sub(
                            ' +',
                            ' ',
                            "".join(temp_line).strip(),
                        ))
                doc = "\n".join(temp_lines)
                #执行方法
                return fn(
                    doc,
                    corpus,
                    *args,
                )

            return objectMethod

        return decorator

    #文档-大小写转换
    @staticmethod
    def doc_lower():
        def decorator(fn):
            def objectMethod(
                    doc,
                    corpus,
                    *args,
            ):
                # print(f"doc_remchar")
                doc = str(doc).lower()
                #执行方法
                return fn(
                    doc,
                    corpus,
                    *args,
                )

            return objectMethod

        return decorator

    #文档-分词
    #https://blog.csdn.net/jdjh1024/article/details/81318635
    @staticmethod
    def doc_cut(
            method="jieba",
            flags=None,
    ):
        def decorator(fn):
            def objectMethod(
                    doc,
                    corpus,
                    *args,
            ):
                # print(f"doc_cut")
                corpus = None
                #需要词性分析
                if flags:
                    corpus = [
                        word.word for word in jp.cut(doc) if word.flag in flags
                    ]
                else:
                    corpus = [item for item in jieba.cut(doc)]
                #执行方法
                return fn(
                    doc,
                    corpus,
                    *args,
                )

            return objectMethod

        return decorator

    #语料-去除停用词
    @staticmethod
    def corpus_stopwords(filename):
        def decorator(fn):
            def objectMethod(
                    doc,
                    corpus,
                    *args,
            ):

                with open(filename, "r") as f:
                    stopwords = [line.strip() for line in f.readlines()]
                # print(f"corpus_stopwords before:{len(corpus)}")
                #去除停用词
                corpus = [item for item in corpus if item not in stopwords]
                # print(f"corpus_stopwords after:{len(corpus)}")
                #函数调用
                return fn(
                    doc,
                    corpus,
                    *args,
                )

            return objectMethod

        return decorator
