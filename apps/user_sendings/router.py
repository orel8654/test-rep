from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserSendingService
from repo.users.schemas import UserSendingResponse, UserSendingUpdate, UserSendingCreate

router = APIRouter(prefix='/users/sending', tags=['Work with user sending'])


@router.get('/{id}', response_model=UserSendingResponse)
async def get_user_sending(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get user sending
    """
    try:
        instance = await UserSendingService.get(session=session, id=id)
        return UserSendingResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=UserSendingResponse)
async def create_user_sending(payload: UserSendingCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create user sending
    """
    try:
        new_settings = await UserSendingService.create(session=session, **payload.model_dump())
        return UserSendingResponse.model_validate(new_settings)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.put('/update/{id}', response_model=UserSendingResponse)
async def update_user_sending(id: int, payload: UserSendingUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update user sending
    """
    try:
        new_instance = await UserSendingService.update(session=session, id=id, **payload.model_dump())
        return UserSendingResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_user_sending(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete user sending
    """
    try:
        await UserSendingService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))