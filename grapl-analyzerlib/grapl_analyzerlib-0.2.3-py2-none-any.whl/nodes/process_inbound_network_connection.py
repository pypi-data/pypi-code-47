from grapl_analyzerlib.schemas import NodeSchema


class ProcessInboundConnectionSchema(NodeSchema):
    def __init__(self):
        super(ProcessInboundConnectionSchema, self).__init__()
        (
            self
            .with_str_prop('ip_address')
            .with_str_prop('protocol')
            .with_int_prop('created_timestamp')
            .with_int_prop('terminated_timestamp')
            .with_int_prop('last_seen_timestamp')
            .with_int_prop('port')
            .with_forward_edge(
                'bound_port',
                # The IP + Port that was bound
                ManyToMany(IpPortSchema),
                'bound_by'
            )
            .with_forward_edge(
                'bound_by',
                # The IP that was bound
                ManyToMany(IpAddressSchema),
                'bound_by',
            )
        )

    @staticmethod
    def self_type() -> str:
        return "ProcessInboundConnection"




def main():
    schema = ProcessInboundConnectionSchema()

    query = generate_plugin_query(schema)
    view = generate_plugin_view(schema)
    query_extensions = generate_plugin_query_extensions(schema)
    view_extensions = generate_plugin_view_extensions(schema)

    print(query)
    print(view)
    print(query_extensions)
    print(view_extensions)


if __name__ == '__main__':
    main()

from grapl_analyzerlib.nodes.ip_address_node import IpAddressSchema
from grapl_analyzerlib.nodes.ip_port_node import IpPortSchema

from grapl_analyzerlib.schemas.schema_builder import generate_plugin_query, generate_plugin_view, \
    generate_plugin_query_extensions, generate_plugin_view_extensions, ManyToOne, ManyToMany
