from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserService
from repo.users.schemas import UserCreate, UserUpdate, UserResponse

from apps.auth.service import PasswordService
from apps.auth.middleware import get_user_access

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/protect/{id}', response_model=UserResponse)
async def get_user(id: int, session: AsyncSession = Depends(get_async_session), current_user: str = Depends(get_user_access)):
    """
        Get user
    """
    try:
        logger.info(f'user request: {current_user}')
        instance = await UserService.get(session=session, id=id)
        return UserResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

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
    except HTTPException as http_error:
        raise http_error
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.put('/update/{id}', response_model=UserResponse)
async def update_user(id: int, payload: UserUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update user
    """
    try:
        new_instance = await UserService.update(session=session, id=id, **payload.model_dump())
        return UserResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_user(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete user
    """
    try:
        await UserService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))