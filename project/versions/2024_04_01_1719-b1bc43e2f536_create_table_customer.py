"""create table customer

Revision ID: b1bc43e2f536
Revises: 784a7abb86b7
Create Date: 2024-04-01 17:19:09.844065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1bc43e2f536'
down_revision: Union[str, None] = '784a7abb86b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.create_table(
        'customers',
        sa.Column('customer_id', sa.Text, primary_key=True),
        sa.Column('customer_unique_id', sa.Text),
        sa.Column('customer_zip_code_prefix', sa.Integer),
        sa.Column('customer_city', sa.Text),
        sa.Column('customer_state', sa.Text),
        schema='ecommerce_olist'
    )

def downgrade():
    op.drop_table('customers', schema='ecommerce_olist')
