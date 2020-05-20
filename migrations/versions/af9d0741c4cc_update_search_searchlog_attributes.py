"""Update search_searchlog attributes

Revision ID: af9d0741c4cc
Revises: 934b74ac20ce
Create Date: 2020-05-15 17:34:05.781935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af9d0741c4cc'
down_revision = '934b74ac20ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('search_searchlog', 'area',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('search_searchlog', 'start_time',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('search_searchlog', 'team',
               existing_type=sa.VARCHAR(length=25),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('search_searchlog', 'team',
               existing_type=sa.VARCHAR(length=25),
               nullable=True)
    op.alter_column('search_searchlog', 'start_time',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('search_searchlog', 'area',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###