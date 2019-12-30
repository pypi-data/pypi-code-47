# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tb_paddle/proto/step_stats.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tb_paddle/proto/step_stats.proto',
  package='tb_paddle',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\017StepStatsProtosP\001Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\370\001\001',
  serialized_pb=b'\n tb_paddle/proto/step_stats.proto\x12\ttb_paddle\"=\n\x10\x41llocationRecord\x12\x14\n\x0c\x61lloc_micros\x18\x01 \x01(\x03\x12\x13\n\x0b\x61lloc_bytes\x18\x02 \x01(\x03\"\xc3\x01\n\x13\x41llocatorMemoryUsed\x12\x16\n\x0e\x61llocator_name\x18\x01 \x01(\t\x12\x13\n\x0btotal_bytes\x18\x02 \x01(\x03\x12\x12\n\npeak_bytes\x18\x03 \x01(\x03\x12\x12\n\nlive_bytes\x18\x04 \x01(\x03\x12\x37\n\x12\x61llocation_records\x18\x06 \x03(\x0b\x32\x1b.tb_paddle.AllocationRecord\x12\x1e\n\x16\x61llocator_bytes_in_use\x18\x05 \x01(\x03\"\x1a\n\nNodeOutput\x12\x0c\n\x04slot\x18\x01 \x01(\x05\"\xec\x01\n\x0bMemoryStats\x12\x18\n\x10temp_memory_size\x18\x01 \x01(\x03\x12\x1e\n\x16persistent_memory_size\x18\x03 \x01(\x03\x12#\n\x1bpersistent_tensor_alloc_ids\x18\x05 \x03(\x03\x12#\n\x17\x64\x65vice_temp_memory_size\x18\x02 \x01(\x03\x42\x02\x18\x01\x12)\n\x1d\x64\x65vice_persistent_memory_size\x18\x04 \x01(\x03\x42\x02\x18\x01\x12.\n\"device_persistent_tensor_alloc_ids\x18\x06 \x03(\x03\x42\x02\x18\x01\"\xda\x02\n\rNodeExecStats\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x18\n\x10\x61ll_start_micros\x18\x02 \x01(\x03\x12\x1b\n\x13op_start_rel_micros\x18\x03 \x01(\x03\x12\x19\n\x11op_end_rel_micros\x18\x04 \x01(\x03\x12\x1a\n\x12\x61ll_end_rel_micros\x18\x05 \x01(\x03\x12.\n\x06memory\x18\x06 \x03(\x0b\x32\x1e.tb_paddle.AllocatorMemoryUsed\x12%\n\x06output\x18\x07 \x03(\x0b\x32\x15.tb_paddle.NodeOutput\x12\x16\n\x0etimeline_label\x18\x08 \x01(\t\x12\x18\n\x10scheduled_micros\x18\t \x01(\x03\x12\x11\n\tthread_id\x18\n \x01(\r\x12,\n\x0cmemory_stats\x18\x0c \x01(\x0b\x32\x16.tb_paddle.MemoryStats\"O\n\x0f\x44\x65viceStepStats\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12,\n\nnode_stats\x18\x02 \x03(\x0b\x32\x18.tb_paddle.NodeExecStats\":\n\tStepStats\x12-\n\tdev_stats\x18\x01 \x03(\x0b\x32\x1a.tb_paddle.DeviceStepStats\"7\n\x0bRunMetadata\x12(\n\nstep_stats\x18\x01 \x01(\x0b\x32\x14.tb_paddle.StepStatsBo\n\x18org.tensorflow.frameworkB\x0fStepStatsProtosP\x01Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\xf8\x01\x01\x62\x06proto3'
)




_ALLOCATIONRECORD = _descriptor.Descriptor(
  name='AllocationRecord',
  full_name='tb_paddle.AllocationRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alloc_micros', full_name='tb_paddle.AllocationRecord.alloc_micros', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alloc_bytes', full_name='tb_paddle.AllocationRecord.alloc_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=108,
)


_ALLOCATORMEMORYUSED = _descriptor.Descriptor(
  name='AllocatorMemoryUsed',
  full_name='tb_paddle.AllocatorMemoryUsed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allocator_name', full_name='tb_paddle.AllocatorMemoryUsed.allocator_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_bytes', full_name='tb_paddle.AllocatorMemoryUsed.total_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peak_bytes', full_name='tb_paddle.AllocatorMemoryUsed.peak_bytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='live_bytes', full_name='tb_paddle.AllocatorMemoryUsed.live_bytes', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocation_records', full_name='tb_paddle.AllocatorMemoryUsed.allocation_records', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocator_bytes_in_use', full_name='tb_paddle.AllocatorMemoryUsed.allocator_bytes_in_use', index=5,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=306,
)


_NODEOUTPUT = _descriptor.Descriptor(
  name='NodeOutput',
  full_name='tb_paddle.NodeOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot', full_name='tb_paddle.NodeOutput.slot', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=334,
)


_MEMORYSTATS = _descriptor.Descriptor(
  name='MemoryStats',
  full_name='tb_paddle.MemoryStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temp_memory_size', full_name='tb_paddle.MemoryStats.temp_memory_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='persistent_memory_size', full_name='tb_paddle.MemoryStats.persistent_memory_size', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='persistent_tensor_alloc_ids', full_name='tb_paddle.MemoryStats.persistent_tensor_alloc_ids', index=2,
      number=5, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_temp_memory_size', full_name='tb_paddle.MemoryStats.device_temp_memory_size', index=3,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_persistent_memory_size', full_name='tb_paddle.MemoryStats.device_persistent_memory_size', index=4,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_persistent_tensor_alloc_ids', full_name='tb_paddle.MemoryStats.device_persistent_tensor_alloc_ids', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=337,
  serialized_end=573,
)


