import abc

from .fields import Field


class ModelMetaclass(abc.ABCMeta):
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            return super().__new__(mcs, name, bases, attrs)
        fields = dict()
        pk = []
        for k, v in attrs.items():
            if isinstance(v, Field):
                if v.is_primary_key:
                    pk = k
                fields[k] = v
        for k in fields.keys():
            attrs.pop(k)
        attrs['primary_key'] = pk
        attrs['fields'] = fields  # 保存属性和列的映射关系
        attrs['table'] = name.lower()  # 假设表名和类名一致
        return super().__new__(mcs, name, bases, attrs)
