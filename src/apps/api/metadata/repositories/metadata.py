import sqlalchemy as sa

from src.apps.api.metadata import model
from src.db.common._repository import BaseRepository


class TestRepository(BaseRepository):

    async def get_list(self) -> list[model.Test]:
        result = await self.session.execute(
            sa.select(
                model.Test.id,
                model.Test.create_stamp,
                model.Test.amount
            )
        )
        return result.all()

    async def add_test_row(self, obj: model.Test) -> None:
        return await super().add(obj)
