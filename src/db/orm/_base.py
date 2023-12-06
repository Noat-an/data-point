import sqlalchemy as sa
from sqlalchemy.orm import registry
from sqlalchemy.orm.decl_api import DeclarativeMeta


class SQLAlchemy:
    def __init__(
        self,
        database_url: str,
        metadata: sa.MetaData | None = None,
        engine_options: dict | None = None,
        sessionmaker_options: dict | None = None,
    ):
        self.Base: DeclarativeMeta = registry(  # pylint: disable=invalid-name
            metadata=metadata
        ).generate_base()
        self._database_url = database_url
        self.engine_options = engine_options or {}
        self.sessionmaker_options = sessionmaker_options or {}

    @property
    def metadata(self) -> sa.MetaData:
        """The metadata from backend.db.Base."""
        return self.Base.metadata

    @property
    def database_url(self) -> str:
        return self._database_url

    @property
    def database_url_as_sync(self) -> str:
        return _change_driver_on_sync(self._database_url)


# utils

_RELATIONSHIP_DRIVERS = (("", "+aiosqlite"), ("+psycopg2", "+asyncpg"))


def _change_driver_on_sync(url: str) -> str:
    """Change on sync driver if current driver async"""
    for dr_sync, dr_async in _RELATIONSHIP_DRIVERS:
        if dr_async in url:
            url = url.replace(dr_async, dr_sync)
            break
    return url
