# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/vocab.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clarifai.rest.grpc.proto.clarifai.api import common_pb2 as proto_dot_clarifai_dot_api_dot_common__pb2
from clarifai.rest.grpc.proto.clarifai.api import concept_pb2 as proto_dot_clarifai_dot_api_dot_concept__pb2
from clarifai.rest.grpc.proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2
from clarifai.rest.grpc.proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/vocab.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1eproto/clarifai/api/vocab.proto\x12\x0c\x63larifai.api\x1a\x1fproto/clarifai/api/common.proto\x1a proto/clarifai/api/concept.proto\x1a&proto/clarifai/api/status/status.proto\x1a)proto/clarifai/api/utils/extensions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"v\n\x05Vocab\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"T\n\x0fGetVocabRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x10\n\x08vocab_id\x18\x02 \x01(\t\"d\n\x11ListVocabsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\x10\n\x08per_page\x18\x03 \x01(\r\"i\n\x11PostVocabsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12#\n\x06vocabs\x18\x02 \x03(\x0b\x32\x13.clarifai.api.Vocab\"z\n\x12PatchVocabsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12#\n\x06vocabs\x18\x02 \x03(\x0b\x32\x13.clarifai.api.Vocab\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\"W\n\x12\x44\x65leteVocabRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x10\n\x08vocab_id\x18\x02 \x01(\t\"g\n\x13\x44\x65leteVocabsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x0b\n\x03ids\x18\x02 \x03(\t\x12\x12\n\ndelete_all\x18\x03 \x01(\x08\"}\n\x18ListVocabConceptsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x10\n\x08vocab_id\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\r\x12\x10\n\x08per_page\x18\x04 \x01(\r\"\x86\x01\n\x18PostVocabConceptsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x10\n\x08vocab_id\x18\x02 \x01(\t\x12\'\n\x08\x63oncepts\x18\x03 \x03(\x0b\x32\x15.clarifai.api.Concept\"r\n\x19\x44\x65leteVocabConceptRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x10\n\x08vocab_id\x18\x02 \x01(\t\x12\x12\n\nconcept_id\x18\x03 \x01(\t\"\x80\x01\n\x1a\x44\x65leteVocabConceptsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x10\n\x08vocab_id\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t\x12\x12\n\ndelete_all\x18\x04 \x01(\x08\"f\n\x13SingleVocabResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12\"\n\x05vocab\x18\x02 \x01(\x0b\x32\x13.clarifai.api.Vocab\"l\n\x12MultiVocabResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12)\n\x06vocabs\x18\x02 \x03(\x0b\x32\x13.clarifai.api.VocabB\x04\x80\xb5\x18\x01\x42$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_common__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_concept__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VOCAB = _descriptor.Descriptor(
  name='Vocab',
  full_name='clarifai.api.Vocab',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.Vocab.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='clarifai.api.Vocab.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='clarifai.api.Vocab.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='clarifai.api.Vocab.app_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='clarifai.api.Vocab.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=349,
)


_GETVOCABREQUEST = _descriptor.Descriptor(
  name='GetVocabRequest',
  full_name='clarifai.api.GetVocabRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetVocabRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_id', full_name='clarifai.api.GetVocabRequest.vocab_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=435,
)


_LISTVOCABSREQUEST = _descriptor.Descriptor(
  name='ListVocabsRequest',
  full_name='clarifai.api.ListVocabsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.ListVocabsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.ListVocabsRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.ListVocabsRequest.per_page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=537,
)


_POSTVOCABSREQUEST = _descriptor.Descriptor(
  name='PostVocabsRequest',
  full_name='clarifai.api.PostVocabsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostVocabsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocabs', full_name='clarifai.api.PostVocabsRequest.vocabs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=644,
)


_PATCHVOCABSREQUEST = _descriptor.Descriptor(
  name='PatchVocabsRequest',
  full_name='clarifai.api.PatchVocabsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PatchVocabsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocabs', full_name='clarifai.api.PatchVocabsRequest.vocabs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='clarifai.api.PatchVocabsRequest.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=646,
  serialized_end=768,
)


_DELETEVOCABREQUEST = _descriptor.Descriptor(
  name='DeleteVocabRequest',
  full_name='clarifai.api.DeleteVocabRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.DeleteVocabRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_id', full_name='clarifai.api.DeleteVocabRequest.vocab_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=857,
)


