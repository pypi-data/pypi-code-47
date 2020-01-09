
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_vm_mgr
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'VM.AllLocations.AllUiids' : {
        'meta_info' : _MetaInfoClass('VM.AllLocations.AllUiids', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('uiid', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Unique Immutable ID
                ''',
                'uiid',
                'Cisco-IOS-XR-sysadmin-vm-mgr', True, is_config=False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ID of the VM
                ''',
                'id',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Status of the VM
                ''',
                'status',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            _MetaInfoClassMember('ipaddr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                CE IP address
                ''',
                'ipaddr',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            _MetaInfoClassMember('last_hb_sent', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Last heartbeat sent
                ''',
                'last_hb_sent',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            _MetaInfoClassMember('last_hb_rec', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Last heartbeat received
                ''',
                'last_hb_rec',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-vm-mgr',
            'all-uiids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm-mgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr',
            is_config=False,
        ),
    },
    'VM.AllLocations' : {
        'meta_info' : _MetaInfoClass('VM.AllLocations', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'location',
                'Cisco-IOS-XR-sysadmin-vm-mgr', True, is_config=False),
            _MetaInfoClassMember('all-uiids', REFERENCE_LIST, 'AllUiids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr', 'VM.AllLocations.AllUiids',
                [], [],
                '''                ''',
                'all_uiids',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-vm-mgr',
            'all-locations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm-mgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr',
            is_config=False,
        ),
    },
    'VM' : {
        'meta_info' : _MetaInfoClass('VM', REFERENCE_CLASS,
            '''VM Info''',
            False, 
            [
            _MetaInfoClassMember('all-locations', REFERENCE_LIST, 'AllLocations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr', 'VM.AllLocations',
                [], [],
                '''                ''',
                'all_locations',
                'Cisco-IOS-XR-sysadmin-vm-mgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-vm-mgr',
            'VM',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm-mgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr',
            is_config=False,
        ),
    },
}
_meta_table['VM.AllLocations.AllUiids']['meta_info'].parent =_meta_table['VM.AllLocations']['meta_info']
_meta_table['VM.AllLocations']['meta_info'].parent =_meta_table['VM']['meta_info']
