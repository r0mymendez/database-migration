"""insert a new product_category

Revision ID: 33083bd5e3b1
Revises: d5e376c66584
Create Date: 2024-04-01 17:21:39.290164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33083bd5e3b1'
down_revision: Union[str, None] = 'd5e376c66584'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.execute(
        """
        INSERT INTO ecommerce_olist.product_category (product_id, product_category_name)
        VALUES (1,'new_category'),(2,'new_category2')
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM ecommerce_olist.product_category
        WHERE product_id IN (1,2)
        """
    )

