import typing as t

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.engine import url as sa_url

from config import settings


class Db:
    def __init__(self):
        self.engine = None
        self.session_maker = None

    async def setup(self, dsn: t.Optional[str] = None):
        if self.session_maker is not None:
            return
        if dsn is None:
            dsn = sa_url.URL(
                "postgresql+asyncpg",
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                database=settings.POSTGRES_DB,
                username=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                query={},
            )
        self.engine = create_async_engine(dsn)
        self.session_maker = async_sessionmaker(self.engine)

    async def release(self):
        if self.engine is not None:
            await self.engine.dispose()


db = Db()
