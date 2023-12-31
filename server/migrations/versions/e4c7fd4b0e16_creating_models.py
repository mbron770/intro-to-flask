"""creating models

Revision ID: e4c7fd4b0e16
Revises: 
Create Date: 2023-07-24 11:20:19.469985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c7fd4b0e16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(), nullable=False),
    sa.Column('lname', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.CheckConstraint('age>=18 and age<=65', name='age_check_constraint'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instructors',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tenured', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('instructor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['instructor_id'], ['instructors.user_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    op.drop_table('instructors')
    op.drop_table('users')
    # ### end Alembic commands ###
