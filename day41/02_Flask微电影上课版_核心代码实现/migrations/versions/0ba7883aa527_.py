"""empty message

Revision ID: 0ba7883aa527
Revises: 
Create Date: 2019-03-30 10:01:48.994012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba7883aa527'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('comment_num', sa.Integer(), nullable=True))
    op.add_column('movie', sa.Column('play_num', sa.Integer(), nullable=True))
    op.drop_index('ix_movie_name', table_name='movie')
    op.create_index(op.f('ix_movie_name'), 'movie', ['name'], unique=False)
    op.drop_index('logo', table_name='movie')
    op.drop_index('url', table_name='movie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('url', 'movie', ['url'], unique=True)
    op.create_index('logo', 'movie', ['logo'], unique=True)
    op.drop_index(op.f('ix_movie_name'), table_name='movie')
    op.create_index('ix_movie_name', 'movie', ['name'], unique=True)
    op.drop_column('movie', 'play_num')
    op.drop_column('movie', 'comment_num')
    # ### end Alembic commands ###
