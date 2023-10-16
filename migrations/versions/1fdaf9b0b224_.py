"""empty message

Revision ID: 1fdaf9b0b224
Revises: 
Create Date: 2023-10-12 12:40:01.570078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fdaf9b0b224'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('structur_tiltmeter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('opdatetime', sa.String(length=200), nullable=False),
    sa.Column('tilt_01_x', sa.Float(), nullable=False),
    sa.Column('tilt_01_y', sa.Float(), nullable=False),
    sa.Column('tilt_02_x', sa.Float(), nullable=False),
    sa.Column('tilt_02_y', sa.Float(), nullable=False),
    sa.Column('tilt_03_x', sa.Float(), nullable=False),
    sa.Column('tilt_03_y', sa.Float(), nullable=False),
    sa.Column('tilt_04_x', sa.Float(), nullable=False),
    sa.Column('tilt_04_y', sa.Float(), nullable=False),
    sa.Column('tilt_05_x', sa.Float(), nullable=False),
    sa.Column('tilt_05_y', sa.Float(), nullable=False),
    sa.Column('tilt_06_x', sa.Float(), nullable=False),
    sa.Column('tilt_06_y', sa.Float(), nullable=False),
    sa.Column('tilt_07_x', sa.Float(), nullable=False),
    sa.Column('tilt_07_y', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('structure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=200), nullable=False),
    sa.Column('batt', sa.Float(), nullable=False),
    sa.Column('temp', sa.Float(), nullable=False),
    sa.Column('ch1_a', sa.Float(), nullable=False),
    sa.Column('ch1_b', sa.Float(), nullable=False),
    sa.Column('ch1_c', sa.Float(), nullable=False),
    sa.Column('ch1_d', sa.Float(), nullable=False),
    sa.Column('ch2_a', sa.Float(), nullable=False),
    sa.Column('ch2_b', sa.Float(), nullable=False),
    sa.Column('ch2_d', sa.Float(), nullable=False),
    sa.Column('ch3_a', sa.Float(), nullable=False),
    sa.Column('ch3_b', sa.Float(), nullable=False),
    sa.Column('ch3_c', sa.Float(), nullable=False),
    sa.Column('ch3_d', sa.Float(), nullable=False),
    sa.Column('ch4_a', sa.Float(), nullable=False),
    sa.Column('ch4_b', sa.Float(), nullable=False),
    sa.Column('ch4_c', sa.Float(), nullable=False),
    sa.Column('ch4_d', sa.Float(), nullable=False),
    sa.Column('ch5_a', sa.Float(), nullable=False),
    sa.Column('ch5_b', sa.Float(), nullable=False),
    sa.Column('ch5_c', sa.Float(), nullable=False),
    sa.Column('ch5_d', sa.Float(), nullable=False),
    sa.Column('ch6_a', sa.Float(), nullable=False),
    sa.Column('ch6_b', sa.Float(), nullable=False),
    sa.Column('ch6_c', sa.Float(), nullable=False),
    sa.Column('ch6_d', sa.Float(), nullable=False),
    sa.Column('ch7_a', sa.Float(), nullable=False),
    sa.Column('ch7_b', sa.Float(), nullable=False),
    sa.Column('ch7_c', sa.Float(), nullable=False),
    sa.Column('ch7_d', sa.Float(), nullable=False),
    sa.Column('ch8_a', sa.Float(), nullable=False),
    sa.Column('ch8_b', sa.Float(), nullable=False),
    sa.Column('ch8_c', sa.Float(), nullable=False),
    sa.Column('ch8_d', sa.Float(), nullable=False),
    sa.Column('ch9_a', sa.Float(), nullable=False),
    sa.Column('ch9_b', sa.Float(), nullable=False),
    sa.Column('ch9_c', sa.Float(), nullable=False),
    sa.Column('ch9_d', sa.Float(), nullable=False),
    sa.Column('ch10_a', sa.Float(), nullable=False),
    sa.Column('ch10_b', sa.Float(), nullable=False),
    sa.Column('ch10_c', sa.Float(), nullable=False),
    sa.Column('ch10_d', sa.Float(), nullable=False),
    sa.Column('ch11_a', sa.Float(), nullable=False),
    sa.Column('ch11_b', sa.Float(), nullable=False),
    sa.Column('ch11_c', sa.Float(), nullable=False),
    sa.Column('ch11_d', sa.Float(), nullable=False),
    sa.Column('ch12_a', sa.Float(), nullable=False),
    sa.Column('ch12_b', sa.Float(), nullable=False),
    sa.Column('ch12_c', sa.Float(), nullable=False),
    sa.Column('ch12_d', sa.Float(), nullable=False),
    sa.Column('ch13_a', sa.Float(), nullable=False),
    sa.Column('ch13_b', sa.Float(), nullable=False),
    sa.Column('ch13_c', sa.Float(), nullable=False),
    sa.Column('ch13_d', sa.Float(), nullable=False),
    sa.Column('ch14_a', sa.Float(), nullable=False),
    sa.Column('ch14_b', sa.Float(), nullable=False),
    sa.Column('ch14_c', sa.Float(), nullable=False),
    sa.Column('ch14_d', sa.Float(), nullable=False),
    sa.Column('ch15_a', sa.Float(), nullable=False),
    sa.Column('ch15_b', sa.Float(), nullable=False),
    sa.Column('ch15_c', sa.Float(), nullable=False),
    sa.Column('ch15_d', sa.Float(), nullable=False),
    sa.Column('ch16_a', sa.Float(), nullable=False),
    sa.Column('ch16_b', sa.Float(), nullable=False),
    sa.Column('ch16_c', sa.Float(), nullable=False),
    sa.Column('ch16_d', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('structure')
    op.drop_table('structur_tiltmeter')
    # ### end Alembic commands ###