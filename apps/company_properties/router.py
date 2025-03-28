from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.companies.service import CompanyPropertiesService
from repo.base.schemas import CompanyPropertyCreate, CompanyPropertyUpdate, CompanyPropertyResponse

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/comapny/property', tags=['Company property'])


@router.get('/{id}', response_model=CompanyPropertyResponse)
async def get_company_property(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a comapny property
    """
    try:
        instance = await CompanyPropertiesService.get(session=session, id=id)
        return CompanyPropertyResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=CompanyPropertyResponse)
async def create_company_property(payload: CompanyPropertyCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a company property
    """
    try:
        new_instance = await CompanyPropertiesService.create(session=session, **payload.model_dump())
        return CompanyPropertyResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=CompanyPropertyResponse)
async def update_company_property(id: int, payload: CompanyPropertyUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update comapny property
    """
    try:
        new_instance = await CompanyPropertiesService.update(session=session, id=id, **payload.model_dump())
        return CompanyPropertyResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_company_property(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a comapny property
    """
    try:
        await CompanyPropertiesService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)
