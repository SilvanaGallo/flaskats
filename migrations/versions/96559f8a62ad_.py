"""empty message

Revision ID: 96559f8a62ad
Revises: 643ec3559e07
Create Date: 2023-01-13 10:23:09.501547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96559f8a62ad'
down_revision = '643ec3559e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('offer', 'repository_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('offer', 'code',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('offer', 'code',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.alter_column('offer', 'repository_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
