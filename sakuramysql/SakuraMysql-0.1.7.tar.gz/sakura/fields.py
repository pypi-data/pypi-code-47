class Field(object):
    __slots__ = (
        'field_type',
        'convert',
        'is_nullable',
        'is_primary_key',
        'default',
        'extra',
        'numeric_precision',
        'numeric_scale',
        'character_maximum_length',
        'character_octet_length'
    )

    def __init__(self, field_type, convert, *, is_nullable=True, is_primary_key=False, default=None, extra=None, numeric_precision=None, numeric_scale=None, character_maximum_length=None, character_octet_length=None):
        self.field_type = field_type
        self.convert = convert
        self.is_nullable = is_nullable
        self.is_primary_key = is_primary_key
        self.default = default
        self.extra = extra
        self.numeric_precision = numeric_precision
        self.numeric_scale = numeric_scale
        self.character_maximum_length = character_maximum_length
        self.character_octet_length = character_octet_length

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               + f"'{self.field_type}'," \
               + f"is_nullable={self.is_nullable}," \
               + f"is_primary_key={self.is_primary_key}," \
               + f"default={self.default}," \
               + ('extra=None,' if self.extra == '' else f"extra='{self.extra}',") \
               + f"numeric_precision={self.numeric_precision}," \
               + f"numeric_scale={self.numeric_scale}," \
               + f"character_maximum_length={self.character_maximum_length}," \
               + f"character_octet_length={self.character_octet_length}" \
               + f")"


class BaseString(Field):
    def __init__(self, field_type, *args, **kwargs):
        super().__init__(field_type, str, *args, **kwargs)


class BaseInt(Field):
    def __init__(self, field_type, *args, **kwargs):
        super().__init__(field_type, int, *args, **kwargs)


class BaseFloat(Field):
    def __init__(self, field_type, *args, **kwargs):
        super().__init__(field_type, float, *args, **kwargs)


class BaseDateTime(Field):
    def __init__(self, field_type, *args, **kwargs):
        super().__init__(field_type, str, *args, **kwargs)


# 字符
string_list = [
    'char', 'varchar',
    'text', 'tinytext', 'mediumtext', 'longtext',
    'blob', 'tinyblob', 'mediumblob', 'longblob',
    'enum',
]
# 数值
int_list = [
    'int', 'integer', 'tinyint', 'smallint', 'mediumint', 'bigint',
]
# 浮点
float_list = [
    'float', 'double', 'decimal'
]
# 日期时间
datetime_list = [
    'date', 'time', 'year', 'datetime', 'timestamp',
]
