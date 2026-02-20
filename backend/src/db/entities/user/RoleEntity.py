from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from ....rest.enums.RoleEnum import RoleEnum
from ...Database import BaseEntity
from .RolesRights import RolesRightsEntity


class RoleEntity(BaseEntity):
    """
    User roles entity class
    """

    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    rights: Mapped[list["RightEntity"]] = relationship(
        secondary=RolesRightsEntity,
        back_populates="roles"
    )

    users: Mapped[list["UserEntity"]] = relationship(
        "UserEntity",
        back_populates="role"
    )

    system_code: Mapped[RoleEnum] = mapped_column(String)
