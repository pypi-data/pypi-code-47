# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sqlflow/proto/sqlflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sqlflow/proto/sqlflow.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bsqlflow/proto/sqlflow.proto\x12\x05proto\x1a\x19google/protobuf/any.proto\"\x11\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\"L\n\x0c\x46\x65tchRequest\x12\x17\n\x03job\x18\x01 \x01(\x0b\x32\n.proto.Job\x12\x0f\n\x07step_id\x18\x02 \x01(\t\x12\x12\n\nlog_offset\x18\x03 \x01(\t\"\x90\x01\n\rFetchResponse\x12\x30\n\x13updated_fetch_since\x18\x01 \x01(\x0b\x32\x13.proto.FetchRequest\x12\x0b\n\x03\x65of\x18\x02 \x01(\x08\x12\'\n\x04logs\x18\x03 \x01(\x0b\x32\x19.proto.FetchResponse.Logs\x1a\x17\n\x04Logs\x12\x0f\n\x07\x63ontent\x18\x01 \x03(\t\"\xaf\x01\n\x07Session\x12\r\n\x05token\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x62_conn_str\x18\x02 \x01(\t\x12\x16\n\x0e\x65xit_on_submit\x18\x03 \x01(\x08\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x15\n\rhive_location\x18\x05 \x01(\t\x12\x1a\n\x12hdfs_namenode_addr\x18\x06 \x01(\t\x12\x11\n\thdfs_user\x18\x07 \x01(\t\x12\x11\n\thdfs_pass\x18\x08 \x01(\t\"7\n\x07Request\x12\x0b\n\x03sql\x18\x01 \x01(\t\x12\x1f\n\x07session\x18\x02 \x01(\x0b\x32\x0e.proto.Session\"\xb2\x01\n\x08Response\x12\x1b\n\x04head\x18\x01 \x01(\x0b\x32\x0b.proto.HeadH\x00\x12\x19\n\x03row\x18\x02 \x01(\x0b\x32\n.proto.RowH\x00\x12!\n\x07message\x18\x03 \x01(\x0b\x32\x0e.proto.MessageH\x00\x12$\n\x03\x65oe\x18\x04 \x01(\x0b\x32\x15.proto.EndOfExecutionH\x00\x12\x19\n\x03job\x18\x05 \x01(\x0b\x32\n.proto.JobH\x00\x42\n\n\x08response\"\x1c\n\x04Head\x12\x14\n\x0c\x63olumn_names\x18\x01 \x03(\t\"1\n\x03Row\x12\"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\x1a\x06\n\x04Null\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"9\n\x0e\x45ndOfExecution\x12\x0b\n\x03sql\x18\x01 \x01(\t\x12\x1a\n\x12spent_time_seconds\x18\x02 \x01(\x03\x32g\n\x07SQLFlow\x12(\n\x03Run\x12\x0e.proto.Request\x1a\x0f.proto.Response0\x01\x12\x32\n\x05\x46\x65tch\x12\x13.proto.FetchRequest\x1a\x14.proto.FetchResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='proto.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=65,
  serialized_end=82,
)


_FETCHREQUEST = _descriptor.Descriptor(
  name='FetchRequest',
  full_name='proto.FetchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='proto.FetchRequest.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step_id', full_name='proto.FetchRequest.step_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_offset', full_name='proto.FetchRequest.log_offset', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=84,
  serialized_end=160,
)


_FETCHRESPONSE_LOGS = _descriptor.Descriptor(
  name='Logs',
  full_name='proto.FetchResponse.Logs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='proto.FetchResponse.Logs.content', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=284,
  serialized_end=307,
)

_FETCHRESPONSE = _descriptor.Descriptor(
  name='FetchResponse',
  full_name='proto.FetchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated_fetch_since', full_name='proto.FetchResponse.updated_fetch_since', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eof', full_name='proto.FetchResponse.eof', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='proto.FetchResponse.logs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FETCHRESPONSE_LOGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=307,
)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='proto.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='proto.Session.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db_conn_str', full_name='proto.Session.db_conn_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_on_submit', full_name='proto.Session.exit_on_submit', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='proto.Session.user_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hive_location', full_name='proto.Session.hive_location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hdfs_namenode_addr', full_name='proto.Session.hdfs_namenode_addr', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hdfs_user', full_name='proto.Session.hdfs_user', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hdfs_pass', full_name='proto.Session.hdfs_pass', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=310,
  serialized_end=485,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='proto.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sql', full_name='proto.Request.sql', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session', full_name='proto.Request.session', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=487,
  serialized_end=542,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='proto.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='proto.Response.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row', full_name='proto.Response.row', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.Response.message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eoe', full_name='proto.Response.eoe', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job', full_name='proto.Response.job', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='response', full_name='proto.Response.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=545,
  serialized_end=723,
)


