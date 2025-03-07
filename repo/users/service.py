from sqlalchemy.ext.asyncio import AsyncSession

from repo.base_service import BaseService
from repo.models import User
from repo.users.schemas import UserCreate
from apps.auth.service import PasswordService

class UserService(BaseService):
    model = User

    @classmethod
    async def create_user(cls, session: AsyncSession, user: UserCreate) -> int:
        user_data = user.model_dump()
        user_data['password'] = PasswordService.get_password_hash(user_data['password'])

        new_instance = cls.model(**user_data)
        session.add(new_instance)
        await session.commit()

        return new_instance.id

