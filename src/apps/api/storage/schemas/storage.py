from __future__ import annotations

from typing import Optional, TypeVar
import enum
from uuid import UUID

from pydantic import BaseModel, field_validator, field_serializer

from src.apps.services.adaptors.google.schemas import GoogleServiceAC


T = TypeVar("T", GoogleServiceAC, dict)


class StorageList(BaseModel):
    type: str
    id: str
    is_deleted: bool


class StorageType(str, enum.Enum):
    """
    Enum class storage type
    """
    googleDrive = "GoogleDrive"
    yandexDisk = "YandexDisk"


class Storage(BaseModel):
    owner_id: UUID
    type: Optional[StorageType] = None
    service_account_info: GoogleServiceAC
    url: str
        
    @field_serializer('service_account_info', when_used='unless-none')
    def serialize_service_in_model(service_account_info: GoogleServiceAC):
        return str(service_account_info.model_dump())

    @field_serializer('type', when_used='always')
    def serialize_type_in_model(self, type: Optional[StorageType]):
        if 'google' in self.url:
            return StorageType.googleDrive.value
        else:
            return StorageType.yandexDisk.value

    class Config:
        use_enum_values = True
