from sqlalchemy.ext.asyncio import AsyncSession

from repo.base_service import BaseService
from repo.models import Company, License, Department
from repo.companies.schemas import CompanyCreate, LicenseCreate, LicenseUpdate, LicenseResponse, DepartmentResponse


class DepartmentService(BaseService):
    model = Department

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> DepartmentResponse:
        instance = await super().get(session=session, id=id)
        return DepartmentResponse.model_validate(instance)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> DepartmentResponse:
        new_instance = await super().create(session=session, **values)
        return DepartmentResponse.model_validate(new_instance)

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **values) -> DepartmentResponse:
        new_instance = await super().update(session=session, id=id, **values)
        return DepartmentResponse.model_validate(new_instance)

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> str:
        instance = await super().delete(session=session, id=id)
        return instance


class CompanyService(BaseService):
    model = Company

    @classmethod
    async def create_company(cls, session: AsyncSession, company: CompanyCreate):
        pass


class LicenseService(BaseService):
    model = License

    @classmethod
    async def create_license(cls, session: AsyncSession, data: LicenseCreate) -> LicenseResponse:
        license_data = data.model_dump()
        new_instance = cls.model(**license_data)
        session.add(new_instance)

        await session.commit()
        await session.refresh(new_instance)
        return LicenseResponse.model_validate(new_instance)

    @classmethod
    async def update_license(cls, session: AsyncSession, data: LicenseUpdate) -> LicenseResponse:
        pass

    @classmethod
    async def delete_license(cls, session: AsyncSession, license_id: int):
        pass