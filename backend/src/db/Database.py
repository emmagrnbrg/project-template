import os
import urllib.parse
from typing import Any, AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import declarative_base

from ..Settings import Settings

load_dotenv()

def get_database_url() -> str:
    load_dotenv()

    user = os.getenv(Settings.POSTGRES_USER)
    password = os.getenv(Settings.POSTGRES_PASSWORD)
    host = os.getenv(Settings.POSTGRES_HOST)
    port = os.getenv(Settings.POSTGRES_PORT)
    db = os.getenv(Settings.POSTGRES_DB)

    if not all([user, password, host, port, db]):
        raise RuntimeError("Database environment variables are not set")

    password = urllib.parse.quote_plus(password)

    return (
        f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
    )

def get_engine(echo: bool = False) -> AsyncEngine:
    return create_async_engine(
        get_database_url(),
        echo=echo,
    )

async_session = async_sessionmaker(get_engine(), expire_on_commit=False)

BaseEntity = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session() as session:
        yield session
