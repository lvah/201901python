"""添加用户性别

Revision ID: bc15c10ae693
Revises: 
Create Date: 2019-03-10 13:49:36.248377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc15c10ae693'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('\u7f51\u7ad9\u7528\u6237', sa.Column('gender', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('网站用户', 'gender')
    # ### end Alembic commands ###
