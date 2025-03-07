from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date


class PropertyCodeDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    group_code: str = Field(..., description="Групповой код", max_length=30)
    code: str = Field(..., description="Код", max_length=30)
    name: Optional[str] = Field(None, description="Название", max_length=100)


class PropertyCodeDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    group_code: str = Field(..., description="Групповой код", max_length=30)
    code: str = Field(..., description="Код", max_length=30)
    name: Optional[str] = Field(None, description="Название", max_length=100)


class RoleDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код роли", max_length=30)
    name: str = Field(..., description="Название роли", max_length=60)


class RoleDictUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: Optional[str] = Field(..., description="Код роли", max_length=30)
    name: Optional[str] = Field(..., description="Название роли", max_length=60)


class RoleDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    code: str = Field(..., description="Код роли", max_length=30)
    name: str = Field(..., description="Название роли", max_length=60)


class TimezoneDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    timezone_name: Optional[str] = Field(None, description="Название временной зоны", max_length=255)
    timezone: Optional[str] = Field(None, description="Временная зона")


class TimezoneDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID временной зоны")
    timezone_name: Optional[str] = Field(None, description="Название временной зоны", max_length=255)
    timezone: Optional[str] = Field(None, description="Временная зона")


class StatusDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код статуса", max_length=16)
    name: str = Field(..., description="Название статуса", max_length=60)


class StatusDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID статуса")
    code: str = Field(..., description="Код статуса", max_length=16)
    name: str = Field(..., description="Название статуса", max_length=60)


class ShablonDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код шаблона", max_length=30)
    name: str = Field(..., description="Название шаблона", max_length=255)
    value: Optional[str] = Field(None, description="Значение шаблона")


class ShablonDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID шаблона")
    code: str = Field(..., description="Код шаблона", max_length=30)
    name: str = Field(..., description="Название шаблона", max_length=255)
    value: Optional[str] = Field(None, description="Значение шаблона")


class ModuleCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код модуля", max_length=30)
    name: str = Field(..., description="Название модуля", max_length=60)


class ModuleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID модуля")
    code: str = Field(..., description="Код модуля", max_length=30)
    name: str = Field(..., description="Название модуля", max_length=60)


class ReportCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код отчета", max_length=30)
    name: str = Field(..., description="Название отчета")
    version: int = Field(..., description="Версия отчета")


class ReportUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: Optional[str] = Field(..., description="Код отчета", max_length=30)
    name: Optional[str] = Field(..., description="Название отчета")
    version: Optional[int] = Field(..., description="Версия отчета")


class ReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID отчета")
    code: str = Field(..., description="Код отчета", max_length=30)
    name: str = Field(..., description="Название отчета")
    version: int = Field(..., description="Версия отчета")


class SettingsCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    setting_code_id: int = Field(..., description="ID кода настройки")
    value: str = Field(..., description="Значение настройки", max_length=255)
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class SettingsUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    setting_code_id: Optional[int] = Field(None, description="ID кода настройки")
    value: Optional[str] = Field(None, description="Значение настройки", max_length=255)
    active_from: Optional[date] = Field(None, description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class SettingsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID настройки")
    setting_code_id: int = Field(..., description="ID кода настройки")
    value: str = Field(..., description="Значение настройки", max_length=255)
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class SettingsDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код настройки", max_length=30)
    name: str = Field(..., description="Название настройки", max_length=255)


class SettingsDictUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: Optional[str] = Field(None, description="Код настройки", max_length=30)
    name: Optional[str] = Field(None, description="Название настройки", max_length=255)


class SettingsDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    code: str = Field(..., description="Код настройки", max_length=30)
    name: str = Field(..., description="Название настройки", max_length=255)


class CompanyPropertyCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id: int = Field(..., description="ID компании")
    property_code_id: int = Field(..., description="ID кода свойства")
    value: Optional[str] = Field(None, description="Значение свойства", max_length=255)


class CompanyPropertyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    company_id: int = Field(..., description="ID компании")
    property_code_id: int = Field(..., description="ID кода свойства")
    value: Optional[str] = Field(None, description="Значение свойства", max_length=255)


class FunctionDictCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    code: str = Field(..., description="Код функции", max_length=30)
    version: int = Field(..., description="Версия функции")


class FunctionDictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID функции")
    code: str = Field(..., description="Код функции", max_length=30)
    version: int = Field(..., description="Версия функции")


class RoleFunctionCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    role_id: int = Field(..., description="ID роли")
    function_code_id: int = Field(..., description="ID кода функции")


class RoleFunctionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    role_id: int = Field(..., description="ID роли")
    function_code_id: int = Field(..., description="ID кода функции")