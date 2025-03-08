from repo.base_service import BaseService
from repo.models import Company, License, Department, CompanyProperty, ModuleCompanyLink


class DepartmentService(BaseService):
    model = Department


class CompanyService(BaseService):
    model = Company


class LicenseService(BaseService):
    model = License


class CompanyPropertiesService(BaseService):
    model = CompanyProperty


class ModuleCompanyLinkService(BaseService):
    model = ModuleCompanyLink
