from sqlalchemy import Column, Table, ForeignKey

from ...Database import BaseEntity

"""
Rights to roles entity class
"""
RolesRightsEntity = Table(
    "roles_rights",
    BaseEntity.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("right_id", ForeignKey("rights.id"), primary_key=True),
)
