from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import FunctionDictService
from repo.base.schemas import FunctionDictResponse, FunctionDictCreate, FunctionDictUpdate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/functions', tags=['Functions'])


@router.get('/{id}', response_model=FunctionDictResponse)
async def get_functions_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a functions dict
    """
    try:
        instance = await FunctionDictService.get(session=session, id=id)
        return FunctionDictResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=FunctionDictResponse)
async def create_functions_dict(payload: FunctionDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a functions dict
    """
    try:
        new_instance = await FunctionDictService.create(session=session, **payload.model_dump())
        return FunctionDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=FunctionDictResponse)
async def update_functions_dict(id: int, payload: FunctionDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update functions dict
    """
    try:
        new_instance = await FunctionDictService.update(session=session, id=id, **payload.model_dump())
        return FunctionDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_functions_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a functions dict
    """
    try:
        await FunctionDictService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)