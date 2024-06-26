from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

# async_engine = create_async_engine(
#     url=settings.DATABASE_URL_asyncpg,
#     echo=True,
# )
#
# session_factory = sessionmaker(engine)
# async_session_factory = async_sessionmaker(async_engine)
#
