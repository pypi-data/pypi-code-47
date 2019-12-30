# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tb_paddle/proto/resource_handle.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tb_paddle/proto/resource_handle.proto',
  package='tb_paddle',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\016ResourceHandleP\001\370\001\001',
  serialized_pb=b'\n%tb_paddle/proto/resource_handle.proto\x12\ttb_paddle\"r\n\x13ResourceHandleProto\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x11\n\tcontainer\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\thash_code\x18\x04 \x01(\x04\x12\x17\n\x0fmaybe_type_name\x18\x05 \x01(\tB/\n\x18org.tensorflow.frameworkB\x0eResourceHandleP\x01\xf8\x01\x01\x62\x06proto3'
)




_RESOURCEHANDLEPROTO = _descriptor.Descriptor(
  name='ResourceHandleProto',
  full_name='tb_paddle.ResourceHandleProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='tb_paddle.ResourceHandleProto.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container', full_name='tb_paddle.ResourceHandleProto.container', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tb_paddle.ResourceHandleProto.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash_code', full_name='tb_paddle.ResourceHandleProto.hash_code', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maybe_type_name', full_name='tb_paddle.ResourceHandleProto.maybe_type_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=52,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['ResourceHandleProto'] = _RESOURCEHANDLEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceHandleProto = _reflection.GeneratedProtocolMessageType('ResourceHandleProto', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEHANDLEPROTO,
  '__module__' : 'tb_paddle.proto.resource_handle_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.ResourceHandleProto)
  })
_sym_db.RegisterMessage(ResourceHandleProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
