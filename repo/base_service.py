from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

class BaseService:
    model = None

    @classmethod
    async def create(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
            await session.refresh(new_instance)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance

    @classmethod
    async def get(cls, session: AsyncSession, id: int):
        instance = await session.get(cls.model, id)
        if not instance:
            raise ValueError(f"{cls.model.__name__} with id={id} not found")
        return instance

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values):
        instance = await session.get(cls.model, id)
        if not instance:
            raise ValueError(f"{cls.model.__name__} with id={id} not found")

        for k, v in values.items():
            setattr(instance, k, v)

        try:
            await session.commit()
            await session.refresh(instance)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return instance

    @classmethod
    async def delete(cls, session: AsyncSession, id: int):
        instance = await session.get(cls.model, id)
        if not instance:
            raise ValueError(f"{cls.model.__name__} with id={id} not found")
        try:
            await session.delete(instance)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return {"message": f"{cls.model.__name__} deleted successfully"}