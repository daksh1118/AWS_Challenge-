from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.core.config import settings

# Async SQLAlchemy engine configuration
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency yielding an async SQLAlchemy session.
    Ensures session is properly closed after usage.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
