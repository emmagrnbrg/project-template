from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...db.Database import get_session
from ...rest.models.common.IdRs import IdRs
from ...rest.models.user.RegistrationModel import UserRegistrationModel
from ...services.user.UserService import UserService

router = APIRouter()


@router.post("/register")
async def register(
        request: Annotated[UserRegistrationModel, Body()],
        session: AsyncSession = Depends(get_session)
) -> IdRs:
    user = await UserService(session).create_user(request)

    return IdRs(id=user.id)
