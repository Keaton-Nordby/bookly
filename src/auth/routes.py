from fastapi import APIRouter, Depends, status
from .schemas import UserCreatedModel, UserModel
from .service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException


auth_router = APIRouter()
user_service = UserService()


@auth_router.POST(
    "/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED
)
async def create_user_Account(
    user_data: UserCreatedModel, session: AsyncSession = Depends(get_session)
):
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists",
        )

    new_user = await user_service.create_user(user_data, session)

    return new_user
