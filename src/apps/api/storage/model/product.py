from datetime import datetime
from typing import Optional
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db import db
from src.db.common._mixin import TableModelMixin


class Product(TableModelMixin, db.Base):
    __tablename__ = "product"
    __table_args__ = {
        "comment": "Справочник доступных дата-продуктов",
    }

    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор"
    )
    name: Mapped[str] = mapped_column(
        sa.TEXT, comment="Наименование дата-продукта"
    )
    source_id: Mapped[str] = mapped_column(
        sa.UUID, comment="Уникальный идентификатор источника"
    )
    owner_id: Mapped[Optional[str]] = mapped_column(
        sa.ForeignKey("storage_owner.id", ondelete="SET NULL"),
        comment="id владельца хранилища"
    )
    size: Mapped[int] = mapped_column(
        sa.INTEGER, nullable=False, comment="Размер в байтах"
    )
    parts: Mapped[int] = mapped_column(
        sa.INTEGER, nullable=False, comment="Определенных частей относящихся к продукту"
    )
    row: Mapped[int] = mapped_column(
        sa.INTEGER, nullable=False, comment="Количесто записей"
    )
    inner_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата добавления",
        default=datetime.now
    )


class QualityIndex(TableModelMixin, db.Base):
    __tablename__ = "quality_index"
    __table_args__ = {
        "comment": "Справочник показателей качества продукта",
    }
    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор записи"
    )
    name: Mapped[str] = mapped_column(
        sa.TEXT, comment="Наименование показателя"
    )
    limit: Mapped[int] = mapped_column(
        sa.INTEGER, comment="Предельное значение метрики"
    )
    create_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата создания",
        default=datetime.now
    )


class ProductParts(TableModelMixin, db.Base):
    __tablename__ = "parts"
    __table_args__ = {
        "comment": "Состав доступных товаров",
    }
    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор"
    )
    product_id: Mapped[str] = mapped_column(
        sa.ForeignKey("product.id", ondelete="CASCADE"),
        comment="Уникальный идентификатор товара"
    )
    part_num: Mapped[int] = mapped_column(
        sa.INTEGER, comment="порядковый номер части"
    )
    hash_sum: Mapped[int] = mapped_column(sa.INTEGER, nullable=False, comment="хэш сумма")
    size: Mapped[int] = mapped_column(sa.INTEGER, comment="Размер в байтах")
    row: Mapped[int] = mapped_column(sa.INTEGER, comment="Количесто записей")
    inner_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата добавления",
        default=datetime.now
    )
    update_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата обновления",
        default=datetime.now
    )


class PartQuality(TableModelMixin, db.Base):
    __tablename__ = "parts_quality"
    __table_args__ = {
        "comment": "качество партиций дата-продукта",
    }
    id: Mapped[str] = mapped_column(
        sa.UUID, primary_key=True,
        default=uuid4, comment="Уникальный идентификатор записи"
    )
    part_id: Mapped[str] = mapped_column(
        sa.ForeignKey("parts.id", ondelete="CASCADE"),
        comment="Уникальный идентификатор куска"
    )
    metric_id: Mapped[str] = mapped_column(
        sa.ForeignKey("quality_index.id", ondelete="CASCADE"),
        comment="Уникальный идентификатор метрики"
    )
    value: Mapped[int] = mapped_column(
        sa.INTEGER, comment="значение метрики"
    )
    update_stamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP, comment="Дата обновления",
        default=datetime.now
    )
