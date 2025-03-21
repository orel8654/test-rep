from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import TimezoneDictService
from repo.base.schemas import TimezoneDictCreate, TimezoneDictUpdate, TimezoneDictResponse

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/timezone/dict', tags=['Timezone dict'])

@router.get('/{id}', response_model=TimezoneDictResponse)
async def get_timezone_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a timezone dict
    """
    try:
        instance = await TimezoneDictService.get(session=session, id=id)
        return TimezoneDictResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=TimezoneDictResponse)
async def create_timezone_dict(payload: TimezoneDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a timezone dict
    """
    try:
        new_instance = await TimezoneDictService.create(session=session, **payload.model_dump())
        return TimezoneDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=TimezoneDictResponse)
async def update_timezone_dict(id: int, payload: TimezoneDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update timezone dict
    """
    try:
        new_instance = await TimezoneDictService.update(session=session, id=id, **payload.model_dump())
        return TimezoneDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_timezone_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a timezone dict
    """
    try:
        await TimezoneDictService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)

