from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import ModuleService
from repo.base.schemas import ModuleCreate, ModuleUpdate, ModuleResponse

from service.exceptions import handle_db_exceptions


router = APIRouter(prefix="/module", tags=["Module"])


@router.get('/{id}', response_model=ModuleResponse)
async def get_module(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get module
    """
    try:
        instance = await ModuleService.get(session=session, id=id)
        return ModuleResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=ModuleResponse)
async def create_module(payload: ModuleCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create module
    """
    try:
        new_instance = await ModuleService.create(session=session, **payload.model_dump())
        return ModuleResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=ModuleResponse)
async def update_module(id: int, payload: ModuleUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update module
    """
    try:
        new_instance = await ModuleService.update(session=session, id=id, **payload.model_dump())
        return ModuleResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_module(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete module
    """
    try:
        await ModuleService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)