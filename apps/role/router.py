from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import RoleService
from repo.base.schemas import RoleDictResponse, RoleDictCreate, RoleDictUpdate

from service.exceptions import handle_db_exceptions


router = APIRouter(prefix='/role', tags=['Roles'])


@router.get('/{id}', response_model=RoleDictResponse)
async def get_role_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a role dict
    """
    try:
        instance = await RoleService.get(session=session, id=id)
        return RoleDictResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=RoleDictResponse)
async def create_role_dict(payload: RoleDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a role dict
    """
    try:
        new_instance = await RoleService.create(session=session, **payload.model_dump())
        return RoleDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=RoleDictResponse)
async def update_role_dict(id: int, payload: RoleDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update role dict
    """
    try:
        new_instance = await RoleService.update(session=session, id=id, **payload.model_dump())
        return RoleDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_role_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a role dict
    """
    try:
        await RoleService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)