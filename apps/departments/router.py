from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.companies.service import DepartmentService
from repo.companies.schemas import DepartmentResponse, DepartmentCreate, DepartmentUpdate

from service.exceptions import handle_db_exceptions


router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get('/{id}', response_model=DepartmentResponse)
async def get_department(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get department
    """
    try:
        instance = await DepartmentService.get(session=session, id=id)
        return DepartmentResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=DepartmentResponse)
async def create_department(payload: DepartmentCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create department
    """
    try:
        new_instance = await DepartmentService.create(session=session, **payload.model_dump())
        return DepartmentResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=DepartmentResponse)
async def update_department(id: int, payload: DepartmentUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update department
    """
    try:
        new_instance = await DepartmentService.update(session=session, id=id, **payload.model_dump())
        return DepartmentResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_department(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete department
    """
    try:
        await DepartmentService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)