_DELETEVOCABSREQUEST = _descriptor.Descriptor(
  name='DeleteVocabsRequest',
  full_name='clarifai.api.DeleteVocabsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.DeleteVocabsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ids', full_name='clarifai.api.DeleteVocabsRequest.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_all', full_name='clarifai.api.DeleteVocabsRequest.delete_all', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=962,
)


_LISTVOCABCONCEPTSREQUEST = _descriptor.Descriptor(
  name='ListVocabConceptsRequest',
  full_name='clarifai.api.ListVocabConceptsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.ListVocabConceptsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_id', full_name='clarifai.api.ListVocabConceptsRequest.vocab_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.ListVocabConceptsRequest.page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.ListVocabConceptsRequest.per_page', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=964,
  serialized_end=1089,
)


_POSTVOCABCONCEPTSREQUEST = _descriptor.Descriptor(
  name='PostVocabConceptsRequest',
  full_name='clarifai.api.PostVocabConceptsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostVocabConceptsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_id', full_name='clarifai.api.PostVocabConceptsRequest.vocab_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concepts', full_name='clarifai.api.PostVocabConceptsRequest.concepts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1092,
  serialized_end=1226,
)


_DELETEVOCABCONCEPTREQUEST = _descriptor.Descriptor(
  name='DeleteVocabConceptRequest',
  full_name='clarifai.api.DeleteVocabConceptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.DeleteVocabConceptRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_id', full_name='clarifai.api.DeleteVocabConceptRequest.vocab_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='clarifai.api.DeleteVocabConceptRequest.concept_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1228,
  serialized_end=1342,
)


_DELETEVOCABCONCEPTSREQUEST = _descriptor.Descriptor(
  name='DeleteVocabConceptsRequest',
  full_name='clarifai.api.DeleteVocabConceptsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.DeleteVocabConceptsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_id', full_name='clarifai.api.DeleteVocabConceptsRequest.vocab_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ids', full_name='clarifai.api.DeleteVocabConceptsRequest.ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_all', full_name='clarifai.api.DeleteVocabConceptsRequest.delete_all', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1345,
  serialized_end=1473,
)


_SINGLEVOCABRESPONSE = _descriptor.Descriptor(
  name='SingleVocabResponse',
  full_name='clarifai.api.SingleVocabResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.SingleVocabResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab', full_name='clarifai.api.SingleVocabResponse.vocab', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1475,
  serialized_end=1577,
)


_MULTIVOCABRESPONSE = _descriptor.Descriptor(
  name='MultiVocabResponse',
  full_name='clarifai.api.MultiVocabResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiVocabResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocabs', full_name='clarifai.api.MultiVocabResponse.vocabs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1579,
  serialized_end=1687,
)

_VOCAB.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETVOCABREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_LISTVOCABSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTVOCABSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTVOCABSREQUEST.fields_by_name['vocabs'].message_type = _VOCAB
_PATCHVOCABSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_PATCHVOCABSREQUEST.fields_by_name['vocabs'].message_type = _VOCAB
_DELETEVOCABREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_DELETEVOCABSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_LISTVOCABCONCEPTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTVOCABCONCEPTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTVOCABCONCEPTSREQUEST.fields_by_name['concepts'].message_type = proto_dot_clarifai_dot_api_dot_concept__pb2._CONCEPT
_DELETEVOCABCONCEPTREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_DELETEVOCABCONCEPTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_SINGLEVOCABRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_SINGLEVOCABRESPONSE.fields_by_name['vocab'].message_type = _VOCAB
_MULTIVOCABRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTIVOCABRESPONSE.fields_by_name['vocabs'].message_type = _VOCAB
DESCRIPTOR.message_types_by_name['Vocab'] = _VOCAB
DESCRIPTOR.message_types_by_name['GetVocabRequest'] = _GETVOCABREQUEST
DESCRIPTOR.message_types_by_name['ListVocabsRequest'] = _LISTVOCABSREQUEST
DESCRIPTOR.message_types_by_name['PostVocabsRequest'] = _POSTVOCABSREQUEST
DESCRIPTOR.message_types_by_name['PatchVocabsRequest'] = _PATCHVOCABSREQUEST
DESCRIPTOR.message_types_by_name['DeleteVocabRequest'] = _DELETEVOCABREQUEST
DESCRIPTOR.message_types_by_name['DeleteVocabsRequest'] = _DELETEVOCABSREQUEST
DESCRIPTOR.message_types_by_name['ListVocabConceptsRequest'] = _LISTVOCABCONCEPTSREQUEST
DESCRIPTOR.message_types_by_name['PostVocabConceptsRequest'] = _POSTVOCABCONCEPTSREQUEST
DESCRIPTOR.message_types_by_name['DeleteVocabConceptRequest'] = _DELETEVOCABCONCEPTREQUEST
DESCRIPTOR.message_types_by_name['DeleteVocabConceptsRequest'] = _DELETEVOCABCONCEPTSREQUEST
DESCRIPTOR.message_types_by_name['SingleVocabResponse'] = _SINGLEVOCABRESPONSE
DESCRIPTOR.message_types_by_name['MultiVocabResponse'] = _MULTIVOCABRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vocab = _reflection.GeneratedProtocolMessageType('Vocab', (_message.Message,), dict(
  DESCRIPTOR = _VOCAB,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.Vocab)
  ))
