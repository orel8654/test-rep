from sqlalchemy.orm import relationship, Mapped, mapped_column, declared_attr
from sqlalchemy import ForeignKey, text, String, func
from typing import Optional, List
from repo.database import Base
from datetime import date


class User(Base):
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("user_groups.id"), nullable=False)
    timezone_id: Mapped[int] = mapped_column(ForeignKey("timezone_dict.id"), nullable=False)
    username: Mapped[str] = mapped_column(String(60), unique=True, index=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(60), nullable=False)
    lastname: Mapped[str] = mapped_column(String(60), nullable=False)
    patronymic: Mapped[Optional[str]] = mapped_column(String(60), nullable=True)
    created_date: Mapped[date] = mapped_column(nullable=False, default=date.today)
    user_lock: Mapped[bool] = mapped_column(default=False, server_default=text("false"))
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)

    company: Mapped["Company"] = relationship("Company", back_populates="users")
    group: Mapped["UserGroup"] = relationship("UserGroup", back_populates="users")
    timezone: Mapped["TimezoneDict"] = relationship("TimezoneDict", back_populates="users")
    properties: Mapped[List["UserProperty"]] = relationship("UserProperty", back_populates="user")
    roles: Mapped[List["UserRole"]] = relationship("UserRole", back_populates="user")
    sendings: Mapped[List["UserSending"]] = relationship("UserSending", back_populates="user")
    report_links: Mapped[List["UserReportLink"]] = relationship("UserReportLink", back_populates="user")


class UserGroup(Base):
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    group_name: Mapped[str] = mapped_column(String(255), nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)

    users: Mapped[List["User"]] = relationship("User", back_populates="group")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_groups'


class UserRole(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles_dict.id"), nullable=False)
    active_from: Mapped[date] = mapped_column(nullable=False)
    active_to: Mapped[Optional[date]] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="roles")
    role: Mapped["RoleDict"] = relationship("RoleDict", back_populates="user_roles")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_roles'


class UserProperty(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    property_code_id: Mapped[int] = mapped_column(ForeignKey("property_code_dict.id"), nullable=False)
    value: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="properties")
    property_code: Mapped["PropertyCodeDict"] = relationship("PropertyCodeDict", back_populates="user_properties")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_properties'


class UserSending(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("status_dict.id"), nullable=False)
    created_date: Mapped[date] = mapped_column(nullable=False, default=date.today)
    message: Mapped[str] = mapped_column(String(4000), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="sendings")
    status: Mapped["StatusDict"] = relationship("StatusDict", back_populates="user_sendings")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_sendings'


class UserReportLink(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    report_id: Mapped[int] = mapped_column(ForeignKey("reports.id"), nullable=False)
    created_date: Mapped[date] = mapped_column(nullable=False, default=date.today)
    active_from: Mapped[date] = mapped_column(nullable=False)
    active_to: Mapped[Optional[date]] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="report_links")
    report: Mapped["Report"] = relationship("Report", back_populates="user_report_links")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_report_links'


