
from .matcher import apply_match


class TypeActor():

    def from_int(obj):
        i = int(obj)
        j = i + 2
        res = f'original {i}, new {j}'  
        err = None
        return res, err

    def from_dict(obj):
        kvs = list(obj.items())
        res = f'items = {kvs}'
        err = None
        return res, err


    def default_func(obj):
        err = f'mismatch: expected int or dict: unknown arr type {type(obj)}'
        return None, err

    type2action = {
        int: from_int,
        dict: from_dict
    }

    @classmethod
    def add_action(cls, klass, func):
        assert klass not in cls.type2action
        cls.type2action[klass] = func



if __name__ == '__main__':
    actor = TypeActor()
    res, err = apply_match(TypeActor, 3)
    print (res)
    res, err = apply_match(TypeActor, {'a': 1, 'b': 2})
    print (res)
    res, err = apply_match(TypeActor, [1, 2, 3])
    print (err)











