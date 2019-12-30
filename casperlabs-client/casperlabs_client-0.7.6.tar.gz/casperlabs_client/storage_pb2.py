# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import consensus_pb2 as consensus__pb2
from . import transforms_pb2 as transforms__pb2
from . import scalapb_pb2 as scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storage.proto',
  package='io.casperlabs.storage',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rstorage.proto\x12\x15io.casperlabs.storage\x1a\x0f\x63onsensus.proto\x1a\x10transforms.proto\x1a\rscalapb.proto\"\x91\x01\n\x15\x42lockMsgWithTransform\x12<\n\rblock_message\x18\x01 \x01(\x0b\x32%.io.casperlabs.casper.consensus.Block\x12:\n\x0ftransform_entry\x18\x02 \x03(\x0b\x32!.io.casperlabs.ipc.TransformEntry\"\x93\x03\n\x15\x42lockMetadataInternal\x12\x11\n\tblockHash\x18\x01 \x01(\x0c\x12/\n\x07parents\x18\x02 \x03(\x0c\x42\x1e\xe2?\x1b\x1a\x19\x63ollection.immutable.List\x12\x1c\n\x14validator_public_key\x18\x03 \x01(\x0c\x12k\n\x0ejustifications\x18\x04 \x03(\x0b\x32\x33.io.casperlabs.casper.consensus.Block.JustificationB\x1e\xe2?\x1b\x1a\x19\x63ollection.immutable.List\x12S\n\x05\x62onds\x18\x05 \x03(\x0b\x32$.io.casperlabs.casper.consensus.BondB\x1e\xe2?\x1b\x1a\x19\x63ollection.immutable.List\x12\x0c\n\x04rank\x18\x06 \x01(\x03\x12\x1f\n\x17validator_block_seq_num\x18\x07 \x01(\x05:\'\xe2?$\"\"io.casperlabs.models.BlockMetadatab\x06proto3')
  ,
  dependencies=[consensus__pb2.DESCRIPTOR,transforms__pb2.DESCRIPTOR,scalapb__pb2.DESCRIPTOR,])




_BLOCKMSGWITHTRANSFORM = _descriptor.Descriptor(
  name='BlockMsgWithTransform',
  full_name='io.casperlabs.storage.BlockMsgWithTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_message', full_name='io.casperlabs.storage.BlockMsgWithTransform.block_message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transform_entry', full_name='io.casperlabs.storage.BlockMsgWithTransform.transform_entry', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=91,
  serialized_end=236,
)


_BLOCKMETADATAINTERNAL = _descriptor.Descriptor(
  name='BlockMetadataInternal',
  full_name='io.casperlabs.storage.BlockMetadataInternal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blockHash', full_name='io.casperlabs.storage.BlockMetadataInternal.blockHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='io.casperlabs.storage.BlockMetadataInternal.parents', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342?\033\032\031collection.immutable.List'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_public_key', full_name='io.casperlabs.storage.BlockMetadataInternal.validator_public_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='justifications', full_name='io.casperlabs.storage.BlockMetadataInternal.justifications', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342?\033\032\031collection.immutable.List'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonds', full_name='io.casperlabs.storage.BlockMetadataInternal.bonds', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342?\033\032\031collection.immutable.List'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='io.casperlabs.storage.BlockMetadataInternal.rank', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_block_seq_num', full_name='io.casperlabs.storage.BlockMetadataInternal.validator_block_seq_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?$\"\"io.casperlabs.models.BlockMetadata'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=642,
)

_BLOCKMSGWITHTRANSFORM.fields_by_name['block_message'].message_type = consensus__pb2._BLOCK
_BLOCKMSGWITHTRANSFORM.fields_by_name['transform_entry'].message_type = transforms__pb2._TRANSFORMENTRY
_BLOCKMETADATAINTERNAL.fields_by_name['justifications'].message_type = consensus__pb2._BLOCK_JUSTIFICATION
_BLOCKMETADATAINTERNAL.fields_by_name['bonds'].message_type = consensus__pb2._BOND
DESCRIPTOR.message_types_by_name['BlockMsgWithTransform'] = _BLOCKMSGWITHTRANSFORM
DESCRIPTOR.message_types_by_name['BlockMetadataInternal'] = _BLOCKMETADATAINTERNAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockMsgWithTransform = _reflection.GeneratedProtocolMessageType('BlockMsgWithTransform', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKMSGWITHTRANSFORM,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.storage.BlockMsgWithTransform)
  })
_sym_db.RegisterMessage(BlockMsgWithTransform)

BlockMetadataInternal = _reflection.GeneratedProtocolMessageType('BlockMetadataInternal', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKMETADATAINTERNAL,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.storage.BlockMetadataInternal)
  })
_sym_db.RegisterMessage(BlockMetadataInternal)


_BLOCKMETADATAINTERNAL.fields_by_name['parents']._options = None
_BLOCKMETADATAINTERNAL.fields_by_name['justifications']._options = None
_BLOCKMETADATAINTERNAL.fields_by_name['bonds']._options = None
_BLOCKMETADATAINTERNAL._options = None
# @@protoc_insertion_point(module_scope)
