from sqlalchemy.orm import relationship, Mapped, mapped_column, declared_attr
from sqlalchemy import ForeignKey, text, String
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
    created_date: Mapped[date] = mapped_column(nullable=False)
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
    created_date: Mapped[date] = mapped_column(nullable=False)
    message: Mapped[str] = mapped_column(String(4000), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="sendings")
    status: Mapped["StatusDict"] = relationship("StatusDict", back_populates="user_sendings")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_sendings'


class UserReportLink(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    report_id: Mapped[int] = mapped_column(ForeignKey("reports.id"), nullable=False)
    created_date: Mapped[date] = mapped_column(nullable=False)
    active_from: Mapped[date] = mapped_column(nullable=False)
    active_to: Mapped[Optional[date]] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="report_links")
    report: Mapped["Report"] = relationship("Report", back_populates="user_report_links")

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'user_report_links'
