"""init

Revision ID: 5b1b33c204e5
Revises: 
Create Date: 2021-10-27 15:52:08.051222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1b33c204e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "documents",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("date", sa.String()),
        sa.Column("date", sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table("documents")
