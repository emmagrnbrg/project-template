from enum import Enum


class RoleEnum(str, Enum):
    SYSTEM_ADMIN = "SYSTEM_ADMIN"
    ADMIN = "ADMIN"
    USER = "USER"
