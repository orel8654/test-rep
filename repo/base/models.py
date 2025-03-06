from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from typing import Optional, List
from repo.database import Base
from datetime import date


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