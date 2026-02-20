"""Create initial roles

Revision ID: 97f7b5ec5c1b
Revises: fcaf9d61d401
Create Date: 2026-02-19 20:01:28.152131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97f7b5ec5c1b'
down_revision: Union[str, Sequence[str], None] = 'fcaf9d61d401'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
               INSERT INTO roles (name, description, system_code)
               VALUES ('System Administrator', 'System (main) administrator', 'SYSTEM_ADMIN'),
                      ('Administrator', 'Regular administrator', 'ADMIN'),
                      ('User', 'Regular User', 'USER');
               """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
               DELETE
               FROM roles
               WHERE system_code IN ('SYSTEM_ADMIN', 'ADMIN', 'USER');
               """)
