"""Added new table Feedback

Revision ID: 99e1d1b5e1bf
Revises: 84a77c789638
Create Date: 2024-06-29 11:41:21.315978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99e1d1b5e1bf'
down_revision: Union[str, None] = '84a77c789638'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
