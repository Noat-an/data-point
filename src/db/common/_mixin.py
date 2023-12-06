import sqlalchemy as sa


class TableModelMixin:
    __table__: sa.Table

    def __repr__(self) -> str:
        return str(self.to_dict())

    def to_dict(self) -> dict:
        """Model to dict"""
        data = {}
        for column in self.__table__.columns:
            data[column.name] = getattr(self, column.name)
        return data
