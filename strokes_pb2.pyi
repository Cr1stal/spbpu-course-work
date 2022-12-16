from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StrokeReply(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class StrokeRequest(_message.Message):
    __slots__ = ["age", "average_glucose_level", "body_mass_index", "ever_married", "gender", "heart_disease", "hypertension", "residence_type", "smoking_status", "work_type"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_GLUCOSE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BODY_MASS_INDEX_FIELD_NUMBER: _ClassVar[int]
    EVER_MARRIED_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    HEART_DISEASE_FIELD_NUMBER: _ClassVar[int]
    HYPERTENSION_FIELD_NUMBER: _ClassVar[int]
    RESIDENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SMOKING_STATUS_FIELD_NUMBER: _ClassVar[int]
    WORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    age: int
    average_glucose_level: int
    body_mass_index: int
    ever_married: str
    gender: str
    heart_disease: bool
    hypertension: bool
    residence_type: str
    smoking_status: str
    work_type: str
    def __init__(self, gender: _Optional[str] = ..., age: _Optional[int] = ..., hypertension: bool = ..., heart_disease: bool = ..., ever_married: _Optional[str] = ..., work_type: _Optional[str] = ..., residence_type: _Optional[str] = ..., average_glucose_level: _Optional[int] = ..., body_mass_index: _Optional[int] = ..., smoking_status: _Optional[str] = ...) -> None: ...
