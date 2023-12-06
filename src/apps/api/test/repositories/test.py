import sqlalchemy as sa

from apps.api.test import model
from db.common._repository import BaseRepository


class TestRepository(BaseRepository):

    async def get_list(self) -> list[model.Test]:
        stmt = await self.session.execute(
            sa.selectTest)
        return stmt.scalars().all()

    async def add(self, obj: model.Test) -> None:
        return await super().add(obj)
