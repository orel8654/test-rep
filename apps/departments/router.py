from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repo. database import get_async_session

from repo.companies.service import DepartmentService
from repo.companies.schemas import DepartmentResponse, DepartmentCreate, DepartmentUpdate


router = APIRouter(prefix="/departments", tags=["Work with departments"])


@router.get('/{id}', response_model=DepartmentResponse)
async def get_department(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get department
    """
    try:
        instance = await DepartmentService.get(session=session, id=id)
        return instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=DepartmentResponse)
async def create_department(payload: DepartmentCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create department
    """
    try:
        new_instance = await DepartmentService.create(session=session, **payload.model_dump())
        return new_instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/update/{id}', response_model=DepartmentResponse)
async def update_department(id: int, payload: DepartmentUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update department
    """
    try:
        new_instance = await DepartmentService.update(session=session, id=id, **payload.model_dump())
        return new_instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_department(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete department
    """
    try:
        instane = await DepartmentService.delete(session=session, id=id)
        return instane
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))