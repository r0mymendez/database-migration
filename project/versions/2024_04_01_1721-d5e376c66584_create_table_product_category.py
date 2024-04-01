"""create table product_category

Revision ID: d5e376c66584
Revises: b1bc43e2f536
Create Date: 2024-04-01 17:21:12.549394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5e376c66584'
down_revision: Union[str, None] = 'b1bc43e2f536'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'product_category',
        sa.Column('product_id', sa.Integer, primary_key=True),
        sa.Column('product_category_name', sa.Text),
        schema='ecommerce_olist'
    )

def downgrade():
    op.drop_table('product_category', schema='ecommerce_olist')

