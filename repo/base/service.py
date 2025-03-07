from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from repo.base_service import BaseService
from repo.models import Settings, SettingsDict
from repo.base.schemas import (
    SettingsCreate, SettingsResponse, SettingsDictCreate, SettingsDictResponse, SettingsDictUpdate
)


class SettingsService(BaseService):
    model = Settings

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> SettingsResponse:
        instance = await super().get(session=session, id=id)
        return SettingsResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> SettingsResponse:
        new_instance = await super().create(session=session, **values)
        return SettingsResponse.model_validate(new_instance)

class SettingsDictService(BaseService):
    model = SettingsDict

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> SettingsDictResponse:
        instance = await super().get(session=session, id=id)
        return SettingsDictResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> SettingsDictResponse:
        new_instance = await super().create(session=session, **values)
        return SettingsDictResponse.model_validate(new_instance)

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> SettingsDictResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return SettingsDictResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> str:
        instance = await super().delete(session=session, id=id)
        return instance