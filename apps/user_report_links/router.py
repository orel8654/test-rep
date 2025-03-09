from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserReportLinkService
from repo.users.schemas import UserReportLinkResponse, UserReportLinkCreate, UserReportLinkUpdate

router = APIRouter(prefix='/users/report/link', tags=['Users report link'])

@router.get('/{id}', response_model=UserReportLinkResponse)
async def get_user_report_link(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get user report link
    """
    try:
        instance = await UserReportLinkService.get(session=session, id=id)
        return UserReportLinkResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=UserReportLinkResponse)
async def create_user_report_link(payload: UserReportLinkCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create user report link
    """
    try:
        new_settings = await UserReportLinkService.create(session=session, **payload.model_dump())
        return UserReportLinkResponse.model_validate(new_settings)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.put('/update/{id}', response_model=UserReportLinkResponse)
async def update_user_report_link(id: int, payload: UserReportLinkUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update user report link
    """
    try:
        new_instance = await UserReportLinkService.update(session=session, id=id, **payload.model_dump())
        return UserReportLinkResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_user_report_link(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete user report link
    """
    try:
        await UserReportLinkService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))