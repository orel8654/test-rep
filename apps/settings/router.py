from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import SettingsService
from repo.base.schemas import SettingsResponse, SettingsCreate, SettingsUpdate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/settings', tags=['Settings'])

@router.get('/{id}', response_model=SettingsResponse)
async def get_settings(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get settings
    """
    try:
        instance = await SettingsService.get(session=session, id=id)
        return SettingsResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=SettingsResponse)
async def create_settings(payload: SettingsCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a new settings
    """
    try:
        new_settings = await SettingsService.create(session=session, **payload.model_dump())
        return SettingsResponse.model_validate(new_settings)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=SettingsResponse)
async def update_settings(id: int, payload: SettingsUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update settings
    """
    try:
        new_instance = await SettingsService.update(session=session, id=id, **payload.model_dump())
        return SettingsResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_settings(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete settings
    """
    try:
        await SettingsService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)