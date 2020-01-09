
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_vm
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Vm.Config.HwProfile.Profile' : _MetaInfoEnum('Profile',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm.Config.HwProfile.Profile',
        '''xrv9k profile vpe|vrr''',
        {
            'vrr':'vrr',
        }, 'Cisco-IOS-XR-sysadmin-vm', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm']),
    'Vm.Config.HwProfile' : {
        'meta_info' : _MetaInfoClass('Vm.Config.HwProfile', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_ENUM_CLASS, 'Profile', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm.Config.HwProfile.Profile',
                [], [],
                '''                xrv9k profile vpe|vrr
                ''',
                'profile',
                'Cisco-IOS-XR-sysadmin-vm', False),
            ],
            'Cisco-IOS-XR-sysadmin-vm',
            'hw-profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm',
        ),
    },
    'Vm.Config.Memory' : {
        'meta_info' : _MetaInfoClass('Vm.Config.Memory', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('admin', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                admin container memory in GB
                ''',
                'admin',
                'Cisco-IOS-XR-sysadmin-vm', False),
            _MetaInfoClassMember('rp', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                rp container memory in GB
                ''',
                'rp',
                'Cisco-IOS-XR-sysadmin-vm', False),
            _MetaInfoClassMember('lc', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                lc container memory in GB
                ''',
                'lc',
                'Cisco-IOS-XR-sysadmin-vm', False),
            ],
            'Cisco-IOS-XR-sysadmin-vm',
            'memory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm',
        ),
    },
    'Vm.Config.Cpu' : {
        'meta_info' : _MetaInfoClass('Vm.Config.Cpu', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('assign', ATTRIBUTE, 'str', 'cp-dp-cores',
                None, None,
                [], [b'0(-[0-9]+)?/[0-9]+(-[0-9]+)?'],
                '''                assign cpu cores to control/data plane
                ''',
                'assign',
                'Cisco-IOS-XR-sysadmin-vm', False),
            ],
            'Cisco-IOS-XR-sysadmin-vm',
            'cpu',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm',
        ),
    },
    'Vm.Config' : {
        'meta_info' : _MetaInfoClass('Vm.Config', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('hw-profile', REFERENCE_CLASS, 'HwProfile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm.Config.HwProfile',
                [], [],
                '''                ''',
                'hw_profile',
                'Cisco-IOS-XR-sysadmin-vm', False),
            _MetaInfoClassMember('memory', REFERENCE_CLASS, 'Memory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm.Config.Memory',
                [], [],
                '''                ''',
                'memory',
                'Cisco-IOS-XR-sysadmin-vm', False),
            _MetaInfoClassMember('cpu', REFERENCE_CLASS, 'Cpu', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm.Config.Cpu',
                [], [],
                '''                ''',
                'cpu',
                'Cisco-IOS-XR-sysadmin-vm', False),
            ],
            'Cisco-IOS-XR-sysadmin-vm',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm',
        ),
    },
    'Vm' : {
        'meta_info' : _MetaInfoClass('Vm', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm.Config',
                [], [],
                '''                ''',
                'config',
                'Cisco-IOS-XR-sysadmin-vm', False),
            ],
            'Cisco-IOS-XR-sysadmin-vm',
            'vm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-vm'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm',
        ),
    },
}
_meta_table['Vm.Config.HwProfile']['meta_info'].parent =_meta_table['Vm.Config']['meta_info']
_meta_table['Vm.Config.Memory']['meta_info'].parent =_meta_table['Vm.Config']['meta_info']
_meta_table['Vm.Config.Cpu']['meta_info'].parent =_meta_table['Vm.Config']['meta_info']
_meta_table['Vm.Config']['meta_info'].parent =_meta_table['Vm']['meta_info']
