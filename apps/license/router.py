from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.companies.service import LicenseService
from repo.companies.schemas import LicenseCreate, LicenseResponse, LicenseUpdate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/license', tags=['License'])


@router.get('/{id}', response_model=LicenseResponse)
async def get_license(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a license
    """
    try:
        instance = await LicenseService.get(session=session, id=id)
        return LicenseResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=LicenseResponse)
async def create_license(payload: LicenseCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a license
    """
    try:
        new_instance = await LicenseService.create(session=session, **payload.model_dump())
        return LicenseResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=LicenseResponse)
async def update_license(id: int, payload: LicenseUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update license
    """
    try:
        new_instance = await LicenseService.update(session=session, id=id, **payload.model_dump())
        return LicenseResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_license(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a license
    """
    try:
        await LicenseService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)


