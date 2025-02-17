"""edit events

Revision ID: 38623e70b652
Revises: 1fb8e433c44d
Create Date: 2024-10-21 14:40:06.396896

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "38623e70b652"
down_revision: Union[str, None] = "1fb8e433c44d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("events", sa.Column("category", sa.String(), nullable=False))
    op.drop_constraint("events_category_id_fkey", "events", type_="foreignkey")
    op.drop_column("events", "category_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "events",
        sa.Column("category_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "events_category_id_fkey", "events", "categories", ["category_id"], ["id"]
    )
    op.drop_column("events", "category")
    # ### end Alembic commands ###
