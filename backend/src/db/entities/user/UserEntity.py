from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .RightEntity import RightEntity
from ...Database import BaseEntity


class UserEntity(BaseEntity):
    """
    User entity class
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    password: Mapped[str] = mapped_column(String, nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    role: Mapped["RoleEntity"] = relationship(back_populates="users")
