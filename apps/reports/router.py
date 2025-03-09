from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import ReportService
from repo.base.schemas import ReportResponse, ReportCreate, ReportUpdate

from service.exceptions import handle_db_exceptions

router = APIRouter(prefix='/report', tags=['Reports'])

@router.get('/{id}', response_model=ReportResponse)
async def get_report(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get report
    """
    try:
        instance = await ReportService.get(session=session, id=id)
        return ReportResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=ReportResponse)
async def create_report(payload: ReportCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create report
    """
    try:
        new_instance = await ReportService.create(session=session, **payload.model_dump())
        return ReportResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=ReportResponse)
async def update_report(id: int, payload: ReportUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update report
    """
    try:
        new_instance = await ReportService.update(session=session, id=id, **payload.model_dump())
        return ReportResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_report(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete report
    """
    try:
        await ReportService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)