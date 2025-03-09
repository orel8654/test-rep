from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserGroupsService
from repo.users.schemas import UserGroupResponse, UserGroupUpdate, UserGroupCreate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix="/users/group", tags=["Users group"])


@router.get('/{id}', response_model=UserGroupResponse)
async def get_users_group(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get users group
    """
    try:
        instance = await UserGroupsService.get(session=session, id=id)
        return UserGroupResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=UserGroupResponse)
async def create_users_group(payload: UserGroupCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create users group
    """
    try:
        new_instance = await UserGroupsService.create(session=session, **payload.model_dump())
        return UserGroupResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=UserGroupResponse)
async def update_users_group(id: int, payload: UserGroupUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update users group
    """
    try:
        new_instance = await UserGroupsService.update(session=session, id=id, **payload.model_dump())
        return UserGroupResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_users_group(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete users group
    """
    try:
        await UserGroupsService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)