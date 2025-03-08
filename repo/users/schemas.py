from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date


class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    username: str = Field(..., description="Username", max_length=60)
    firstname: str = Field(..., description="First name", max_length=60)
    lastname: str = Field(..., description="Last name", max_length=60)
    patronymic: Optional[str] = Field(None, description="Patronymic", max_length=60)
    company_id: int = Field(..., description="Company ID")
    group_id: int = Field(..., description="Group ID")
    timezone_id: int = Field(..., description="Timezone ID")
    password: str = Field(..., description="User password", min_length=8)
    comment: Optional[str] = Field(None, description="Комментарий", max_length=1000)


class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    username: Optional[str] = Field(..., description="Username", max_length=60)
    firstname: Optional[str] = Field(..., description="First name", max_length=60)
    lastname: Optional[str] = Field(..., description="Last name", max_length=60)
    patronymic: Optional[str] = Field(None, description="Patronymic", max_length=60)
    company_id: int = Field(..., description="Company ID")
    group_id: int = Field(..., description="Group ID")
    timezone_id: int = Field(..., description="Timezone ID")
    comment: Optional[str] = Field(None, description="Комментарий", max_length=1000)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID пользователя")
    company_id: int = Field(..., description="ID компании")
    group_id: int = Field(..., description="ID группы пользователя")
    timezone_id: int = Field(..., description="ID временной зоны")
    username: str = Field(..., description="Имя пользователя", max_length=60)
    firstname: str = Field(..., description="Имя", max_length=60)
    lastname: str = Field(..., description="Фамилия", max_length=60)
    patronymic: Optional[str] = Field(None, description="Отчество", max_length=60)
    created_date: date = Field(..., description="Дата создания")
    user_lock: bool = Field(False, description="Блокировка пользователя")
    comment: Optional[str] = Field(None, description="Комментарий", max_length=1000)


class UserAuth(BaseModel):
    username: str = Field(..., description="Имя пользователя", max_length=60)
    password: str = Field(..., description="User password", min_length=8)


class UserAuthResponse(BaseModel):
    token: str = Field(..., description="Токен авторизации")
    token_type: str = Field(..., description="Тип токена")


class UserGroupCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id: int = Field(..., description="ID компании")
    group_name: str = Field(..., description="Название группы", max_length=255)
    comment: Optional[str] = Field(None, description="Комментарий", max_length=1000)


class UserGroupUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    company_id: int = Field(..., description="ID компании")
    group_name: str = Field(..., description="Название группы", max_length=255)
    comment: Optional[str] = Field(None, description="Комментарий", max_length=1000)


class UserGroupResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID группы")
    company_id: int = Field(..., description="ID компании")
    group_name: str = Field(..., description="Название группы", max_length=255)
    comment: Optional[str] = Field(None, description="Комментарий", max_length=1000)


class UserRoleCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    role_id: int = Field(..., description="ID роли")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class UserRoleUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    role_id: int = Field(..., description="ID роли")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class UserRoleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    user_id: int = Field(..., description="ID пользователя")
    role_id: int = Field(..., description="ID роли")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class UserPropertyCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    property_code_id: int = Field(..., description="ID кода свойства")
    value: Optional[str] = Field(None, description="Значение свойства", max_length=255)


class UserPropertyUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    property_code_id: int = Field(..., description="ID кода свойства")
    value: Optional[str] = Field(None, description="Значение свойства", max_length=255)


class UserPropertyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    user_id: int = Field(..., description="ID пользователя")
    property_code_id: int = Field(..., description="ID кода свойства")
    value: Optional[str] = Field(None, description="Значение свойства", max_length=255)


class UserSendingCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    status_id: int = Field(..., description="ID статуса")
    message: str = Field(..., description="Сообщение", max_length=4000)


class UserSendingUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    status_id: int = Field(..., description="ID статуса")
    message: str = Field(..., description="Сообщение", max_length=4000)


class UserSendingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    user_id: int = Field(..., description="ID пользователя")
    status_id: int = Field(..., description="ID статуса")
    created_date: date = Field(..., description="Дата создания")
    message: str = Field(..., description="Сообщение", max_length=4000)


class UserReportLinkCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    report_id: int = Field(..., description="ID отчета")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class UserReportLinkUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    user_id: int = Field(..., description="ID пользователя")
    report_id: int = Field(..., description="ID отчета")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")


class UserReportLinkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    id: int = Field(..., description="ID записи")
    user_id: int = Field(..., description="ID пользователя")
    report_id: int = Field(..., description="ID отчета")
    created_date: date = Field(..., description="Дата создания")
    active_from: date = Field(..., description="Дата начала действия")
    active_to: Optional[date] = Field(None, description="Дата окончания действия")