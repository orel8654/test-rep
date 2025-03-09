from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import RoleFunctionsService
from repo.base.schemas import RoleFunctionResponse, RoleFunctionUpdate, RoleFunctionCreate

from service.exceptions import handle_db_exceptions


router = APIRouter(prefix='/role/function', tags=['Roles dict'])


@router.get('/{id}', response_model=RoleFunctionResponse)
async def get_role_function(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get role function
    """
    try:
        instance = await RoleFunctionsService.get(session=session, id=id)
        return RoleFunctionResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=RoleFunctionResponse)
async def create_role_function(payload: RoleFunctionCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a role function
    """
    try:
        new_instance = await RoleFunctionsService.create(session=session, **payload.model_dump())
        return RoleFunctionResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=RoleFunctionResponse)
async def update_role_function(id: int, payload: RoleFunctionUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update role fiunction
    """
    try:
        new_instance = await RoleFunctionsService.update(session=session, id=id, **payload.model_dump())
        return RoleFunctionResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_role_function(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a role function
    """
    try:
        await RoleFunctionsService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)