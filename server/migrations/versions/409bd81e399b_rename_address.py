"""rename address

Revision ID: 409bd81e399b
Revises: 964f6c248cf0
Create Date: 2023-11-12 17:24:59.622457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "409bd81e399b"
down_revision = "964f6c248cf0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments", "address", new_column_name="location")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments", "location", new_column_name="address")
    # ### end Alembic commands ###
