from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date


class CompanyCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    property_id: int = Field(..., description="ID свойства компании")
    name: str = Field(..., description="Название компании", max_length=255)
    inn: str = Field(..., description="ИНН компании", min_length=10, max_length=16)
    kpp: str = Field(..., description="КПП компании", min_length=9, max_length=9)
    ogrn: str | None = Field(None, description="ОГРН компании", max_length=13)
    bic: str | None = Field(None, description="БИК компании", max_length=9)


class CompanyUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    property_id: Optional[int] = Field(..., description="ID свойства компании")
    name: Optional[str] = Field(..., description="Название компании", max_length=255)
    inn: Optional[str] = Field(..., description="ИНН компании", min_length=10, max_length=16)
    kpp: Optional[str] = Field(..., description="КПП компании", min_length=9, max_length=9)
    ogrn: Optional[str] | None = Field(None, description="ОГРН компании", max_length=13)
    bic: Optional[str] | None = Field(None, description="БИК компании", max_length=9)


class CompanyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID компании")
    property_id: int = Field(..., description="ID свойства компании")
    name: str = Field(..., description="Название компании", max_length=255)
    created_date: date = Field(..., description="Дата создания")
    inn: str = Field(..., description="ИНН компании", min_length=10, max_length=16)
    kpp: str = Field(..., description="КПП компании", min_length=9, max_length=9)
    ogrn: Optional[str] = Field(None, description="ОГРН компании", max_length=13)
    bic: Optional[str] = Field(None, description="БИК компании", max_length=9)


class LicenseCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id: int = Field(..., description="ID компании")
    license_key: str = Field(..., description="Лицензионный ключ", max_length=1000)
    active_from: date = Field(..., description="Дата начала действия")
    active_to: date = Field(..., description="Дата окончания действия")


class LicenseUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id : int = Field(..., description="ID компании")
    license_key: Optional[str] = Field(None, description="Лицензионный ключ", max_length=1000)
    active_from: Optional[date] = Field(None, description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class LicenseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID лицензии")
    company_id: int = Field(..., description="ID компании")
    license_key: str = Field(..., description="Лицензионный ключ", max_length=1000)
    active_from: date = Field(..., description="Дата начала действия")
    active_to: date = Field(..., description="Дата окончания действия")


class DepartmentCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id: int = Field(..., description="ID компании")
    code: int = Field(..., description="Код подразделения")
    name: str = Field(..., description="Название подразделения", max_length=255)


class DepartmentUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id: int = Field(..., description="ID компании")
    code: Optional[int] = Field(..., description="Код подразделения")
    name: Optional[str] = Field(..., description="Название подразделения", max_length=255)


class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID подразделения")
    company_id: int = Field(..., description="ID компании")
    code: int = Field(..., description="Код подразделения")
    name: str = Field(..., description="Название подразделения", max_length=255)
    created_date: date = Field(..., description="Дата создания")


class ModuleCompanyLinkCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    module_id: int = Field(..., description="ID модуля")
    company_id: int = Field(..., description="ID компании")
    position: int = Field(..., description="Позиция")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class ModuleCompanyLinkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    module_id: int = Field(..., description="ID модуля")
    company_id: int = Field(..., description="ID компании")
    position: int = Field(..., description="Позиция")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")