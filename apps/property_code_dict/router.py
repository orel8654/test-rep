from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.base.service import PropertyCodeDictService
from repo.base.schemas import PropertyCodeDictCreate, PropertyCodeDictUpdate, PropertyCodeDictResponse

from service.exceptions import handle_db_exceptions


router = APIRouter(prefix="/propertycode/dict", tags=["Property code dict"])


@router.get('/{id}', response_model=PropertyCodeDictResponse)
async def get_property_code_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get property code dict
    """
    try:
        instance = await PropertyCodeDictService.get(session=session, id=id)
        return PropertyCodeDictResponse.model_validate(instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.post('/create', response_model=PropertyCodeDictResponse)
async def create_property_code_dict(payload: PropertyCodeDictCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create property code dict
    """
    try:
        new_instance = await PropertyCodeDictService.create(session=session, **payload.model_dump())
        return PropertyCodeDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.put('/update/{id}', response_model=PropertyCodeDictResponse)
async def update_property_code_dict(id: int, payload: PropertyCodeDictUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update property code dict
    """
    try:
        new_instance = await PropertyCodeDictService.update(session=session, id=id, **payload.model_dump())
        return PropertyCodeDictResponse.model_validate(new_instance)
    except Exception as error:
        handle_db_exceptions(error)

@router.delete('/delete/{id}')
async def delete_property_code_dict(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete property code dict
    """
    try:
        await PropertyCodeDictService.delete(session=session, id=id)
        return Response(status_code=204)
    except Exception as error:
        handle_db_exceptions(error)
