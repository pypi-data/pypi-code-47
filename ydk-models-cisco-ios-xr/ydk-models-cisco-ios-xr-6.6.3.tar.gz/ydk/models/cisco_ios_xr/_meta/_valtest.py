
'''
This is auto-generated file,
which includes metadata for module valtest
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Config.Valtest' : {
        'meta_info' : _MetaInfoClass('Config.Valtest', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('a_number', ATTRIBUTE, 'int', 'int64',
                None, None,
                [('-9223372036854775808', '9223372036854775807')], [],
                '''                ''',
                'a_number',
                'valtest', False, default_value="42"),
            _MetaInfoClassMember('b_number', ATTRIBUTE, 'int', 'int64',
                None, None,
                [('-9223372036854775808', '9223372036854775807')], [],
                '''                ''',
                'b_number',
                'valtest', False, default_value="7"),
            ],
            'valtest',
            'valtest',
            _yang_ns.NAMESPACE_LOOKUP['valtest'],
            'ydk.models.cisco_ios_xr.valtest',
        ),
    },
    'Config' : {
        'meta_info' : _MetaInfoClass('Config', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('valtest', REFERENCE_CLASS, 'Valtest', '',
                'ydk.models.cisco_ios_xr.valtest', 'Config.Valtest',
                [], [],
                '''                ''',
                'valtest',
                'valtest', False),
            ],
            'valtest',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['valtest'],
            'ydk.models.cisco_ios_xr.valtest',
        ),
    },
}
_meta_table['Config.Valtest']['meta_info'].parent =_meta_table['Config']['meta_info']
