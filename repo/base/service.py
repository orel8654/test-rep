from repo.base_service import BaseService
from repo.models import (Settings, SettingsDict, Report, RoleDict, FunctionDict, RoleFunction, Module,
                         StatusDict, PropertyCodeDict)


class SettingsService(BaseService):
    model = Settings


class SettingsDictService(BaseService):
    model = SettingsDict


class ReportService(BaseService):
    model = Report


class RoleService(BaseService):
    model = RoleDict


class FunctionDictService(BaseService):
    model = FunctionDict


class RoleFunctionsService(BaseService):
    model = RoleFunction


class ModuleService(BaseService):
    model = Module


class StatusDictService(BaseService):
    model = StatusDict


class PropertyCodeDictService(BaseService):
    model = PropertyCodeDict