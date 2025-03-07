from fastapi import APIRouter, HTTPException

from repo.companies.schemas import LicenseCreate, LicenseResponse
from repo.companies.service import LicenseService

router = APIRouter(prefix='/license', tags=['Work with licenses'])

@router.post("/create", response_model=LicenseResponse)
async def create_license(payload: LicenseCreate):
    """
        Создание новой лицензии
    """
    try:
        new_license = LicenseService.create_license(data=payload)
        return new_license
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


