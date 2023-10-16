"""empty message

Revision ID: 030a2669d7cd
Revises: d4c5afd5e00e
Create Date: 2023-10-13 09:05:13.967377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '030a2669d7cd'
down_revision = 'd4c5afd5e00e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###