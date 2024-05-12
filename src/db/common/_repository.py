from typing import Any

from sqlalchemy.ext.asyncio.session import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, obj: Any) -> None:
        self.session.add(obj)
        await self.session.commit()

    async def delete(self, obj: Any) -> None:
        await self.session.delete(obj)
        await self.session.commit()
