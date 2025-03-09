from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from repo.database import get_async_session

from repo.users.service import UserService
from repo.users.schemas import UserAuth, UserAuthResponse

from apps.auth.service import PasswordService, AuthService


router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/login', response_model=UserAuthResponse)
async def login(payload: UserAuth, session: AsyncSession = Depends(get_async_session)):
    try:
        user_data = payload.model_dump()
        user = await UserService.get_by_username(session=session, username=user_data['username'])
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
                headers={"Authorization": "Bearer"}
            )
        if not PasswordService.verify_password(user_data['password'], user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
                headers={"Authorization": "Bearer"}
            )
        access_token = AuthService.create_access_token(data={"sub": user.username})
        return UserAuthResponse(token=access_token, token_type='bearer')
    except HTTPException as http_error:
        raise http_error
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
