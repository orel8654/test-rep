from fastapi import APIRouter, HTTPException



router = APIRouter(prefix='/companies', tags=['Work with companies'])

@router.post('/create')
async def create_company(payload):
    pass
