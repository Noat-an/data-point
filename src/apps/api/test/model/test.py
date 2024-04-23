from datetime import datetime
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db import db
from src.db.common._mixin import TableModelMixin


class Test(TableModelMixin, db.Base):
    __tablename__ = "test"
    __table_args__ = {
        "comment": "Test table",
    }

    id: Mapped[str] = mapped_column(sa.UUID, primary_key=True,
                                    default=uuid4, comment="Уникальный идентификатор")
    create_stamp: Mapped[datetime] = mapped_column(sa.TIMESTAMP,
                                                   comment="Дата создания",
                                                   default=datetime.now)
    amount: Mapped[int] = mapped_column(sa.INTEGER, nullable=False, comment="Сумма")
