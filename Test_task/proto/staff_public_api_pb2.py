# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cron/internal/proto/staff-public-api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cron/internal/proto/staff-public-api.proto\x12\x35ozon.kdp.api.staff_public_api.api.staff_public_api.v1\x1a\x1cgoogle/api/annotations.proto\"j\n\x1dGetEmployeesByOrgGuidsRequest\x12\r\n\x05guids\x18\x01 \x03(\t\x12\x11\n\trecursive\x18\x02 \x01(\x08\x12\x10\n\x08mainOnly\x18\x03 \x01(\x08\x12\x15\n\rcompanyPrefix\x18\x04 \x01(\t\"\x93\x02\n\x1eGetEmployeesByOrgGuidsResponse\x12x\n\x0corgEmployees\x18\x01 \x03(\x0b\x32\x62.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetEmployeesByOrgGuidsResponse.OrgEmployees\x1aw\n\x0cOrgEmployees\x12\x0f\n\x07orgGuid\x18\x01 \x01(\t\x12V\n\temployees\x18\x02 \x03(\x0b\x32\x43.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.StaffProfile\"4\n#GetEmployeesAmountByOrgGuidsRequest\x12\r\n\x05guids\x18\x01 \x03(\t\"\xae\x02\n$GetEmployeesAmountByOrgGuidsResponse\x12\x84\x01\n\x0corgEmployees\x18\x01 \x03(\x0b\x32n.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetEmployeesAmountByOrgGuidsResponse.OrgEmployeesAmount\x1a\x7f\n\x12OrgEmployeesAmount\x12P\n\x03org\x18\x01 \x01(\x0b\x32\x43.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.OrgStructure\x12\x17\n\x0f\x65mployeesAmount\x18\x02 \x01(\x05\"/\n\x1eGetHeadsVerticalByLoginRequest\x12\r\n\x05login\x18\x01 \x01(\t\"u\n\x1fGetHeadsVerticalByLoginResponse\x12R\n\x05heads\x18\x01 \x03(\x0b\x32\x43.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.ShortProfile\"+\n\x0cOrgStructure\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\"\xb1\x01\n\x0cStaffProfile\x12M\n\x06person\x18\x01 \x01(\x0b\x32=.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Person\x12R\n\temployees\x18\x02 \x03(\x0b\x32?.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Employee\"\xbd\x07\n\x08\x45mployee\x12\x10\n\x08personId\x18\x01 \x01(\x03\x12\x0c\n\x04guid\x18\x02 \x01(\t\x12Q\n\x08position\x18\x03 \x01(\x0b\x32?.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Position\x12P\n\x03org\x18\x04 \x01(\x0b\x32\x43.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.OrgStructure\x12I\n\x04\x63ity\x18\x05 \x01(\x0b\x32;.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.City\x12O\n\x07\x63ompany\x18\x06 \x01(\x0b\x32>.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Company\x12M\n\x06street\x18\x07 \x01(\x0b\x32=.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Street\x12W\n\x0bsubdivision\x18\x08 \x01(\x0b\x32\x42.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Subdivision\x12K\n\x04head\x18\t \x01(\x0b\x32=.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Person\x12K\n\x04hrBp\x18\n \x01(\x0b\x32=.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Person\x12\x0e\n\x06isMain\x18\x0b \x01(\x08\x12\x0e\n\x06isHead\x18\x0c \x01(\x08\x12\x16\n\x0e\x65mployeeNumber\x18\r \x01(\t\x12U\n\ncostCenter\x18\x0e \x01(\x0b\x32\x41.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.CostCenter\x12U\n\x06status\x18\x0f \x01(\x0b\x32\x45.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.EmployeeStatus\x12\x14\n\x0cworkTimeRate\x18\x10 \x01(\x02\x12\x12\n\npersonGuid\x18\x11 \x01(\t\"(\n\x07\x43ompany\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06prefix\x18\x02 \x01(\t\"#\n\x04\x43ity\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04guid\x18\x02 \x01(\t\"%\n\x06Street\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04guid\x18\x02 \x01(\t\"*\n\x0bSubdivision\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04guid\x18\x02 \x01(\t\")\n\nCostCenter\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04guid\x18\x02 \x01(\t\"\'\n\x08Position\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\"+\n\x0e\x45mployeeStatus\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\"\x85\x02\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\npersonGuid\x18\x02 \x01(\t\x12\r\n\x05login\x18\x03 \x01(\t\x12\x10\n\x08photoUrl\x18\x04 \x01(\t\x12\x10\n\x08\x66ullName\x18\x05 \x01(\t\x12Q\n\x08\x63ontacts\x18\x06 \x01(\x0b\x32?.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Contacts\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0f\n\x07surname\x18\x08 \x01(\t\x12\x12\n\npatronymic\x18\t \x01(\t\x12\x10\n\x08\x62irthday\x18\n \x01(\t\x12\x10\n\x08isRemote\x18\x0b \x01(\x08\"~\n\x08\x43ontacts\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05phone\x18\x02 \x01(\t\x12\r\n\x05slack\x18\x03 \x01(\t\x12\r\n\x05teams\x18\x04 \x01(\t\x12\x10\n\x08telegram\x18\x05 \x01(\t\x12\x11\n\tonecPhone\x18\x06 \x01(\t\x12\x11\n\tworkPhone\x18\x07 \x01(\t\"\xd3\x02\n\x0cShortProfile\x12M\n\x06person\x18\x01 \x01(\x0b\x32=.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Person\x12Q\n\x08position\x18\x02 \x01(\x0b\x32?.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Position\x12P\n\x03org\x18\x03 \x01(\x0b\x32\x43.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.OrgStructure\x12O\n\x07\x63ompany\x18\x04 \x01(\x0b\x32>.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.Company2\xde\x05\n\x0eStaffPublicAPI\x12\xdd\x01\n\x16GetEmployeesByOrgGuids\x12T.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetEmployeesByOrgGuidsRequest\x1aU.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetEmployeesByOrgGuidsResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/employees/org\x12\xf6\x01\n\x1cGetEmployeesAmountByOrgGuids\x12Z.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetEmployeesAmountByOrgGuidsRequest\x1a[.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetEmployeesAmountByOrgGuidsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/org/employees/amount\x12\xf2\x01\n\x17GetHeadsVerticalByLogin\x12U.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetHeadsVerticalByLoginRequest\x1aV.ozon.kdp.api.staff_public_api.api.staff_public_api.v1.GetHeadsVerticalByLoginResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /profiles/heads/{login}/verticalBVZTgitlab.ozon.ru/kdp/api/staff-public-api/pkg/api/staff_public_api/v1;staff_public_apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cron.internal.proto.staff_public_api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZTgitlab.ozon.ru/kdp/api/staff-public-api/pkg/api/staff_public_api/v1;staff_public_api'
  _STAFFPUBLICAPI.methods_by_name['GetEmployeesByOrgGuids']._options = None
  _STAFFPUBLICAPI.methods_by_name['GetEmployeesByOrgGuids']._serialized_options = b'\202\323\344\223\002\020\022\016/employees/org'
  _STAFFPUBLICAPI.methods_by_name['GetEmployeesAmountByOrgGuids']._options = None
  _STAFFPUBLICAPI.methods_by_name['GetEmployeesAmountByOrgGuids']._serialized_options = b'\202\323\344\223\002\027\022\025/org/employees/amount'
  _STAFFPUBLICAPI.methods_by_name['GetHeadsVerticalByLogin']._options = None
  _STAFFPUBLICAPI.methods_by_name['GetHeadsVerticalByLogin']._serialized_options = b'\202\323\344\223\002\"\022 /profiles/heads/{login}/vertical'
  _GETEMPLOYEESBYORGGUIDSREQUEST._serialized_start=131
  _GETEMPLOYEESBYORGGUIDSREQUEST._serialized_end=237
  _GETEMPLOYEESBYORGGUIDSRESPONSE._serialized_start=240
  _GETEMPLOYEESBYORGGUIDSRESPONSE._serialized_end=515
  _GETEMPLOYEESBYORGGUIDSRESPONSE_ORGEMPLOYEES._serialized_start=396
  _GETEMPLOYEESBYORGGUIDSRESPONSE_ORGEMPLOYEES._serialized_end=515
  _GETEMPLOYEESAMOUNTBYORGGUIDSREQUEST._serialized_start=517
  _GETEMPLOYEESAMOUNTBYORGGUIDSREQUEST._serialized_end=569
  _GETEMPLOYEESAMOUNTBYORGGUIDSRESPONSE._serialized_start=572
  _GETEMPLOYEESAMOUNTBYORGGUIDSRESPONSE._serialized_end=874
  _GETEMPLOYEESAMOUNTBYORGGUIDSRESPONSE_ORGEMPLOYEESAMOUNT._serialized_start=747
  _GETEMPLOYEESAMOUNTBYORGGUIDSRESPONSE_ORGEMPLOYEESAMOUNT._serialized_end=874
  _GETHEADSVERTICALBYLOGINREQUEST._serialized_start=876
  _GETHEADSVERTICALBYLOGINREQUEST._serialized_end=923
  _GETHEADSVERTICALBYLOGINRESPONSE._serialized_start=925
  _GETHEADSVERTICALBYLOGINRESPONSE._serialized_end=1042
  _ORGSTRUCTURE._serialized_start=1044
  _ORGSTRUCTURE._serialized_end=1087
  _STAFFPROFILE._serialized_start=1090
  _STAFFPROFILE._serialized_end=1267
  _EMPLOYEE._serialized_start=1270
  _EMPLOYEE._serialized_end=2227
  _COMPANY._serialized_start=2229
  _COMPANY._serialized_end=2269
  _CITY._serialized_start=2271
  _CITY._serialized_end=2306
  _STREET._serialized_start=2308
  _STREET._serialized_end=2345
  _SUBDIVISION._serialized_start=2347
  _SUBDIVISION._serialized_end=2389
  _COSTCENTER._serialized_start=2391
  _COSTCENTER._serialized_end=2432
  _POSITION._serialized_start=2434
  _POSITION._serialized_end=2473
  _EMPLOYEESTATUS._serialized_start=2475
  _EMPLOYEESTATUS._serialized_end=2518
  _PERSON._serialized_start=2521
  _PERSON._serialized_end=2782
  _CONTACTS._serialized_start=2784
  _CONTACTS._serialized_end=2910
  _SHORTPROFILE._serialized_start=2913
  _SHORTPROFILE._serialized_end=3252
  _STAFFPUBLICAPI._serialized_start=3255
  _STAFFPUBLICAPI._serialized_end=3989
# @@protoc_insertion_point(module_scope)
