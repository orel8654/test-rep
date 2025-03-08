from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import RoleService
from repo.base.schemas import RoleDictResponse, RoleDictCreate, RoleDictUpdate


router = APIRouter(prefix='/role', tags=['Work with role functions'])


@router.get('/{id}', response_model=RoleDictResponse)
async def get_role_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a role dict
    """
    try:
        instance = await RoleService.get(session=session, id=id)
        return RoleDictResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=RoleDictResponse)
async def create_role_dict(payload: RoleDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a role dict
    """
    try:
        new_instance = await RoleService.create(session=session, **payload.model_dump())
        return RoleDictResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/update/{id}', response_model=RoleDictResponse)
async def update_role_dict(id: int, payload: RoleDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update role dict
    """
    try:
        new_instance = await RoleService.update(session=session, id=id, **payload.model_dump())
        return RoleDictResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_role_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a role dict
    """
    try:
        await RoleService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))