"""Create order product association table21

Revision ID: 8313935be746
Revises: 647c2b05abdf
Create Date: 2024-01-06 18:55:26.313043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8313935be746'
down_revision: Union[str, None] = '647c2b05abdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_product_association', sa.Column('count', sa.Integer(), server_default='1', nullable=False))
    op.add_column('order_product_association', sa.Column('unit_price', sa.Integer(), server_default='0', nullable=False))
    op.drop_column('orders', 'price')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('price', sa.INTEGER(), nullable=False))
    op.drop_column('order_product_association', 'unit_price')
    op.drop_column('order_product_association', 'count')
    # ### end Alembic commands ###