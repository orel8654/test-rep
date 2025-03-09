from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserSendingService
from repo.users.schemas import UserSendingResponse, UserSendingUpdate, UserSendingCreate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/users/sending', tags=['Users sending'])


@router.get('/{id}', response_model=UserSendingResponse)
async def get_user_sending(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get user sending
    """
    try:
        instance = await UserSendingService.get(session=session, id=id)
        return UserSendingResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=UserSendingResponse)
async def create_user_sending(payload: UserSendingCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create user sending
    """
    try:
        new_settings = await UserSendingService.create(session=session, **payload.model_dump())
        return UserSendingResponse.model_validate(new_settings)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=UserSendingResponse)
async def update_user_sending(id: int, payload: UserSendingUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update user sending
    """
    try:
        new_instance = await UserSendingService.update(session=session, id=id, **payload.model_dump())
        return UserSendingResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_user_sending(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete user sending
    """
    try:
        await UserSendingService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)