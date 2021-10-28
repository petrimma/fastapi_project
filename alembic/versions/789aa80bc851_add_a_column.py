"""Add a column

Revision ID: 789aa80bc851
Revises: 5b1b33c204e5
Create Date: 2021-10-27 17:05:30.871512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '789aa80bc851'
down_revision = '5b1b33c204e5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('documents', sa.Column('content', sa.String))


def downgrade():
    op.drop_column('documents', 'content')