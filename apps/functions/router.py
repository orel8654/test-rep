from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repo. database import get_async_session

from repo.base.service import FunctionDictService
from repo.base.schemas import FunctionDictResponse, FunctionDictCreate, FunctionDictUpdate

router = APIRouter(prefix='/functions', tags=['Work with functions'])


@router.get('/{id}', response_model=FunctionDictResponse)
async def get_functions_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a functions dict
    """
    try:
        instance = await FunctionDictService.get(session=session, id=id)
        return FunctionDictResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=FunctionDictResponse)
async def create_functions_dict(payload: FunctionDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a functions dict
    """
    try:
        new_instance = await FunctionDictService.create(session=session, **payload.model_dump())
        return FunctionDictResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/update/{id}', response_model=FunctionDictResponse)
async def update_functions_dict(id: int, payload: FunctionDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update functions dict
    """
    try:
        new_instance = await FunctionDictService.update(session=session, id=id, **payload.model_dump())
        return FunctionDictResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_functions_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a functions dict
    """
    try:
        instane = await FunctionDictService.delete(session=session, id=id)
        return FunctionDictResponse.model_validate(instane)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))