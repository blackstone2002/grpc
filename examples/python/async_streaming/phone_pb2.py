# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phone.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='phone.proto',
  package='grpc.testing',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0bphone.proto\x12\x0cgrpc.testing\"-\n\x08\x43\x61llInfo\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\r\n\x05media\x18\x02 \x01(\t\"q\n\tCallState\x12,\n\x05state\x18\x02 \x01(\x0e\x32\x1d.grpc.testing.CallState.State\"6\n\x05State\x12\r\n\tUNDEFINED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x06\x12\t\n\x05\x45NDED\x10\x07\")\n\x11StreamCallRequest\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\"\x88\x01\n\x12StreamCallResponse\x12+\n\tcall_info\x18\x01 \x01(\x0b\x32\x16.grpc.testing.CallInfoH\x00\x12-\n\ncall_state\x18\x02 \x01(\x0b\x32\x17.grpc.testing.CallStateH\x00\x42\x16\n\x14stream_call_response2\\\n\x05Phone\x12S\n\nStreamCall\x12\x1f.grpc.testing.StreamCallRequest\x1a .grpc.testing.StreamCallResponse(\x01\x30\x01\x62\x06proto3'
)



_CALLSTATE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='grpc.testing.CallState.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDED', index=3, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=135,
  serialized_end=189,
)
_sym_db.RegisterEnumDescriptor(_CALLSTATE_STATE)


_CALLINFO = _descriptor.Descriptor(
  name='CallInfo',
  full_name='grpc.testing.CallInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='grpc.testing.CallInfo.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media', full_name='grpc.testing.CallInfo.media', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=29,
  serialized_end=74,
)


_CALLSTATE = _descriptor.Descriptor(
  name='CallState',
  full_name='grpc.testing.CallState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='grpc.testing.CallState.state', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CALLSTATE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=189,
)


_STREAMCALLREQUEST = _descriptor.Descriptor(
  name='StreamCallRequest',
  full_name='grpc.testing.StreamCallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='grpc.testing.StreamCallRequest.phone_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=191,
  serialized_end=232,
)


_STREAMCALLRESPONSE = _descriptor.Descriptor(
  name='StreamCallResponse',
  full_name='grpc.testing.StreamCallResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_info', full_name='grpc.testing.StreamCallResponse.call_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_state', full_name='grpc.testing.StreamCallResponse.call_state', index=1,
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
    _descriptor.OneofDescriptor(
      name='stream_call_response', full_name='grpc.testing.StreamCallResponse.stream_call_response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=235,
  serialized_end=371,
)

_CALLSTATE.fields_by_name['state'].enum_type = _CALLSTATE_STATE
_CALLSTATE_STATE.containing_type = _CALLSTATE
_STREAMCALLRESPONSE.fields_by_name['call_info'].message_type = _CALLINFO
_STREAMCALLRESPONSE.fields_by_name['call_state'].message_type = _CALLSTATE
_STREAMCALLRESPONSE.oneofs_by_name['stream_call_response'].fields.append(
  _STREAMCALLRESPONSE.fields_by_name['call_info'])
_STREAMCALLRESPONSE.fields_by_name['call_info'].containing_oneof = _STREAMCALLRESPONSE.oneofs_by_name['stream_call_response']
_STREAMCALLRESPONSE.oneofs_by_name['stream_call_response'].fields.append(
  _STREAMCALLRESPONSE.fields_by_name['call_state'])
_STREAMCALLRESPONSE.fields_by_name['call_state'].containing_oneof = _STREAMCALLRESPONSE.oneofs_by_name['stream_call_response']
DESCRIPTOR.message_types_by_name['CallInfo'] = _CALLINFO
DESCRIPTOR.message_types_by_name['CallState'] = _CALLSTATE
DESCRIPTOR.message_types_by_name['StreamCallRequest'] = _STREAMCALLREQUEST
DESCRIPTOR.message_types_by_name['StreamCallResponse'] = _STREAMCALLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CallInfo = _reflection.GeneratedProtocolMessageType('CallInfo', (_message.Message,), {
  'DESCRIPTOR' : _CALLINFO,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.CallInfo)
  })
_sym_db.RegisterMessage(CallInfo)

CallState = _reflection.GeneratedProtocolMessageType('CallState', (_message.Message,), {
  'DESCRIPTOR' : _CALLSTATE,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.CallState)
  })
_sym_db.RegisterMessage(CallState)

StreamCallRequest = _reflection.GeneratedProtocolMessageType('StreamCallRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCALLREQUEST,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.StreamCallRequest)
  })
_sym_db.RegisterMessage(StreamCallRequest)

StreamCallResponse = _reflection.GeneratedProtocolMessageType('StreamCallResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCALLRESPONSE,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.StreamCallResponse)
  })
_sym_db.RegisterMessage(StreamCallResponse)



_PHONE = _descriptor.ServiceDescriptor(
  name='Phone',
  full_name='grpc.testing.Phone',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=373,
  serialized_end=465,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamCall',
    full_name='grpc.testing.Phone.StreamCall',
    index=0,
    containing_service=None,
    input_type=_STREAMCALLREQUEST,
    output_type=_STREAMCALLRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PHONE)

DESCRIPTOR.services_by_name['Phone'] = _PHONE

# @@protoc_insertion_point(module_scope)
