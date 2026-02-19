from sqlalchemy.sql.expression import select

from ..BaseRepository import BaseRepository
from ...rest.enums.RoleEnum import RoleEnum
from ...db.entities import RoleEntity


class RoleRepository(BaseRepository):
    async def find_by_system_code(self, system_code: RoleEnum) -> RoleEntity:
        """
        Find user's role by system code

        :param system_code: system code (user / admin / etc.)
        :return: user's role entity
        """
        role = select(RoleEntity).where(RoleEntity.system_code == system_code)
        result = await self.session.execute(role)
        return result.scalar_one_or_none()
