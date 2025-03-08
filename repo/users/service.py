from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from repo.base_service import BaseService
from repo.models import User, UserGroup, UserSending, UserProperty, UserReportLink, UserRole


class UserService(BaseService):
    model = User

    @classmethod
    async def if_username_exists(cls, session: AsyncSession, username: str) -> bool:
        query = select(cls.model).where(cls.model.username == username)
        result = await session.execute(query)
        instance = result.scalars().first()
        return instance is not None

    @classmethod
    async def get_by_username(cls, session: AsyncSession, username: str) -> User | None:
        query = select(cls.model).where(cls.model.username == username)
        result = await session.execute(query)
        instance = result.scalar_one_or_none()
        return instance


class UserGroupsService(BaseService):
    model = UserGroup


class UserSendingService(BaseService):
    model = UserSending


class UserPropertyService(BaseService):
    model = UserProperty


class UserReportLinkService(BaseService):
    model = UserReportLink


class UserRoleService(BaseService):
    model = UserRole

