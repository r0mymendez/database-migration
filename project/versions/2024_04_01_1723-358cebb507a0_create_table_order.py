"""create table order

Revision ID: 358cebb507a0
Revises: 33083bd5e3b1
Create Date: 2024-04-01 17:23:21.615597

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '358cebb507a0'
down_revision: Union[str, None] = '33083bd5e3b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
