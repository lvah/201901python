"""empty message

Revision ID: 72042cc52eb8
Revises: 76ef35536e41
Create Date: 2019-03-29 13:56:47.791171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72042cc52eb8'
down_revision = '76ef35536e41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('logo', table_name='movie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('logo', 'movie', ['logo'], unique=True)
    # ### end Alembic commands ###
