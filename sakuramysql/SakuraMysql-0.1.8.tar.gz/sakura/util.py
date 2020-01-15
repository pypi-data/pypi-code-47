from .exception import SakuraException
from . import fields
from .log import logger


class SqlUtil:
    @staticmethod
    def get_fields(fields):
        if not fields:
            return '*'

        if isinstance(fields, (list, tuple)):
            return f"`{'`, `'.join(fields)}`"

        raise SakuraException('fields error')

    @staticmethod
    def get_field_value(field_value):
        if field_value and isinstance(field_value, dict):
            _args = []
            fields = []
            for i in field_value.items():
                fields.append(f'`{i[0]}` = %s')
                _args.append(i[1])
            _field_value = ', '.join(fields)
            return _field_value, _args
        raise SakuraException('field_value is empty')

    @staticmethod
    def get_where(cond=None):
        """
        cond:[and_cond,or_cond]
        cond:[#or
            [#and
                ['id','=',1],
                ['status','=',1],
            ],
            [
                ...
            ]

        ]
        """
        if not cond:
            return '', []
        args = []
        for i in cond:
            args.extend(j[2] for j in i)
        where = 'WHERE ' + ' OR '.join([' AND '.join([f'`{j[0]}` {j[1]} %s' for j in i]) for i in cond])
        return where, args

    @staticmethod
    def get_groupby(group_by):
        if not group_by:
            return ''

        if isinstance(group_by, (list, tuple)):
            return f'GROUP BY `{"`, `".join(group_by)}`'

        raise SakuraException('group_by error')

    @staticmethod
    def get_orderby(order_by):
        if not order_by:
            return ''

        if isinstance(order_by, (list, tuple)):
            return f'ORDER BY `{"`, `".join(order_by)}`'

        raise SakuraException('order_by error')

    @staticmethod
    def get_limit(limit):
        if not limit:
            return ''

        if isinstance(limit, int):
            if limit == -1:
                return ''
            return f'LIMIT {limit}'

        if isinstance(limit, (list, tuple)):
            return f'LIMIT {limit[0]},{limit[1]}'

        raise SakuraException('limit error')

    @staticmethod
    def format_sql(sql):
        return ' '.join([i for i in sql if i])

    @staticmethod
    def getField(field_type: str):
        if field_type in fields.string_list:
            field = fields.BaseString
        elif field_type in fields.int_list:
            field = fields.BaseInt
        elif field_type in fields.float_list:
            field = fields.BaseFloat
        elif field_type in fields.datetime_list:
            field = fields.BaseDateTime
        else:
            logger.warning(f'This type:{field_type} is not supported,use default type:varchar')
            field = fields.BaseString
        return field
