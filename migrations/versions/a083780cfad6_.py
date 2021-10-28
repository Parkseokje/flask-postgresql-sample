"""empty message

Revision ID: a083780cfad6
Revises: 
Create Date: 2021-10-25 16:35:16.326641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a083780cfad6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('building',
    sa.Column('id', sa.String(length=25), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('desc', sa.String(length=50), nullable=True),
    sa.Column('addr', sa.String(length=100), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('xcoord', sa.Float(), nullable=False),
    sa.Column('ycoord', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('building_id', sa.String(length=25), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['building_id'], ['building.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('polygon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('building_id', sa.String(length=25), nullable=False),
    sa.Column('seq', sa.Integer(), nullable=True),
    sa.Column('area', sa.Float(), nullable=True),
    sa.Column('xycoords', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['building_id'], ['building.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('polygon')
    op.drop_table('object')
    op.drop_table('answer')
    op.drop_table('question')
    op.drop_table('building')
    # ### end Alembic commands ###