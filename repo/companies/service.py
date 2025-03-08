from repo.base_service import BaseService
from repo.models import Company, License, Department, CompanyProperty


class DepartmentService(BaseService):
    model = Department


class CompanyService(BaseService):
    model = Company


class LicenseService(BaseService):
    model = License


class CompanyPropertiesService(BaseService):
    model = CompanyProperty
