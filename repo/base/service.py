from sqlalchemy.ext.asyncio import AsyncSession

from repo.base_service import BaseService
from repo.models import Settings, SettingsDict, Report, RoleDict, FunctionDict, RoleFunction
from repo.base.schemas import (
    SettingsResponse, SettingsDictResponse, ReportResponse, RoleDictResponse, FunctionDictResponse, RoleFunctionResponse
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

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> SettingsResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return SettingsResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> SettingsResponse:
        instance = await super().delete(session=session, id=id)
        return instance


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


class ReportService(BaseService):
    model = Report

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> ReportResponse:
        instance = await super().get(session=session, id=id)
        return ReportResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> ReportResponse:
        new_instance = await super().create(session=session, **values)
        return ReportResponse.model_validate(new_instance)

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> ReportResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return ReportResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> str:
        instance = await super().delete(session=session, id=id)
        return instance


class RoleService(BaseService):
    model = RoleDict

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> RoleDictResponse:
        instance = await super().get(session=session, id=id)
        return RoleDictResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> RoleDictResponse:
        new_instance = await super().create(session=session, **values)
        return RoleDictResponse.model_validate(new_instance)

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> RoleDictResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return RoleDictResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> str:
        instance = await super().delete(session=session, id=id)
        return instance


class FunctionDictService(BaseService):
    model = FunctionDict

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> FunctionDictResponse:
        instance = await super().get(session=session, id=id)
        return FunctionDictResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> FunctionDictResponse:
        new_instance = await super().create(session=session, **values)
        return FunctionDictResponse.model_validate(new_instance)

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> FunctionDictResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return FunctionDictResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> str:
        instance = await super().delete(session=session, id=id)
        return instance


class RoleFunctionsService(BaseService):
    model = RoleFunction

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> RoleFunctionResponse:
        instance = await super().get(session=session, id=id)
        return RoleFunctionResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> RoleFunctionResponse:
        new_instance = await super().create(session=session, **values)
        return RoleFunctionResponse.model_validate(new_instance)

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> RoleFunctionResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return RoleFunctionResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> str:
        instance = await super().delete(session=session, id=id)
        return instance
