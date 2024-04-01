"""create table seller

Revision ID: b036a88df8fb
Revises: 358cebb507a0
Create Date: 2024-04-01 17:23:24.358505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b036a88df8fb'
down_revision: Union[str, None] = '358cebb507a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
