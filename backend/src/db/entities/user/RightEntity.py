from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .RolesRights import RolesRightsEntity
from ....rest.enums.RightEnum import RightEnum
from ...Database import BaseEntity


class RightEntity(BaseEntity):
    """
    User rights entity class
    """

    __tablename__ = "rights"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[RightEnum] = mapped_column(String, unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    roles: Mapped[list["RoleEntity"]] = relationship(
        secondary=RolesRightsEntity,
        back_populates="rights"
    )
