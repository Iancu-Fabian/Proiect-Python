"""empty message

Revision ID: 1440f2e8836e
Revises: 807943f0ae1e
Create Date: 2023-12-29 14:24:40.312544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1440f2e8836e'
down_revision = '807943f0ae1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('end_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('start_time', sa.Time(), nullable=True))
        batch_op.add_column(sa.Column('end_time', sa.Time(), nullable=True))
        batch_op.drop_column('start_datetime')
        batch_op.drop_column('end_datetime')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('end_datetime', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('start_datetime', sa.DATETIME(), nullable=True))
        batch_op.drop_column('end_time')
        batch_op.drop_column('start_time')
        batch_op.drop_column('end_date')
        batch_op.drop_column('start_date')

    # ### end Alembic commands ###
