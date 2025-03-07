from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['auth service'])

@router.post('/login')
async def login():
    pass