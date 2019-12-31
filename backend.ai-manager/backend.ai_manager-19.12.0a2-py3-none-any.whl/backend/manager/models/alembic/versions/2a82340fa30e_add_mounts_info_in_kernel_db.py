"""add_mounts_info_in_kernel_db

Revision ID: 2a82340fa30e
Revises: c1409ad0e8da
Create Date: 2019-08-01 15:59:41.807766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a82340fa30e'
down_revision = 'c1409ad0e8da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kernels', sa.Column('mounts', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kernels', 'mounts')
    # ### end Alembic commands ###