_sym_db.RegisterMessage(Vocab)

GetVocabRequest = _reflection.GeneratedProtocolMessageType('GetVocabRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVOCABREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetVocabRequest)
  ))
_sym_db.RegisterMessage(GetVocabRequest)

ListVocabsRequest = _reflection.GeneratedProtocolMessageType('ListVocabsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTVOCABSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListVocabsRequest)
  ))
_sym_db.RegisterMessage(ListVocabsRequest)

PostVocabsRequest = _reflection.GeneratedProtocolMessageType('PostVocabsRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTVOCABSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostVocabsRequest)
  ))
_sym_db.RegisterMessage(PostVocabsRequest)

PatchVocabsRequest = _reflection.GeneratedProtocolMessageType('PatchVocabsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PATCHVOCABSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PatchVocabsRequest)
  ))
_sym_db.RegisterMessage(PatchVocabsRequest)

DeleteVocabRequest = _reflection.GeneratedProtocolMessageType('DeleteVocabRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVOCABREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.DeleteVocabRequest)
  ))
_sym_db.RegisterMessage(DeleteVocabRequest)

DeleteVocabsRequest = _reflection.GeneratedProtocolMessageType('DeleteVocabsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVOCABSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.DeleteVocabsRequest)
  ))
_sym_db.RegisterMessage(DeleteVocabsRequest)

ListVocabConceptsRequest = _reflection.GeneratedProtocolMessageType('ListVocabConceptsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTVOCABCONCEPTSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListVocabConceptsRequest)
  ))
_sym_db.RegisterMessage(ListVocabConceptsRequest)

PostVocabConceptsRequest = _reflection.GeneratedProtocolMessageType('PostVocabConceptsRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTVOCABCONCEPTSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostVocabConceptsRequest)
  ))
_sym_db.RegisterMessage(PostVocabConceptsRequest)

DeleteVocabConceptRequest = _reflection.GeneratedProtocolMessageType('DeleteVocabConceptRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVOCABCONCEPTREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.DeleteVocabConceptRequest)
  ))
_sym_db.RegisterMessage(DeleteVocabConceptRequest)

DeleteVocabConceptsRequest = _reflection.GeneratedProtocolMessageType('DeleteVocabConceptsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVOCABCONCEPTSREQUEST,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.DeleteVocabConceptsRequest)
  ))
_sym_db.RegisterMessage(DeleteVocabConceptsRequest)

SingleVocabResponse = _reflection.GeneratedProtocolMessageType('SingleVocabResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEVOCABRESPONSE,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.SingleVocabResponse)
  ))
_sym_db.RegisterMessage(SingleVocabResponse)

MultiVocabResponse = _reflection.GeneratedProtocolMessageType('MultiVocabResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTIVOCABRESPONSE,
  __module__ = 'proto.clarifai.api.vocab_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiVocabResponse)
  ))
_sym_db.RegisterMessage(MultiVocabResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
_MULTIVOCABRESPONSE.fields_by_name['vocabs'].has_options = True
_MULTIVOCABRESPONSE.fields_by_name['vocabs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
# @@protoc_insertion_point(module_scope)