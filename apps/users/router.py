from fastapi import APIRouter, HTTPException

from repo.users.service import UserService
from repo.users.schemas import UserCreate

router = APIRouter(prefix='/users', tags=['Work with users'])

@router.post('/create')
async def create_user(payload: UserCreate):
    try:
        new_user = await UserService.create_user(user=payload)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
