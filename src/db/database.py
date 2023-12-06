from typing import Annotated

from fastapi import Depends
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.settings import settings

from .orm.database import SQLAlchemyAsync

db = SQLAlchemyAsync(
    database_url=settings.sqlalchemy_database_uri,
    sessionmaker_options={"expire_on_commit": False, "autoflush": False, "autocommit": False},
)
SessionDepends = Annotated[AsyncSession, Depends(db.get_session_generator)]
