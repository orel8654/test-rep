from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.companies.service import CompanyService
from repo.companies.schemas import CompanyResponse, CompanyCreate, CompanyUpdate, CompanyFullyResponse

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/companies', tags=['Company'])

@router.get('/{id}', response_model=CompanyResponse)
async def get_company(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a company
    """
    try:
        instance = await CompanyService.get(session=session, id=id)
        return CompanyResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.get('/{id}/fully', response_model=CompanyFullyResponse)
async def get_company_fully(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a company with users
    """
    try:
        instance = await CompanyService.get_company_with_users(session=session, id=id)
        return CompanyFullyResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=CompanyResponse)
async def create_company(payload: CompanyCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a company
    """
    try:
        new_instance = await CompanyService.create(session=session, **payload.model_dump())
        return CompanyResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=CompanyResponse)
async def update_comapny(id: int, payload: CompanyUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update comapny
    """
    try:
        new_instance = await CompanyService.update(session=session, id=id, **payload.model_dump())
        return CompanyResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_comapny(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a comapny
    """
    try:
        await CompanyService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)