"""adding day_length, year_length, and average_temp columns to Planet table

Revision ID: 4d6241440afd
Revises: 526e15dd9449
Create Date: 2021-05-04 19:59:02.459359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d6241440afd'
down_revision = '526e15dd9449'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('average_temp', sa.Float(), nullable=True))
    op.add_column('planet', sa.Column('day_length', sa.Float(), nullable=True))
    op.add_column('planet', sa.Column('year_length', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'year_length')
    op.drop_column('planet', 'day_length')
    op.drop_column('planet', 'average_temp')
    # ### end Alembic commands ###
