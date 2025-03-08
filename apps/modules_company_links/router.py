from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.companies.service import ModuleCompanyLinkService
from repo.companies.schemas import ModuleCompanyLinkResponse, ModuleCompanyLinkCreate, ModuleCompanyLinkUpdate

router = APIRouter(prefix='/modules/company/links', tags=['Work with modules comapny links'])


@router.get('/{id}', response_model=ModuleCompanyLinkResponse)
async def get_modules_company_links(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Get a modules comapny link
    """
    try:
        instance = await ModuleCompanyLinkService.get(session=session, id=id)
        return ModuleCompanyLinkResponse.model_validate(instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post('/create', response_model=ModuleCompanyLinkResponse)
async def create_modules_company_links(payload: ModuleCompanyLinkCreate, session: AsyncSession = Depends(get_async_session)):
    """
        Create a modules comapny link
    """
    try:
        new_instance = await ModuleCompanyLinkService.create(session=session, **payload.model_dump())
        return ModuleCompanyLinkResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put('/update/{id}', response_model=ModuleCompanyLinkResponse)
async def update_modules_company_links(id: int, payload: ModuleCompanyLinkUpdate, session: AsyncSession = Depends(get_async_session)):
    """
        Update modules comapny link
    """
    try:
        new_instance = await ModuleCompanyLinkService.update(session=session, id=id, **payload.model_dump())
        return ModuleCompanyLinkResponse.model_validate(new_instance)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.delete('/delete/{id}')
async def delete_modules_company_links(id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Delete a modules comapny link
    """
    try:
        await ModuleCompanyLinkService.delete(session=session, id=id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))