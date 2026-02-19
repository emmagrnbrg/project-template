from ...db.entities import RoleEntity
from ...repositories.user.RoleRepository import RoleRepository
from ...rest.enums.RoleEnum import RoleEnum


class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def find_by_system_code(self, system_code: RoleEnum) -> RoleEntity:
        """
        Find user's role by system code

        :param system_code: system code (user / admin / etc.)
        :return: user's role entity
        """
        return await self.repository.find_by_system_code(system_code)
