# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: installed_protos/v1/api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="installed_protos/v1/api.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1dinstalled_protos/v1/api.proto""\n\x12SimpleAPIleMessage\x12\x0c\n\x04name\x18\x01 \x01(\t2F\n\nAPIService\x12\x38\n\x0cGetSomething\x12\x13.SimpleAPIleMessage\x1a\x13.SimpleAPIleMessageb\x06proto3',
)


_SIMPLEAPILEMESSAGE = _descriptor.Descriptor(
    name="SimpleAPIleMessage",
    full_name="SimpleAPIleMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="SimpleAPIleMessage.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=33,
    serialized_end=67,
)

DESCRIPTOR.message_types_by_name["SimpleAPIleMessage"] = _SIMPLEAPILEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleAPIleMessage = _reflection.GeneratedProtocolMessageType(
    "SimpleAPIleMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIMPLEAPILEMESSAGE,
        "__module__": "installed_protos.v1.api_pb2"
        # @@protoc_insertion_point(class_scope:SimpleAPIleMessage)
    },
)
_sym_db.RegisterMessage(SimpleAPIleMessage)


_APISERVICE = _descriptor.ServiceDescriptor(
    name="APIService",
    full_name="APIService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=69,
    serialized_end=139,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetSomething",
            full_name="APIService.GetSomething",
            index=0,
            containing_service=None,
            input_type=_SIMPLEAPILEMESSAGE,
            output_type=_SIMPLEAPILEMESSAGE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_APISERVICE)

DESCRIPTOR.services_by_name["APIService"] = _APISERVICE

# @@protoc_insertion_point(module_scope)