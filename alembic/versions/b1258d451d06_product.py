"""product

Revision ID: b1258d451d06
Revises: 
Create Date: 2023-06-11 06:37:55.907259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1258d451d06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_product',
    sa.Column('id_product', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('product_name', sa.String(), nullable=False, comment='Product Name'),
    sa.PrimaryKeyConstraint('id_product')
    )
    op.create_index(op.f('ix_t_product_id_product'), 't_product', ['id_product'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_t_product_id_product'), table_name='t_product')
    op.drop_table('t_product')
    # ### end Alembic commands ###