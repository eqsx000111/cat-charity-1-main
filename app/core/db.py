from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


class AbstractBase(Base):

    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    invested_amount: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    fully_invested: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    create_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    close_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session