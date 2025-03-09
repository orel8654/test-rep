from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserService
from repo.users.schemas import UserCreate, UserUpdate, UserResponse

from apps.auth.service import PasswordService
from apps.auth.middleware import get_user_access

from service.exceptions import handle_db_exceptions

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/{id}', response_model=UserResponse)
async def get_user(id: int, session: AsyncSession = Depends(get_async_session), current_user: str = Depends(get_user_access)):
    """
        Get user
    """
    try:
        logger.info(f'user request: {current_user}')
        instance = await UserService.get(session=session, id=id)
        return UserResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.get('/get/all', response_model=list[UserResponse])
async def get_all_users(session: AsyncSession = Depends(get_async_session), current_user: str = Depends(get_user_access)):
    """
        Get all users
    """
    try:
        logger.info(f'user request: {current_user}')
        users = await UserService.get_all(session=session)
        return users
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=UserResponse)
async def create_user(payload: UserCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create user
    """
    try:
        user_data = payload.model_dump()
        if await UserService.if_username_exists(session=session, username=user_data['username']):
            raise HTTPException(status_code=409, detail="Username already exists")
        user_data['password'] = PasswordService.get_password_hash(user_data['password'])
        new_settings = await UserService.create(session=session, **user_data)
        return UserResponse.model_validate(new_settings)
    except Exception as error:
        handle_db_exceptions(error)


@router.put('/update/{id}', response_model=UserResponse)
async def update_user(id: int, payload: UserUpdate, session: AsyncSession = Depends(get_async_session), current_user: str = Depends(get_user_access)):
    """
        Update user
    """
    try:
        logger.info(f'user request: {current_user}')
        new_instance = await UserService.update(session=session, id=id, **payload.model_dump())
        return UserResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_user(id: int, session: AsyncSession = Depends(get_async_session), current_user: str = Depends(get_user_access)):
    """
        Delete user
    """
    try:
        logger.info(f'user request: {current_user}')
        await UserService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)