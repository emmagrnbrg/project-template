from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import select

from ..BaseRepository import BaseRepository
from ...core.security import hash_password
from ...db.entities import UserEntity, RoleEntity
from ...errors.user.RegistrationError import DuplicateEmailError


class UserRepository(BaseRepository):
    async def find_by_email(self, email: str) -> UserEntity:
        """
        Find user by email

        :param email: user email
        :return: user entity
        """
        user = (
            select(UserEntity)
            .where(UserEntity.email == email)
            .options(
                selectinload(UserEntity.role).selectinload(RoleEntity.rights)
            )
        )
        result = await self.session.execute(user)
        return result.scalar_one_or_none()

    async def create_user(self, email: str, password: str, role: RoleEntity) -> UserEntity:
        """
        Create a new user

        :param email:    user's email
        :param password: user's password
        :param role:     user's role
        :return: user entity
        """
        user = UserEntity()

        user.email = email
        user.password = hash_password(password)
        user.role_id = role.id
        user.role = role

        self.session.add(user)

        try:
            await self.session.flush()
            await self.session.commit()
        except IntegrityError as e:
            await self.session.rollback()

            if "ix_users_email" in str(e.orig):
                raise DuplicateEmailError(email)

            raise

        return user
