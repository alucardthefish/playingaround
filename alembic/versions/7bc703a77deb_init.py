"""init

Revision ID: 7bc703a77deb
Revises: 
Create Date: 2023-01-15 16:15:13.414784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bc703a77deb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    	"jobs",
    	sa.Column("id", sa.Integer, primary_key=True),
    	sa.Column("title", sa.String, nullable=False),
    	sa.Column("description", sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("jobs")
