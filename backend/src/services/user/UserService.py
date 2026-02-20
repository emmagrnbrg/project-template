from sqlalchemy.ext.asyncio import AsyncSession

from .RoleService import RoleService
from ..BaseService import BaseService
from ...db.entities import UserEntity
from ...repositories.user.UserRepository import UserRepository
from ...rest.enums.RoleEnum import RoleEnum
from ...rest.models.user.RegistrationModel import UserRegistrationModel


class UserService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.repository = UserRepository(session)
        self.role_service = RoleService(session)

    async def find_by_email(self, email: str) -> UserEntity:
        """
        Find user by email

        :param email: user email
        :return: user entity
        """
        return await self.repository.find_by_email(email)

    async def create_user(self, user_data: UserRegistrationModel) -> UserEntity:
        """
        Create a new user

        :param user_data: user data
        :return: user entity
        """
        role = await self.role_service.find_by_system_code(RoleEnum.USER)
        return await self.repository.create_user(user_data.email, user_data.password, role)