class Company(Base):
    property_id: Mapped[int] = mapped_column(ForeignKey("property_code_dict.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[date] = mapped_column(nullable=False, default=date.today)
    inn: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    kpp: Mapped[str] = mapped_column(String(9), unique=True, nullable=False)
    ogrn: Mapped[Optional[str]] = mapped_column(String(13), nullable=True)
    bic: Mapped[Optional[str]] = mapped_column(String(9), nullable=True)

    users: Mapped[List["User"]] = relationship("User", back_populates="company")
    properties: Mapped[List["CompanyProperty"]] = relationship("CompanyProperty", back_populates="company")
    license: Mapped[List["License"]] = relationship("License", back_populates="company")
    modules: Mapped[List["ModuleCompanyLink"]] = relationship("ModuleCompanyLink", back_populates="company")
    departments: Mapped[List["Department"]] = relationship("Department", back_populates="company")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'companies'


class CompanyProperty(Base):
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    property_code_id: Mapped[int] = mapped_column(ForeignKey("property_code_dict.id"), nullable=False)
    value: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    company: Mapped["Company"] = relationship("Company", back_populates="properties")
    property_code: Mapped["PropertyCodeDict"] = relationship("PropertyCodeDict", back_populates="company_properties")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'company_properties'


class License(Base):
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    license_key: Mapped[str] = mapped_column(String(1000), nullable=False)
    active_from: Mapped[date] = mapped_column(nullable=False)
    active_to: Mapped[date] = mapped_column(nullable=False)

    company: Mapped["Company"] = relationship("Company", back_populates="license")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'license'


class Department(Base):
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    code: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[date] = mapped_column(nullable=False, default=date.today)

    company: Mapped["Company"] = relationship("Company", back_populates="departments")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'departments'


class ModuleCompanyLink(Base):
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"), nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    position: Mapped[int] = mapped_column(nullable=False)
    active_from: Mapped[date] = mapped_column(nullable=False)
    active_to: Mapped[Optional[date]] = mapped_column(nullable=True)

    module: Mapped["Module"] = relationship("Module", back_populates="company_links")
    company: Mapped["Company"] = relationship("Company", back_populates="modules")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'module_company_links'


class PropertyCodeDict(Base):
    group_code: Mapped[str] = mapped_column(String(30), nullable=False)
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    user_properties: Mapped[List["UserProperty"]] = relationship("UserProperty", back_populates="property_code")
    company_properties: Mapped[List["CompanyProperty"]] = relationship("CompanyProperty", back_populates="property_code")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'property_code_dict'


class RoleDict(Base):
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[str] = mapped_column(String(60), nullable=False)

    user_roles: Mapped[List["UserRole"]] = relationship("UserRole", back_populates="role")
    functions: Mapped[List["RoleFunction"]] = relationship("RoleFunction", back_populates="role")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'roles_dict'


class RoleFunction(Base):
    role_id: Mapped[int] = mapped_column(ForeignKey("roles_dict.id"), nullable=False)
    function_code_id: Mapped[int] = mapped_column(ForeignKey("functions_dict.id"), nullable=False)

    role: Mapped["RoleDict"] = relationship("RoleDict", back_populates="functions")
    function: Mapped["FunctionDict"] = relationship("FunctionDict", back_populates="role_functions")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'role_functions'


class FunctionDict(Base):
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    version: Mapped[int] = mapped_column(nullable=False)

    role_functions: Mapped[List["RoleFunction"]] = relationship("RoleFunction", back_populates="function")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'functions_dict'


class Settings(Base):
    setting_code_id: Mapped[int] = mapped_column(ForeignKey("settings_dict.id"), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    active_from: Mapped[date] = mapped_column(nullable=False)
    active_to: Mapped[Optional[date]] = mapped_column(nullable=True)

    setting_code: Mapped["SettingsDict"] = relationship("SettingsDict", back_populates="settings")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'settings'


class SettingsDict(Base):
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    settings: Mapped[List["Settings"]] = relationship("Settings", back_populates="setting_code")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'settings_dict'


class TimezoneDict(Base):
    timezone_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    timezone: Mapped[Optional[str]] = mapped_column(nullable=True)

    users: Mapped[List["User"]] = relationship("User", back_populates="timezone")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'timezone_dict'


class StatusDict(Base):
    code: Mapped[str] = mapped_column(String(16), nullable=False)
    name: Mapped[str] = mapped_column(String(60), nullable=False)

    user_sendings: Mapped[List["UserSending"]] = relationship("UserSending", back_populates="status")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'status_dict'


class Module(Base):
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[str] = mapped_column(String(60), nullable=False)

    company_links: Mapped[List["ModuleCompanyLink"]] = relationship("ModuleCompanyLink", back_populates="module")


class Report(Base):
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[int] = mapped_column(nullable=False)

    user_report_links: Mapped[List["UserReportLink"]] = relationship("UserReportLink", back_populates="report")


class ShablonDict(Base):
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[Optional[str]] = mapped_column(nullable=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'shablon_dict'