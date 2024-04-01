"""create schema ecommerce

Revision ID: 784a7abb86b7
Revises: 
Create Date: 2024-04-01 17:18:06.680872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '784a7abb86b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# alembic does not support creating schema directly and we need to use op.execute
def upgrade() -> None:
    op.execute('CREATE SCHEMA IF NOT EXISTS ecommerce_olist;')


def downgrade() -> None:
    op.execute('DROP SCHEMA IF EXISTS ecommerce_olist CASCADE;')
