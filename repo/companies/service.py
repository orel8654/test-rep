from sqlalchemy.ext.asyncio import AsyncSession

from repo.base_service import BaseService
from repo.models import Company, License
from repo.companies.schemas import CompanyCreate, LicenseCreate, LicenseUpdate, LicenseResponse


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