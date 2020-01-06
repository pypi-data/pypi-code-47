import random

from data import data

def produceComments(_type="好评", _class="鞋子", filename="data.json"):
    """
    :param _type: 好评 或者 差评
    :param _class: 商品类目，例如：鞋子
    """
    try:
        comments = data.datas[_type]
        return (random.choice(comments["开始"]) + random.choice(comments["中间"]) + random.choice(comments["结束"])).replace("$", _class)
    except Exception as e:
        print("{} 文件找不到，请放在main的同目录下！".format(e))
    

if __name__ == "__main__":
    produceComments(_type="好评", _class="手机")