import sqlalchemy as sa

from src.apps.api.storage import model
from src.db.common._repository import BaseRepository


class RemoteStorageRepository(BaseRepository):

    async def get_storage_list(self, owner_id) -> list[model.Storage]:
        stmt = await self.session.execute(
            sa.select(
                model.Storage.type,
                model.Storage.id,
                model.Storage.is_deleted
            ).where(
                model.Storage.owner_id == owner_id
            )
        )
        return stmt.all()

    async def add_storage(self, obj: model.Storage) -> None:
        return await super().add(obj)
