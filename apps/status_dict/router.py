from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import StatusDictService
from repo.base.schemas import StatusDictCreate, StatusDictUpdate, StatusDictResponse

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix="/status/dict", tags=["Status dict"])


@router.get('/{id}', response_model=StatusDictResponse)
async def get_status_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get status_dict
    """
    try:
        instance = await StatusDictService.get(session=session, id=id)
        return StatusDictResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=StatusDictResponse)
async def create_status_dict(payload: StatusDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create status_dict
    """
    try:
        new_instance = await StatusDictService.create(session=session, **payload.model_dump())
        return StatusDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=StatusDictResponse)
async def update_status_dict(id: int, payload: StatusDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update status_dict
    """
    try:
        new_instance = await StatusDictService.update(session=session, id=id, **payload.model_dump())
        return StatusDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_status_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete status_dict
    """
    try:
        await StatusDictService.delete(session=session, id=id)
        return Response( status_code=204)
    except Exception as error:
        handle_db_exceptions(error)