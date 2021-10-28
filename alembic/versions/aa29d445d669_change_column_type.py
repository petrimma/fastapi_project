"""Change column type

Revision ID: aa29d445d669
Revises: 789aa80bc851
Create Date: 2021-10-28 12:51:19.510665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa29d445d669'
down_revision = '789aa80bc851'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        table_name="documents",
        column_name="date",
        existing_type=sa.String(),
        type_=sa.DateTime(),
        postgresql_using="date::timestamp without time zone"
    )


def downgrade():
    op.alter_column(
        table_name="documents",
        column_name="date",
        existing_type=sa.String(),
        type_=sa.DateTime(),
        postgresql_using="date::timestamp without time zone"

    )
