from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel


class Owner(BaseModel):
    id: UUID
    name: str
    email: str
