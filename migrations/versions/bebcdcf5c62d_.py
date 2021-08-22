"""empty message

Revision ID: bebcdcf5c62d
Revises: 3e16ebc3bf96
Create Date: 2021-08-22 14:08:28.287343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bebcdcf5c62d'
down_revision = '3e16ebc3bf96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('timestamp', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'timestamp')
    # ### end Alembic commands ###