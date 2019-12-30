# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tb_paddle/proto/graph.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tb_paddle.proto import node_def_pb2 as tb__paddle_dot_proto_dot_node__def__pb2
from tb_paddle.proto import versions_pb2 as tb__paddle_dot_proto_dot_versions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tb_paddle/proto/graph.proto',
  package='tb_paddle',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\013GraphProtosP\001\370\001\001',
  serialized_pb=b'\n\x1btb_paddle/proto/graph.proto\x12\ttb_paddle\x1a\x1etb_paddle/proto/node_def.proto\x1a\x1etb_paddle/proto/versions.proto\"j\n\x08GraphDef\x12 \n\x04node\x18\x01 \x03(\x0b\x32\x12.tb_paddle.NodeDef\x12\'\n\x08versions\x18\x04 \x01(\x0b\x32\x15.tb_paddle.VersionDef\x12\x13\n\x07version\x18\x03 \x01(\x05\x42\x02\x18\x01\x42,\n\x18org.tensorflow.frameworkB\x0bGraphProtosP\x01\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tb__paddle_dot_proto_dot_node__def__pb2.DESCRIPTOR,tb__paddle_dot_proto_dot_versions__pb2.DESCRIPTOR,])




_GRAPHDEF = _descriptor.Descriptor(
  name='GraphDef',
  full_name='tb_paddle.GraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='tb_paddle.GraphDef.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versions', full_name='tb_paddle.GraphDef.versions', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='tb_paddle.GraphDef.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=212,
)

_GRAPHDEF.fields_by_name['node'].message_type = tb__paddle_dot_proto_dot_node__def__pb2._NODEDEF
_GRAPHDEF.fields_by_name['versions'].message_type = tb__paddle_dot_proto_dot_versions__pb2._VERSIONDEF
DESCRIPTOR.message_types_by_name['GraphDef'] = _GRAPHDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphDef = _reflection.GeneratedProtocolMessageType('GraphDef', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHDEF,
  '__module__' : 'tb_paddle.proto.graph_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.GraphDef)
  })
_sym_db.RegisterMessage(GraphDef)


DESCRIPTOR._options = None
_GRAPHDEF.fields_by_name['version']._options = None
# @@protoc_insertion_point(module_scope)
