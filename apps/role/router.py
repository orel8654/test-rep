from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repo. database import get_async_session

from repo.base.service import RoleService, RoleFunctionsService
from repo.base.schemas import (RoleDictResponse, RoleDictCreate, RoleDictUpdate,
                               RoleFunctionResponse, RoleFunctionUpdate, RoleFunctionCreate)


router = APIRouter(prefix='/role', tags=['Work with roles'])


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
        instane = await RoleService.delete(session=session, id=id)
        return RoleDictResponse.model_validate(instane)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.get('/function/{id}', response_model=RoleFunctionResponse)
async def get_role_function(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get role function
    """
    try:
        instance = await RoleFunctionsService.get(session=session, id=id)
        return RoleFunctionResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/function/create', response_model=RoleFunctionResponse)
async def create_role_function(payload: RoleFunctionCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a role function
    """
    try:
        new_instance = await RoleFunctionsService.create(session=session, **payload.model_dump())
        return RoleFunctionResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/function/update/{id}', response_model=RoleFunctionResponse)
async def update_role_function(id: int, payload: RoleFunctionUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update role fiunction
    """
    try:
        new_instance = await RoleFunctionsService.update(session=session, id=id, **payload.model_dump())
        return RoleFunctionResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/function/delete/{id}')
async def delete_role_function(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a role function
    """
    try:
        instane = await RoleFunctionsService.delete(session=session, id=id)
        return RoleFunctionResponse.model_validate(instane)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))