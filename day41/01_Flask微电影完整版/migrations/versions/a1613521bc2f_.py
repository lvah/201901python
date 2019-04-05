"""empty message

Revision ID: a1613521bc2f
Revises: 03d223d3a48c
Create Date: 2019-03-24 17:22:11.787948

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a1613521bc2f'
down_revision = '03d223d3a48c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('auth_ibfk_1', 'auth', type_='foreignkey')
    op.drop_column('auth', 'role_id')
    op.add_column('role', sa.Column('auths', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'auths')
    op.add_column('auth', sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('auth_ibfk_1', 'auth', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###
