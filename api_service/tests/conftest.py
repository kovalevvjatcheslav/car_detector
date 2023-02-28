from httpx import AsyncClient
import pytest
import pytest_asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.engine.url import URL

from config import settings
from api_service.main import app
from models import Base
from sources import db

TEST_DB = "test_db"


@pytest.fixture
def client():
    return AsyncClient(app=app, base_url="http://testserver")


@pytest_asyncio.fixture(autouse=True)
async def setup():
    await init_db()
    yield
    await release_db()


async def init_db():
    session_maker, dsn_dict = get_session_maker()
    async with session_maker.begin() as session:
        await session.execute(text(f"DROP DATABASE IF EXISTS {TEST_DB}"))
        await session.execute(text(f"CREATE DATABASE {TEST_DB}"))
    dsn_dict["database"] = TEST_DB
    dsn = URL("postgresql+asyncpg", **dsn_dict)
    await db.setup(dsn)
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def release_db():
    await db.release()
    session_maker, _ = get_session_maker()
    async with session_maker() as session:
        await session.execute(text(f"DROP DATABASE IF EXISTS {TEST_DB}"))


def get_session_maker():
    dsn_dict = dict(
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        database=settings.POSTGRES_DB,
        username=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        query={},
    )
    dsn = URL("postgresql+asyncpg", **dsn_dict)
    engine = create_async_engine(dsn, isolation_level="AUTOCOMMIT")
    return async_sessionmaker(engine), dsn_dict
