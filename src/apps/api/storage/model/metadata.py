from datetime import datetime
from typing import Optional
from uuid import uuid4
import enum

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db import db
from src.db.common._mixin import TableModelMixin


class StorageType(enum.Enum):
    """
    Enum class storage type
    """
    googleDrive = "GoogleDrive"
    yandexDisk = "YandexDisk"


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
    email: Mapped[str] = mapped_column(sa.TEXT, comment="электронная почта")
    inner_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата добавления",
        default=datetime.now
    )
    is_deleted: Mapped[bool] = mapped_column(
        sa.Boolean, nullable=False,
        comment="Пометка удаления", default=False
    )


class Storage(TableModelMixin, db.Base):
    __tablename__ = "storage"
    __table_args__ = {
        "comment": "Справочник доступных дата-продуктов",
    }
    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор"
    )
    owner_id: Mapped[Optional[str]] = mapped_column(
        sa.ForeignKey("storage_owner.id", ondelete="SET NULL"),
        comment="id владельца хранилища"
    )
    type: Mapped[StorageType]
    service_account_info: Mapped[str] = mapped_column(
        sa.TEXT,
        comment="инфа для коннекта"
    )  # TODO надо подумать как хранить пока просто тексто
    url: Mapped[str] = mapped_column(
        sa.String, nullable=False, 
        comment="URL источника"
    )
    inner_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата добавления",
        default=datetime.now
    )
    is_deleted: Mapped[bool] = mapped_column(
        sa.Boolean, nullable=False,
        comment="Пометка удаления", default=False
    )
