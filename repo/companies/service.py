from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from repo.base_service import BaseService
from repo.models import Company, License, Department, CompanyProperty, ModuleCompanyLink


class DepartmentService(BaseService):
    model = Department


class CompanyService(BaseService):
    model = Company

    @classmethod
    async def get_company_with_users(cls, session: AsyncSession, id: int):
        query = select(cls.model).options(joinedload(cls.model.users)).where(cls.model.id == id)
        result = await session.execute(query)
        instance = result.scalars().first()
        if instance is None:
            raise ValueError(f"{cls.model.__name__} with id={id} not found")
        return instance


class LicenseService(BaseService):
    model = License


class CompanyPropertiesService(BaseService):
    model = CompanyProperty


class ModuleCompanyLinkService(BaseService):
    model = ModuleCompanyLink
