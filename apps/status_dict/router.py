from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import StatusDictService
from repo.base.schemas import StatusDictCreate, StatusDictUpdate, StatusDictResponse

router = APIRouter(prefix="/status/dict", tags=["Work with status dict"])


@router.get('/{id}', response_model=StatusDictResponse)
async def get_status_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get status_dict
    """
    try:
        instance = await StatusDictService.get(session=session, id=id)
        return StatusDictResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=StatusDictResponse)
async def create_status_dict(payload: StatusDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create status_dict
    """
    try:
        new_instance = await StatusDictService.create(session=session, **payload.model_dump())
        return StatusDictResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/update/{id}', response_model=StatusDictResponse)
async def update_status_dict(id: int, payload: StatusDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update status_dict
    """
    try:
        new_instance = await StatusDictService.update(session=session, id=id, **payload.model_dump())
        return StatusDictResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_status_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete status_dict
    """
    try:
        await StatusDictService.delete(session=session, id=id)
        return Response( status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))