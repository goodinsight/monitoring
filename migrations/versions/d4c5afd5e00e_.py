"""empty message

Revision ID: d4c5afd5e00e
Revises: 1fdaf9b0b224
Create Date: 2023-10-12 13:55:48.533943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4c5afd5e00e'
down_revision = '1fdaf9b0b224'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('structure', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ch2_c', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('structure', schema=None) as batch_op:
        batch_op.drop_column('ch2_c')

    # ### end Alembic commands ###