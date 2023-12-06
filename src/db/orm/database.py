from typing import Any, AsyncGenerator, Generator

import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from ._base import SQLAlchemy as _SQLAlchemy


class SQLAlchemyAsync(_SQLAlchemy):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._engine = create_async_engine(self._database_url, **self.engine_options)
        self._async_session_factory = async_sessionmaker(self._engine, **self.sessionmaker_options)

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    @property
    def get_session(self) -> async_sessionmaker[AsyncSession]:
        return self._async_session_factory

    async def get_session_generator(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.get_session() as session:
            yield session


class SQLAlchemySync(_SQLAlchemy):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._engine = sa.create_engine(self._database_url, **self.engine_options)
        self._session_factory = so.scoped_session(
            sessionmaker(self._engine, **self.sessionmaker_options)
        )

    def __del__(self) -> None:
        if getattr(self, "_engine", None):
            self._engine.dispose()

    @property
    def engine(self) -> sa.engine.base.Engine:
        return self._engine

    @property
    def get_session(self) -> so.scoped_session[so.Session]:
        return self._session_factory

    def get_session_generator(self) -> Generator:
        with self.get_session() as session:
            yield session
