from .RoleService import RoleService
from ...db.entities import UserEntity
from ...repositories.user.UserRepository import UserRepository
from ...rest.enums.RoleEnum import RoleEnum
from ...rest.models.user.RegistrationModel import UserRegistrationModel


class UserService:
    def __init__(self, repository: UserRepository, role_service: RoleService):
        self.repository = repository
        self.role_service = role_service

    async def create_user(self, user_data: UserRegistrationModel) -> UserEntity:
        """
        Create a new user

        :param user_data: user data
        :return: user entity
        """
        role = await self.role_service.find_by_system_code(RoleEnum.USER)
        return await self.repository.create_user(user_data.email, user_data.password, role)
