from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import SettingsService, SettingsDictService
from repo.base.schemas import (SettingsResponse, SettingsCreate, SettingsUpdate, SettingsDictResponse, SettingsDictCreate,
                               SettingsDictUpdate)

router = APIRouter(prefix='/settings', tags=['Work with settings'])

@router.get('/{id}', response_model=SettingsResponse)
async def get_settings(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get settings
    """
    try:
        instance = await SettingsService.get(session=session, id=id)
        return instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=SettingsResponse)
async def create_settings(payload: SettingsCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a new settings
    """
    try:
        new_settings = await SettingsService.create(session=session, **payload.model_dump())
        return new_settings
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.put('/update/{id}', response_model=SettingsResponse)
async def update_settings(id: int, payload: SettingsUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update settings
    """
    try:
        new_instance = await SettingsService.update(session=session, id=id, **payload.model_dump())
        return new_instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_settings(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete settings
    """
    try:
        instance = await SettingsService.delete(session=session, id=id)
        return instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.get('/dict/{id}', response_model=SettingsDictResponse)
async def get_settings_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a settings dict
    """
    try:
        settings_dict = await SettingsDictService.get(id=id, session=session)
        return settings_dict
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/dict/create', response_model=SettingsDictResponse)
async def create_settings_dict(payload: SettingsDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a new settings dict
    """
    try:
        new_settings_dict = await SettingsDictService.create(session=session, **payload.model_dump())
        return new_settings_dict
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.put('/dict/update/{id}', response_model=SettingsDictResponse)
async def update_settings_dict(id: int, payload: SettingsDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update a settings dict
    """
    try:
        new_settings_dict = await SettingsDictService.update(id=id, session=session, **payload.model_dump())
        return new_settings_dict
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.delete('/dict/delete/{id}')
async def delete_settings_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a settings dict
    """
    try:
        deleted_settings_dict = await SettingsDictService.delete(id=id, session=session)
        return deleted_settings_dict
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
