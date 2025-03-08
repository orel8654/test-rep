from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import RoleFunctionsService
from repo.base.schemas import RoleFunctionResponse, RoleFunctionUpdate, RoleFunctionCreate


router = APIRouter(prefix='/role/function', tags=['Work with roles'])


@router.get('/{id}', response_model=RoleFunctionResponse)
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

@router.post('/create', response_model=RoleFunctionResponse)
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

@router.put('/update/{id}', response_model=RoleFunctionResponse)
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

@router.delete('/delete/{id}')
async def delete_role_function(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a role function
    """
    try:
        await RoleFunctionsService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))