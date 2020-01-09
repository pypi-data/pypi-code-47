
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_pfilter_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo', REFERENCE_LIST,
            '''Operational data for pfilter in bag''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True, is_config=False),
            _MetaInfoClassMember('acl-info', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                acl information
                ''',
                'acl_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-info',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('interface-info', REFERENCE_LIST, 'InterfaceInfo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo',
                [], [],
                '''                Operational data for pfilter in bag
                ''',
                'interface_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-infos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('interface-infos', REFERENCE_CLASS, 'InterfaceInfos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos',
                [], [],
                '''                Operational data for pfilter
                ''',
                'interface_infos',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'acl-info-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('acl-info-table', REFERENCE_CLASS, 'AclInfoTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable',
                [], [],
                '''                Operational data for pfilter
                ''',
                'acl_info_table',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo', REFERENCE_LIST,
            '''Operational data for pfilter in bag''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True, is_config=False),
            _MetaInfoClassMember('acl-info', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                acl information
                ''',
                'acl_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-info',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('interface-info', REFERENCE_LIST, 'InterfaceInfo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo',
                [], [],
                '''                Operational data for pfilter in bag
                ''',
                'interface_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-infos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('interface-infos', REFERENCE_CLASS, 'InterfaceInfos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos',
                [], [],
                '''                Operational data for pfilter
                ''',
                'interface_infos',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'acl-info-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('acl-info-table', REFERENCE_CLASS, 'AclInfoTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable',
                [], [],
                '''                Operational data for pfilter
                ''',
                'acl_info_table',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node.Process' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process', REFERENCE_CLASS,
            '''Operational data for pfilter''',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6',
                [], [],
                '''                Operational data for pfilter
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4',
                [], [],
                '''                Operational data for pfilter
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'process',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node', REFERENCE_LIST,
            '''PfilterMa operational data for a particular
node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                The node
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True, is_config=False),
            _MetaInfoClassMember('process', REFERENCE_CLASS, 'Process', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process',
                [], [],
                '''                Operational data for pfilter
                ''',
                'process',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa.Nodes' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes', REFERENCE_CLASS,
            '''Node-specific operational data''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node',
                [], [],
                '''                PfilterMa operational data for a particular
                node
                ''',
                'node',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
    'PfilterMa' : {
        'meta_info' : _MetaInfoClass('PfilterMa', REFERENCE_CLASS,
            '''Root class of PfilterMa Oper schema''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes',
                [], [],
                '''                Node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-pfilter-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'pfilter-ma',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper',
            is_config=False,
        ),
    },
}
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node']['meta_info']
_meta_table['PfilterMa.Nodes.Node']['meta_info'].parent =_meta_table['PfilterMa.Nodes']['meta_info']
_meta_table['PfilterMa.Nodes']['meta_info'].parent =_meta_table['PfilterMa']['meta_info']
