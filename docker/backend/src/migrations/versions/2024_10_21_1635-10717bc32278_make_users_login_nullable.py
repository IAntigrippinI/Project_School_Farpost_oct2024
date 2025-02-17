"""make users.login nullable

Revision ID: 10717bc32278
Revises: 38623e70b652
Create Date: 2024-10-21 16:35:22.840026

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "10717bc32278"
down_revision: Union[str, None] = "38623e70b652"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "login", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "login", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