_HEAD = _descriptor.Descriptor(
  name='Head',
  full_name='proto.Head',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column_names', full_name='proto.Head.column_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=725,
  serialized_end=753,
)


_ROW_NULL = _descriptor.Descriptor(
  name='Null',
  full_name='proto.Row.Null',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=798,
  serialized_end=804,
)

_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='proto.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='proto.Row.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ROW_NULL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=755,
  serialized_end=804,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='proto.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=806,
  serialized_end=832,
)


_ENDOFEXECUTION = _descriptor.Descriptor(
  name='EndOfExecution',
  full_name='proto.EndOfExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sql', full_name='proto.EndOfExecution.sql', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spent_time_seconds', full_name='proto.EndOfExecution.spent_time_seconds', index=1,
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
  serialized_start=834,
  serialized_end=891,
)

_FETCHREQUEST.fields_by_name['job'].message_type = _JOB
_FETCHRESPONSE_LOGS.containing_type = _FETCHRESPONSE
_FETCHRESPONSE.fields_by_name['updated_fetch_since'].message_type = _FETCHREQUEST
_FETCHRESPONSE.fields_by_name['logs'].message_type = _FETCHRESPONSE_LOGS
_REQUEST.fields_by_name['session'].message_type = _SESSION
_RESPONSE.fields_by_name['head'].message_type = _HEAD
_RESPONSE.fields_by_name['row'].message_type = _ROW
_RESPONSE.fields_by_name['message'].message_type = _MESSAGE
_RESPONSE.fields_by_name['eoe'].message_type = _ENDOFEXECUTION
_RESPONSE.fields_by_name['job'].message_type = _JOB
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['head'])
_RESPONSE.fields_by_name['head'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['row'])
_RESPONSE.fields_by_name['row'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['message'])
_RESPONSE.fields_by_name['message'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['eoe'])
_RESPONSE.fields_by_name['eoe'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['job'])
_RESPONSE.fields_by_name['job'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_ROW_NULL.containing_type = _ROW
_ROW.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['FetchRequest'] = _FETCHREQUEST
DESCRIPTOR.message_types_by_name['FetchResponse'] = _FETCHRESPONSE
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Head'] = _HEAD
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['EndOfExecution'] = _ENDOFEXECUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Job)
  })
_sym_db.RegisterMessage(Job)

FetchRequest = _reflection.GeneratedProtocolMessageType('FetchRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHREQUEST,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.FetchRequest)
  })
_sym_db.RegisterMessage(FetchRequest)

FetchResponse = _reflection.GeneratedProtocolMessageType('FetchResponse', (_message.Message,), {

  'Logs' : _reflection.GeneratedProtocolMessageType('Logs', (_message.Message,), {
    'DESCRIPTOR' : _FETCHRESPONSE_LOGS,
    '__module__' : 'sqlflow.proto.sqlflow_pb2'
    # @@protoc_insertion_point(class_scope:proto.FetchResponse.Logs)
    })
  ,
  'DESCRIPTOR' : _FETCHRESPONSE,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.FetchResponse)
  })
_sym_db.RegisterMessage(FetchResponse)
_sym_db.RegisterMessage(FetchResponse.Logs)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Session)
  })
_sym_db.RegisterMessage(Session)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Response)
  })
_sym_db.RegisterMessage(Response)

Head = _reflection.GeneratedProtocolMessageType('Head', (_message.Message,), {
  'DESCRIPTOR' : _HEAD,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Head)
  })
_sym_db.RegisterMessage(Head)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {

  'Null' : _reflection.GeneratedProtocolMessageType('Null', (_message.Message,), {
    'DESCRIPTOR' : _ROW_NULL,
    '__module__' : 'sqlflow.proto.sqlflow_pb2'
    # @@protoc_insertion_point(class_scope:proto.Row.Null)
    })
  ,
  'DESCRIPTOR' : _ROW,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Row)
  })
_sym_db.RegisterMessage(Row)
_sym_db.RegisterMessage(Row.Null)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.Message)
  })
_sym_db.RegisterMessage(Message)

EndOfExecution = _reflection.GeneratedProtocolMessageType('EndOfExecution', (_message.Message,), {
  'DESCRIPTOR' : _ENDOFEXECUTION,
  '__module__' : 'sqlflow.proto.sqlflow_pb2'
  # @@protoc_insertion_point(class_scope:proto.EndOfExecution)
  })
_sym_db.RegisterMessage(EndOfExecution)



_SQLFLOW = _descriptor.ServiceDescriptor(
  name='SQLFlow',
  full_name='proto.SQLFlow',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=893,
  serialized_end=996,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='proto.SQLFlow.Run',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Fetch',
    full_name='proto.SQLFlow.Fetch',
    index=1,
    containing_service=None,
    input_type=_FETCHREQUEST,
    output_type=_FETCHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SQLFLOW)

DESCRIPTOR.services_by_name['SQLFlow'] = _SQLFLOW

# @@protoc_insertion_point(module_scope)
