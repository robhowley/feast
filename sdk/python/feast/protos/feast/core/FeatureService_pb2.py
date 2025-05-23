# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feast/core/FeatureService.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'feast/core/FeatureService.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.protos.feast.core import FeatureViewProjection_pb2 as feast_dot_core_dot_FeatureViewProjection__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x66\x65\x61st/core/FeatureService.proto\x12\nfeast.core\x1a\x1fgoogle/protobuf/timestamp.proto\x1a&feast/core/FeatureViewProjection.proto\"l\n\x0e\x46\x65\x61tureService\x12,\n\x04spec\x18\x01 \x01(\x0b\x32\x1e.feast.core.FeatureServiceSpec\x12,\n\x04meta\x18\x02 \x01(\x0b\x32\x1e.feast.core.FeatureServiceMeta\"\xa4\x02\n\x12\x46\x65\x61tureServiceSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x33\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32!.feast.core.FeatureViewProjection\x12\x36\n\x04tags\x18\x04 \x03(\x0b\x32(.feast.core.FeatureServiceSpec.TagsEntry\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\r\n\x05owner\x18\x06 \x01(\t\x12\x31\n\x0elogging_config\x18\x07 \x01(\x0b\x32\x19.feast.core.LoggingConfig\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x12\x46\x65\x61tureServiceMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd1\x08\n\rLoggingConfig\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x02\x12\x45\n\x10\x66ile_destination\x18\x03 \x01(\x0b\x32).feast.core.LoggingConfig.FileDestinationH\x00\x12M\n\x14\x62igquery_destination\x18\x04 \x01(\x0b\x32-.feast.core.LoggingConfig.BigQueryDestinationH\x00\x12M\n\x14redshift_destination\x18\x05 \x01(\x0b\x32-.feast.core.LoggingConfig.RedshiftDestinationH\x00\x12O\n\x15snowflake_destination\x18\x06 \x01(\x0b\x32..feast.core.LoggingConfig.SnowflakeDestinationH\x00\x12I\n\x12\x63ustom_destination\x18\x07 \x01(\x0b\x32+.feast.core.LoggingConfig.CustomDestinationH\x00\x12I\n\x12\x61thena_destination\x18\x08 \x01(\x0b\x32+.feast.core.LoggingConfig.AthenaDestinationH\x00\x12`\n\x1e\x63ouchbase_columnar_destination\x18\t \x01(\x0b\x32\x36.feast.core.LoggingConfig.CouchbaseColumnarDestinationH\x00\x1aS\n\x0f\x46ileDestination\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x1c\n\x14s3_endpoint_override\x18\x02 \x01(\t\x12\x14\n\x0cpartition_by\x18\x03 \x03(\t\x1a(\n\x13\x42igQueryDestination\x12\x11\n\ttable_ref\x18\x01 \x01(\t\x1a)\n\x13RedshiftDestination\x12\x12\n\ntable_name\x18\x01 \x01(\t\x1a\'\n\x11\x41thenaDestination\x12\x12\n\ntable_name\x18\x01 \x01(\t\x1a*\n\x14SnowflakeDestination\x12\x12\n\ntable_name\x18\x01 \x01(\t\x1a\x99\x01\n\x11\x43ustomDestination\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12G\n\x06\x63onfig\x18\x02 \x03(\x0b\x32\x37.feast.core.LoggingConfig.CustomDestination.ConfigEntry\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aS\n\x1c\x43ouchbaseColumnarDestination\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x12\n\ncollection\x18\x03 \x01(\tB\r\n\x0b\x64\x65stination\"I\n\x12\x46\x65\x61tureServiceList\x12\x33\n\x0f\x66\x65\x61tureservices\x18\x01 \x03(\x0b\x32\x1a.feast.core.FeatureServiceBX\n\x10\x66\x65\x61st.proto.coreB\x13\x46\x65\x61tureServiceProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.FeatureService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020feast.proto.coreB\023FeatureServiceProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _globals['_FEATURESERVICESPEC_TAGSENTRY']._loaded_options = None
  _globals['_FEATURESERVICESPEC_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_LOGGINGCONFIG_CUSTOMDESTINATION_CONFIGENTRY']._loaded_options = None
  _globals['_LOGGINGCONFIG_CUSTOMDESTINATION_CONFIGENTRY']._serialized_options = b'8\001'
  _globals['_FEATURESERVICE']._serialized_start=120
  _globals['_FEATURESERVICE']._serialized_end=228
  _globals['_FEATURESERVICESPEC']._serialized_start=231
  _globals['_FEATURESERVICESPEC']._serialized_end=523
  _globals['_FEATURESERVICESPEC_TAGSENTRY']._serialized_start=480
  _globals['_FEATURESERVICESPEC_TAGSENTRY']._serialized_end=523
  _globals['_FEATURESERVICEMETA']._serialized_start=526
  _globals['_FEATURESERVICEMETA']._serialized_end=661
  _globals['_LOGGINGCONFIG']._serialized_start=664
  _globals['_LOGGINGCONFIG']._serialized_end=1769
  _globals['_LOGGINGCONFIG_FILEDESTINATION']._serialized_start=1260
  _globals['_LOGGINGCONFIG_FILEDESTINATION']._serialized_end=1343
  _globals['_LOGGINGCONFIG_BIGQUERYDESTINATION']._serialized_start=1345
  _globals['_LOGGINGCONFIG_BIGQUERYDESTINATION']._serialized_end=1385
  _globals['_LOGGINGCONFIG_REDSHIFTDESTINATION']._serialized_start=1387
  _globals['_LOGGINGCONFIG_REDSHIFTDESTINATION']._serialized_end=1428
  _globals['_LOGGINGCONFIG_ATHENADESTINATION']._serialized_start=1430
  _globals['_LOGGINGCONFIG_ATHENADESTINATION']._serialized_end=1469
  _globals['_LOGGINGCONFIG_SNOWFLAKEDESTINATION']._serialized_start=1471
  _globals['_LOGGINGCONFIG_SNOWFLAKEDESTINATION']._serialized_end=1513
  _globals['_LOGGINGCONFIG_CUSTOMDESTINATION']._serialized_start=1516
  _globals['_LOGGINGCONFIG_CUSTOMDESTINATION']._serialized_end=1669
  _globals['_LOGGINGCONFIG_CUSTOMDESTINATION_CONFIGENTRY']._serialized_start=1624
  _globals['_LOGGINGCONFIG_CUSTOMDESTINATION_CONFIGENTRY']._serialized_end=1669
  _globals['_LOGGINGCONFIG_COUCHBASECOLUMNARDESTINATION']._serialized_start=1671
  _globals['_LOGGINGCONFIG_COUCHBASECOLUMNARDESTINATION']._serialized_end=1754
  _globals['_FEATURESERVICELIST']._serialized_start=1771
  _globals['_FEATURESERVICELIST']._serialized_end=1844
# @@protoc_insertion_point(module_scope)
