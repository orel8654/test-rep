from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import SettingsDictService
from repo.base.schemas import SettingsDictResponse, SettingsDictCreate, SettingsDictUpdate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/settings/dict', tags=['Settings dict'])


@router.get('/{id}', response_model=SettingsDictResponse)
async def get_settings_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a settings dict
    """
    try:
        settings_dict = await SettingsDictService.get(id=id, session=session)
        return SettingsDictResponse.model_validate(settings_dict)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=SettingsDictResponse)
async def create_settings_dict(payload: SettingsDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a new settings dict
    """
    try:
        new_settings_dict = await SettingsDictService.create(session=session, **payload.model_dump())
        return SettingsDictResponse.model_validate(new_settings_dict)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=SettingsDictResponse)
async def update_settings_dict(id: int, payload: SettingsDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update a settings dict
    """
    try:
        new_settings_dict = await SettingsDictService.update(id=id, session=session, **payload.model_dump())
        return SettingsDictResponse.model_validate(new_settings_dict)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_settings_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a settings dict
    """
    try:
        await SettingsDictService.delete(id=id, session=session)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)