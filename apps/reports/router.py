from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repo. database import get_async_session

from repo.base.service import ReportService
from repo.base.schemas import ReportResponse, ReportCreate, ReportUpdate

router = APIRouter(prefix='/report', tags=['Work with report'])

@router.get('/{id}', response_model=ReportResponse)
async def get_report(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get report
    """
    try:
        instance = await ReportService.get(session=session, id=id)
        return instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=ReportResponse)
async def create_report(payload: ReportCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create report
    """
    try:
        new_instance = await ReportService.create(session=session, **payload.model_dump())
        return new_instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/update/{id}', response_model=ReportResponse)
async def update_report(id: int, payload: ReportUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update report
    """
    try:
        new_instance = await ReportService.update(session=session, id=id, **payload.model_dump())
        return new_instance
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_report(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete report
    """
    try:
        instane = await ReportService.delete(session=session, id=id)
        return instane
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))