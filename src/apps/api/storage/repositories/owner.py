import sqlalchemy as sa

from src.apps.api.storage import model
from src.db.common._repository import BaseRepository


class OwnerRepository(BaseRepository):

    async def add_owner(self, obj: model.StorageOwner) -> None:
        return await super().add(obj)

    async def get_owner(self, owner_id: str):
        stmt = await self.session.execute(
            sa.select(
                model.StorageOwner.id,
                model.StorageOwner.name,
                model.StorageOwner.email
            ).where(
                model.StorageOwner.id == owner_id
            )
        )
        return stmt.all()
