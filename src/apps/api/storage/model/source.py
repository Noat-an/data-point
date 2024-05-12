from datetime import datetime
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db import db
from src.db.common._mixin import TableModelMixin


class Source(TableModelMixin, db.Base):
    __tablename__ = "sourse"
    __table_args__ = {
        "comment": "Справочник доступных источников данных",
    }

    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор"
    )
    type_id: Mapped[str] = mapped_column(
        sa.UUID, comment="Уникальный идентификатор типа источника"
    )
    owner_id: Mapped[str] = mapped_column(
        sa.UUID, comment="Уникальный идентификатор владельца"
    )
    url: Mapped[str] = mapped_column(
        sa.String, nullable=False,
        comment="часть URL источника"
    )
    inner_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата добавления",
        default=datetime.now
    )
