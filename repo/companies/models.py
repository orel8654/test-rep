from sqlalchemy.orm import relationship, Mapped, mapped_column, declared_attr
from sqlalchemy import ForeignKey, String
from repo.database import Base
from typing import Optional, List
from datetime import date


class Company(Base):
    property_id: Mapped[int] = mapped_column(ForeignKey("property_code_dict.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[date] = mapped_column(nullable=False)
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
    created_date: Mapped[date] = mapped_column(nullable=False)

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