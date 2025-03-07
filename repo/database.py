from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs, AsyncSession
from repo.config.config import settings
from typing import Annotated, AsyncGenerator

DATABASE_URL = settings.get_db_url()

engine = create_async_engine(url=DATABASE_URL)
async_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True, index=True, autoincrement=True)]

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int_pk]

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
