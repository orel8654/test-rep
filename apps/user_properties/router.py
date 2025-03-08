from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserPropertyService
from repo.users.schemas import UserPropertyResponse, UserPropertyUpdate, UserPropertyCreate

router = APIRouter(prefix='/users/property', tags=['Work with users property'])


@router.get('/{id}', response_model=UserPropertyResponse)
async def get_user_property(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get user property
    """
    try:
        instance = await UserPropertyService.get(session=session, id=id)
        return UserPropertyResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=UserPropertyResponse)
async def create_user_property(payload: UserPropertyCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create user property
    """
    try:
        new_settings = await UserPropertyService.create(session=session, **payload.model_dump())
        return UserPropertyResponse.model_validate(new_settings)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.put('/update/{id}', response_model=UserPropertyResponse)
async def update_user_property(id: int, payload: UserPropertyUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update user property
    """
    try:
        new_instance = await UserPropertyService.update(session=session, id=id, **payload.model_dump())
        return UserPropertyResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_user_property(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete user property
    """
    try:
        await UserPropertyService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))