_NODEEXECSTATS = _descriptor.Descriptor(
  name='NodeExecStats',
  full_name='tb_paddle.NodeExecStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='tb_paddle.NodeExecStats.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_start_micros', full_name='tb_paddle.NodeExecStats.all_start_micros', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_start_rel_micros', full_name='tb_paddle.NodeExecStats.op_start_rel_micros', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_end_rel_micros', full_name='tb_paddle.NodeExecStats.op_end_rel_micros', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_end_rel_micros', full_name='tb_paddle.NodeExecStats.all_end_rel_micros', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='tb_paddle.NodeExecStats.memory', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='tb_paddle.NodeExecStats.output', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeline_label', full_name='tb_paddle.NodeExecStats.timeline_label', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduled_micros', full_name='tb_paddle.NodeExecStats.scheduled_micros', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='tb_paddle.NodeExecStats.thread_id', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_stats', full_name='tb_paddle.NodeExecStats.memory_stats', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=576,
  serialized_end=922,
)


_DEVICESTEPSTATS = _descriptor.Descriptor(
  name='DeviceStepStats',
  full_name='tb_paddle.DeviceStepStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='tb_paddle.DeviceStepStats.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_stats', full_name='tb_paddle.DeviceStepStats.node_stats', index=1,
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
  serialized_start=924,
  serialized_end=1003,
)


_STEPSTATS = _descriptor.Descriptor(
  name='StepStats',
  full_name='tb_paddle.StepStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_stats', full_name='tb_paddle.StepStats.dev_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1005,
  serialized_end=1063,
)


_RUNMETADATA = _descriptor.Descriptor(
  name='RunMetadata',
  full_name='tb_paddle.RunMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_stats', full_name='tb_paddle.RunMetadata.step_stats', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1065,
  serialized_end=1120,
)

_ALLOCATORMEMORYUSED.fields_by_name['allocation_records'].message_type = _ALLOCATIONRECORD
_NODEEXECSTATS.fields_by_name['memory'].message_type = _ALLOCATORMEMORYUSED
_NODEEXECSTATS.fields_by_name['output'].message_type = _NODEOUTPUT
_NODEEXECSTATS.fields_by_name['memory_stats'].message_type = _MEMORYSTATS
_DEVICESTEPSTATS.fields_by_name['node_stats'].message_type = _NODEEXECSTATS
_STEPSTATS.fields_by_name['dev_stats'].message_type = _DEVICESTEPSTATS
_RUNMETADATA.fields_by_name['step_stats'].message_type = _STEPSTATS
DESCRIPTOR.message_types_by_name['AllocationRecord'] = _ALLOCATIONRECORD
DESCRIPTOR.message_types_by_name['AllocatorMemoryUsed'] = _ALLOCATORMEMORYUSED
DESCRIPTOR.message_types_by_name['NodeOutput'] = _NODEOUTPUT
DESCRIPTOR.message_types_by_name['MemoryStats'] = _MEMORYSTATS
DESCRIPTOR.message_types_by_name['NodeExecStats'] = _NODEEXECSTATS
DESCRIPTOR.message_types_by_name['DeviceStepStats'] = _DEVICESTEPSTATS
DESCRIPTOR.message_types_by_name['StepStats'] = _STEPSTATS
DESCRIPTOR.message_types_by_name['RunMetadata'] = _RUNMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AllocationRecord = _reflection.GeneratedProtocolMessageType('AllocationRecord', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATIONRECORD,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.AllocationRecord)
  })
_sym_db.RegisterMessage(AllocationRecord)

AllocatorMemoryUsed = _reflection.GeneratedProtocolMessageType('AllocatorMemoryUsed', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATORMEMORYUSED,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.AllocatorMemoryUsed)
  })
_sym_db.RegisterMessage(AllocatorMemoryUsed)

NodeOutput = _reflection.GeneratedProtocolMessageType('NodeOutput', (_message.Message,), {
  'DESCRIPTOR' : _NODEOUTPUT,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.NodeOutput)
  })
_sym_db.RegisterMessage(NodeOutput)

MemoryStats = _reflection.GeneratedProtocolMessageType('MemoryStats', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYSTATS,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.MemoryStats)
  })
_sym_db.RegisterMessage(MemoryStats)

NodeExecStats = _reflection.GeneratedProtocolMessageType('NodeExecStats', (_message.Message,), {
  'DESCRIPTOR' : _NODEEXECSTATS,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.NodeExecStats)
  })
_sym_db.RegisterMessage(NodeExecStats)

DeviceStepStats = _reflection.GeneratedProtocolMessageType('DeviceStepStats', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTEPSTATS,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.DeviceStepStats)
  })
_sym_db.RegisterMessage(DeviceStepStats)

StepStats = _reflection.GeneratedProtocolMessageType('StepStats', (_message.Message,), {
  'DESCRIPTOR' : _STEPSTATS,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.StepStats)
  })
_sym_db.RegisterMessage(StepStats)

RunMetadata = _reflection.GeneratedProtocolMessageType('RunMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RUNMETADATA,
  '__module__' : 'tb_paddle.proto.step_stats_pb2'
  # @@protoc_insertion_point(class_scope:tb_paddle.RunMetadata)
  })
_sym_db.RegisterMessage(RunMetadata)


DESCRIPTOR._options = None
_MEMORYSTATS.fields_by_name['device_temp_memory_size']._options = None
_MEMORYSTATS.fields_by_name['device_persistent_memory_size']._options = None
_MEMORYSTATS.fields_by_name['device_persistent_tensor_alloc_ids']._options = None
# @@protoc_insertion_point(module_scope)
