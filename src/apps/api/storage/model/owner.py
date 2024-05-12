from datetime import datetime
from typing import Optional
from uuid import uuid4
import enum

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db import db
from src.db.common._mixin import TableModelMixin


class StorageOwner(TableModelMixin, db.Base):
    __tablename__ = "storage_owner"
    __table_args__ = {
        "comment": "Справочник владельцев",
    }
    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор"
    )
    name: Mapped[str] = mapped_column(sa.TEXT, comment="Имя владельца")
    email: Mapped[str] = mapped_column(sa.TEXT, comment="электронная почта") # накинуть индекс уникальности
    inner_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата добавления",
        default=datetime.now
    )
    is_deleted: Mapped[bool] = mapped_column(
        sa.Boolean, nullable=False,
        comment="Пометка удаления", default=False
    )
