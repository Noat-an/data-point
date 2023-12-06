from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, field_validator


class Test(BaseModel):
    id: UUID
    create_stamp: datetime
    amount: int

    class Config:
        from_attributes = True

    @field_validator('amount')
    @classmethod
    def count_mustbe_not_zero(cls, v: int) -> str:
        if v <= 0:
            raise ValueError('Amount must be greater than 0.')
        return v
