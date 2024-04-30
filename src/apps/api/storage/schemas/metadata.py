from __future__ import annotations

from pydantic import BaseModel


class StorageList(BaseModel):
    type: str
    id: str
    is_deleted: bool


class Storage(BaseModel):
    owner_id: str
    type: str
    service_account_info: str
