
'''
This is auto-generated file,
which includes metadata for module tailf_netconf_query
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'StartQuery.Input.Select.ResultType' : _MetaInfoEnum('ResultType',
        'ydk.models.cisco_ios_xr.tailf_netconf_query', 'StartQuery.Input.Select.ResultType',
        '''Controls how the result of the select expression is returned
in 'fetch-query-result'.''',
        {
            'string':'string',
            'path':'path',
            'leaf-value':'leaf_value',
            'inline':'inline',
        }, 'tailf-common-query', _yang_ns.NAMESPACE_LOOKUP['tailf-common-query']),
    'StartQuery.Input.Select' : {
        'meta_info' : _MetaInfoClass('StartQuery.Input.Select', REFERENCE_LIST,
            '''A list of expressions that define what to return from each
node in the node set returned by the 'foreach' expression.''',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Optional label which is copied as is to the 'result' list;
                can be used for easy labeling of the returned node(s).
                ''',
                'label',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('expression', ATTRIBUTE, 'str', 'yang:xpath1.0',
                None, None,
                [], [],
                '''                Declare what node(s) you want to retrieve.
                
                This XPath expression is evaluated once for every node in
                the node set returned by the 'foreach' expression.  That node
                is the inital context node when this expression is evaluated.
                ''',
                'expression',
                'tailf-netconf-query', False, is_mandatory=True),
            _MetaInfoClassMember('result-type', REFERENCE_LEAFLIST, 'ResultType', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'StartQuery.Input.Select.ResultType',
                [], [],
                '''                Controls how the result of the select expression is returned
                in 'fetch-query-result'.
                ''',
                'result_type',
                'tailf-netconf-query', False, min_elements=1),
            ],
            'tailf-netconf-query',
            'select',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'StartQuery.Input' : {
        'meta_info' : _MetaInfoClass('StartQuery.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('foreach', ATTRIBUTE, 'str', 'yang:xpath1.0',
                None, None,
                [], [],
                '''                An XPath 1.0 expression that returns a node set.  For each
                node in this node set, a 'result' entry is constructed.  For
                each such node all 'select/expression's are evaluated, and
                stored in 'result/select'.  The resulting entries are
                returned from the 'fetch-query-result' function.
                
                When this XPath expression is evaluated, the context node is the
                root node of the requested data store.
                ''',
                'foreach',
                'tailf-netconf-query', False, is_mandatory=True),
            _MetaInfoClassMember('select', REFERENCE_LIST, 'Select', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'StartQuery.Input.Select',
                [], [],
                '''                A list of expressions that define what to return from each
                node in the node set returned by the 'foreach' expression.
                ''',
                'select',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('sort-by', REFERENCE_LEAFLIST, 'str', 'yang:xpath1.0',
                None, None,
                [], [],
                '''                It is possible to sort the result using an ordered list of
                XPath expressions.
                
                For each node in the node set returned by 'foreach', all
                'sort-by' expressions are evaluated, in order, with the node
                from the 'foreach' evaluation as context node, and the result
                is stored in a tuple.  Thus, this tuple has as many elements
                as entries in the 'sort-by' leaf list.
                
                Each expression should return a node set where the first
                node should be a leaf.  The value of this leaf is used in
                the tuple.  If the expression returns something else, the
                value in the tuple is undefined.
                
                When the 'result' list is fetched, is is sorted according to
                the associated tuple.
                ''',
                'sort_by',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The maximum number of 'result' entries to return in each
                call to 'fetch-query-result'.
                
                If this parameter is not given, all entries are returned.
                ''',
                'limit',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                ''',
                'offset',
                'tailf-netconf-query', False, default_value="1"),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The maximum time (in seconds) before a query times out. Resets every
                new request, i.e. subsequent function calls starts a new timeout
                timer.
                ''',
                'timeout',
                'tailf-netconf-query', False, default_value="600"),
            ],
            'tailf-netconf-query',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'StartQuery.Output' : {
        'meta_info' : _MetaInfoClass('StartQuery.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'query_handle',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'StartQuery' : {
        'meta_info' : _MetaInfoClass('StartQuery', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'StartQuery.Input',
                [], [],
                '''                ''',
                'input',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'StartQuery.Output',
                [], [],
                '''                ''',
                'output',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'start-query',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'FetchQueryResult.Input' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'query_handle',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'FetchQueryResult.Output.QueryResult.Result.Select' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult.Output.QueryResult.Result.Select', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Present if the label was given in the input select
                entry.
                ''',
                'label',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'instance-identifier',
                None, None,
                [], [],
                '''                ''',
                'path',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'value',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object', '',
                None, None,
                [], [],
                '''                A deep structure of XML (or other API dependent
                format, e.g., JSON)
                ''',
                'data',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'select',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'FetchQueryResult.Output.QueryResult.Result' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult.Output.QueryResult.Result', REFERENCE_LIST,
            '''There will be one result for each node in the node set
produced by evaluating the 'foreach' expression.''',
            False, 
            [
            _MetaInfoClassMember('select', REFERENCE_LIST, 'Select', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'FetchQueryResult.Output.QueryResult.Result.Select',
                [], [],
                '''                ''',
                'select',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'result',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'FetchQueryResult.Output.QueryResult' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult.Output.QueryResult', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('result', REFERENCE_LIST, 'Result', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'FetchQueryResult.Output.QueryResult.Result',
                [], [],
                '''                There will be one result for each node in the node set
                produced by evaluating the 'foreach' expression.
                ''',
                'result',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'query-result',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'FetchQueryResult.Output' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('query-result', REFERENCE_CLASS, 'QueryResult', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'FetchQueryResult.Output.QueryResult',
                [], [],
                '''                ''',
                'query_result',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'FetchQueryResult' : {
        'meta_info' : _MetaInfoClass('FetchQueryResult', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'FetchQueryResult.Input',
                [], [],
                '''                ''',
                'input',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'FetchQueryResult.Output',
                [], [],
                '''                ''',
                'output',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'fetch-query-result',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery.Input.Select.ResultType' : _MetaInfoEnum('ResultType',
        'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Input.Select.ResultType',
        '''Controls how the result of the select expression is returned
in 'fetch-query-result'.''',
        {
            'string':'string',
            'path':'path',
            'leaf-value':'leaf_value',
            'inline':'inline',
        }, 'tailf-common-query', _yang_ns.NAMESPACE_LOOKUP['tailf-common-query']),
    'ImmediateQuery.Input.Select' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery.Input.Select', REFERENCE_LIST,
            '''A list of expressions that define what to return from each
node in the node set returned by the 'foreach' expression.''',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Optional label which is copied as is to the 'result' list;
                can be used for easy labeling of the returned node(s).
                ''',
                'label',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('expression', ATTRIBUTE, 'str', 'yang:xpath1.0',
                None, None,
                [], [],
                '''                Declare what node(s) you want to retrieve.
                
                This XPath expression is evaluated once for every node in
                the node set returned by the 'foreach' expression.  That node
                is the inital context node when this expression is evaluated.
                ''',
                'expression',
                'tailf-netconf-query', False, is_mandatory=True),
            _MetaInfoClassMember('result-type', REFERENCE_LEAFLIST, 'ResultType', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Input.Select.ResultType',
                [], [],
                '''                Controls how the result of the select expression is returned
                in 'fetch-query-result'.
                ''',
                'result_type',
                'tailf-netconf-query', False, min_elements=1),
            ],
            'tailf-netconf-query',
            'select',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery.Input' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('foreach', ATTRIBUTE, 'str', 'yang:xpath1.0',
                None, None,
                [], [],
                '''                An XPath 1.0 expression that returns a node set.  For each
                node in this node set, a 'result' entry is constructed.  For
                each such node all 'select/expression's are evaluated, and
                stored in 'result/select'.  The resulting entries are
                returned from the 'fetch-query-result' function.
                
                When this XPath expression is evaluated, the context node is the
                root node of the requested data store.
                ''',
                'foreach',
                'tailf-netconf-query', False, is_mandatory=True),
            _MetaInfoClassMember('select', REFERENCE_LIST, 'Select', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Input.Select',
                [], [],
                '''                A list of expressions that define what to return from each
                node in the node set returned by the 'foreach' expression.
                ''',
                'select',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('sort-by', REFERENCE_LEAFLIST, 'str', 'yang:xpath1.0',
                None, None,
                [], [],
                '''                It is possible to sort the result using an ordered list of
                XPath expressions.
                
                For each node in the node set returned by 'foreach', all
                'sort-by' expressions are evaluated, in order, with the node
                from the 'foreach' evaluation as context node, and the result
                is stored in a tuple.  Thus, this tuple has as many elements
                as entries in the 'sort-by' leaf list.
                
                Each expression should return a node set where the first
                node should be a leaf.  The value of this leaf is used in
                the tuple.  If the expression returns something else, the
                value in the tuple is undefined.
                
                When the 'result' list is fetched, is is sorted according to
                the associated tuple.
                ''',
                'sort_by',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The maximum number of 'result' entries to return in each
                call to 'fetch-query-result'.
                
                If this parameter is not given, all entries are returned.
                ''',
                'limit',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                ''',
                'offset',
                'tailf-netconf-query', False, default_value="1"),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The maximum time (in seconds) before a query times out. Resets every
                new request, i.e. subsequent function calls starts a new timeout
                timer.
                ''',
                'timeout',
                'tailf-netconf-query', False, default_value="600"),
            ],
            'tailf-netconf-query',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery.Output.QueryResult.Result.Select' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery.Output.QueryResult.Result.Select', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Present if the label was given in the input select
                entry.
                ''',
                'label',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'instance-identifier',
                None, None,
                [], [],
                '''                ''',
                'path',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'value',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object', '',
                None, None,
                [], [],
                '''                A deep structure of XML (or other API dependent
                format, e.g., JSON)
                ''',
                'data',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'select',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery.Output.QueryResult.Result' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery.Output.QueryResult.Result', REFERENCE_LIST,
            '''There will be one result for each node in the node set
produced by evaluating the 'foreach' expression.''',
            False, 
            [
            _MetaInfoClassMember('select', REFERENCE_LIST, 'Select', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Output.QueryResult.Result.Select',
                [], [],
                '''                ''',
                'select',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'result',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery.Output.QueryResult' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery.Output.QueryResult', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('result', REFERENCE_LIST, 'Result', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Output.QueryResult.Result',
                [], [],
                '''                There will be one result for each node in the node set
                produced by evaluating the 'foreach' expression.
                ''',
                'result',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'query-result',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery.Output' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('query-result', REFERENCE_CLASS, 'QueryResult', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Output.QueryResult',
                [], [],
                '''                ''',
                'query_result',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ImmediateQuery' : {
        'meta_info' : _MetaInfoClass('ImmediateQuery', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Input',
                [], [],
                '''                ''',
                'input',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ImmediateQuery.Output',
                [], [],
                '''                ''',
                'output',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'immediate-query',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ResetQuery.Input' : {
        'meta_info' : _MetaInfoClass('ResetQuery.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'query_handle',
                'tailf-netconf-query', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                ''',
                'offset',
                'tailf-netconf-query', False, default_value="1"),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The maximum time (in seconds) before a query times out. Resets every
                new request, i.e. subsequent function calls starts a new timeout
                timer.
                ''',
                'timeout',
                'tailf-netconf-query', False, default_value="600"),
            ],
            'tailf-netconf-query',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'ResetQuery' : {
        'meta_info' : _MetaInfoClass('ResetQuery', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'ResetQuery.Input',
                [], [],
                '''                ''',
                'input',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'reset-query',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'StopQuery.Input' : {
        'meta_info' : _MetaInfoClass('StopQuery.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('query-handle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'query_handle',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
    'StopQuery' : {
        'meta_info' : _MetaInfoClass('StopQuery', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.tailf_netconf_query', 'StopQuery.Input',
                [], [],
                '''                ''',
                'input',
                'tailf-netconf-query', False),
            ],
            'tailf-netconf-query',
            'stop-query',
            _yang_ns.NAMESPACE_LOOKUP['tailf-netconf-query'],
            'ydk.models.cisco_ios_xr.tailf_netconf_query',
        ),
    },
}
_meta_table['StartQuery.Input.Select']['meta_info'].parent =_meta_table['StartQuery.Input']['meta_info']
_meta_table['StartQuery.Input']['meta_info'].parent =_meta_table['StartQuery']['meta_info']
_meta_table['StartQuery.Output']['meta_info'].parent =_meta_table['StartQuery']['meta_info']
_meta_table['FetchQueryResult.Output.QueryResult.Result.Select']['meta_info'].parent =_meta_table['FetchQueryResult.Output.QueryResult.Result']['meta_info']
_meta_table['FetchQueryResult.Output.QueryResult.Result']['meta_info'].parent =_meta_table['FetchQueryResult.Output.QueryResult']['meta_info']
_meta_table['FetchQueryResult.Output.QueryResult']['meta_info'].parent =_meta_table['FetchQueryResult.Output']['meta_info']
_meta_table['FetchQueryResult.Input']['meta_info'].parent =_meta_table['FetchQueryResult']['meta_info']
_meta_table['FetchQueryResult.Output']['meta_info'].parent =_meta_table['FetchQueryResult']['meta_info']
_meta_table['ImmediateQuery.Input.Select']['meta_info'].parent =_meta_table['ImmediateQuery.Input']['meta_info']
_meta_table['ImmediateQuery.Output.QueryResult.Result.Select']['meta_info'].parent =_meta_table['ImmediateQuery.Output.QueryResult.Result']['meta_info']
_meta_table['ImmediateQuery.Output.QueryResult.Result']['meta_info'].parent =_meta_table['ImmediateQuery.Output.QueryResult']['meta_info']
_meta_table['ImmediateQuery.Output.QueryResult']['meta_info'].parent =_meta_table['ImmediateQuery.Output']['meta_info']
_meta_table['ImmediateQuery.Input']['meta_info'].parent =_meta_table['ImmediateQuery']['meta_info']
_meta_table['ImmediateQuery.Output']['meta_info'].parent =_meta_table['ImmediateQuery']['meta_info']
_meta_table['ResetQuery.Input']['meta_info'].parent =_meta_table['ResetQuery']['meta_info']
_meta_table['StopQuery.Input']['meta_info'].parent =_meta_table['StopQuery']['meta_info']
