"""Initial migration

Revision ID: f2f5e882561e
Revises: 
Create Date: 2024-12-05 14:53:02.734636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2f5e882561e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('title', sa.String(), nullable=False))
    op.add_column('todos', sa.Column('sort', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'sort')
    op.drop_column('todos', 'title')
    # ### end Alembic commands ###
