import pymysql

from .util import SqlUtil
from .exception import SakuraException
from .log import logger
from .models import Model


class SakuraMysql:
    def __init__(self, *args, **kwargs) -> None:
        self.conn = pymysql.connect(*args, **kwargs)

    def _sql(self, query, args):
        """获取sql语句"""
        cur = self.conn.cursor()
        return cur.mogrify(query, args)

    def insert(self, model, field_value):
        fields, _args = list(field_value.keys()), list(field_value.values())
        _fields = SqlUtil.get_fields(fields)

        _sql = SqlUtil.format_sql(
            [
                'INSERT INTO',
                f'`{model.table}`',
                f'({_fields})',
                f'VALUES ({", ".join(["%s"] * len(_args))})'
            ]
        )
        try:
            cur = self.execute(_sql, _args, True)
            if cur:
                return cur.lastrowid
            else:
                return False
        except Exception as e:
            raise SakuraException(e)

    def update(self, model, field_value, cond=None):
        _field_value, _args1 = SqlUtil.get_field_value(field_value)
        _where, _args2 = SqlUtil.get_where(cond)
        _args = _args1 + _args2
        _sql = SqlUtil.format_sql(
            [
                'UPDATE',
                f'`{model.table}`',
                'SET',
                _field_value,
                _where]
        )
        try:
            if self.execute(_sql, _args, True):
                return True
            else:
                return False
        except Exception as e:
            raise SakuraException(e)

    def delete(self, model, cond=None):
        _where, _args = SqlUtil.get_where(cond)
        _sql = SqlUtil.format_sql(
            [
                'DELETE FROM',
                f'`{model.table}`',
                _where,
            ]
        )
        try:
            cur = self.execute(_sql, _args, True)
            if cur:
                return True
            else:
                return False
        except Exception as e:
            raise SakuraException(e)

    def select(self, model, cond=None, group_by=None, order_by=None, limit=100, fields=None):
        _fields = SqlUtil.get_fields(fields)
        if not fields:
            fields = model.fields
        _where, _args = SqlUtil.get_where(cond)
        _group_by = SqlUtil.get_groupby(group_by)
        _order_by = SqlUtil.get_orderby(order_by)
        _limit = SqlUtil.get_limit(limit)
        _sql = SqlUtil.format_sql(
            [
                'SELECT',
                _fields,
                'FROM',
                f'`{model.table}`',
                _where,
                _group_by,
                _order_by,
                _limit
            ]
        )
        try:
            l = self.execute(_sql, _args)
            models = []
            for i in l:
                models.append(model(**dict(zip(fields, i))))
            return models
        except Exception as e:
            raise SakuraException(e)

    def select_one(self, model, cond=None, group_by=None, order_by=None, fields=None):
        models = self.select(model, cond, group_by, order_by, 1, fields)
        if models:
            return models[0]
        return {}

    def execute(self, query, args=None, commit=False):
        try:
            cur = self.conn.cursor()
            logger.debug('sql:%s', self._sql(query, args))
            cur.execute(query, args)
            if commit:
                self.conn.commit()
                return cur
            return cur.fetchall()
        except Exception as e:
            raise SakuraException(e)

    def execute_many(self, query, args=None):
        try:
            cur = self.conn.cursor()
            logger.debug('sql:%s', self._sql(query, args))
            cur.executemany(query, args)
            self.conn.commit()
            return cur.fetchall()
        except Exception as e:
            raise SakuraException(e)

    def getModel(self, tablename):
        fields = {
            'connection': self
        }
        sql = f'''
        select COLUMN_NAME,DATA_TYPE,IS_NULLABLE,COLUMN_KEY,COLUMN_DEFAULT,EXTRA,NUMERIC_PRECISION,NUMERIC_SCALE,CHARACTER_MAXIMUM_LENGTH,CHARACTER_OCTET_LENGTH from information_schema.COLUMNS
        where TABLE_SCHEMA = '{self.conn.db.decode()}' 
        and TABLE_NAME = '{tablename}'
        order by ORDINAL_POSITION; 
        '''
        for i in self.execute(sql):
            field_name, field_type, is_nullable, primary, default, extra, numeric_precision, numeric_scale, character_maximum_length, character_octet_length = i
            Field = SqlUtil.getField(field_type)
            fields[field_name] = Field(
                field_type,
                is_nullable=is_nullable.lower() == 'yes',
                is_primary_key=primary.lower() == 'pri',
                default=default,
                extra=extra,
                numeric_precision=numeric_precision,
                numeric_scale=numeric_scale,
                character_maximum_length=character_maximum_length,
                character_octet_length=character_octet_length
            )
        return type(tablename.title(), (Model,), fields)


def connect(*args, **kwargs):
    return SakuraMysql(*args, **kwargs)
