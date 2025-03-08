from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserRoleService
from repo.users.schemas import UserRoleResponse, UserRoleUpdate, UserRoleCreate

router = APIRouter(prefix='/users/roles', tags=['Work with users roles'])

@router.get('/{id}', response_model=UserRoleResponse)
async def get_user_roles(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get user roles
    """
    try:
        instance = await UserRoleService.get(session=session, id=id)
        return UserRoleResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=UserRoleResponse)
async def create_user_roles(payload: UserRoleCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create user roles
    """
    try:
        new_settings = await UserRoleService.create(session=session, **payload.model_dump())
        return UserRoleResponse.model_validate(new_settings)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.put('/update/{id}', response_model=UserRoleResponse)
async def update_user_roles(id: int, payload: UserRoleUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update user roles
    """
    try:
        new_instance = await UserRoleService.update(session=session, id=id, **payload.model_dump())
        return UserRoleResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_user_roles(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete user roles
    """
    try:
        await UserRoleService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))