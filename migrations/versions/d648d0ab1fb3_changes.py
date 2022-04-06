"""Changes

Revision ID: d648d0ab1fb3
Revises: 
Create Date: 2022-04-06 13:59:32.714746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd648d0ab1fb3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bungalows', 'updated_at',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('bungalows', 'deleted_at',
               existing_type=sa.DATE(),
               nullable=True)
    op.add_column('reservations', sa.Column('start_date', sa.Date(), nullable=False))
    op.alter_column('reservations', 'updated_at',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('reservations', 'deleted_at',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_column('reservations', 'begin_date')
    op.add_column('users', sa.Column('first_name', sa.String(length=1000), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=1000), nullable=True))
    op.add_column('users', sa.Column('phone_nr', sa.String(length=1000), nullable=True))
    op.alter_column('users', 'updated_at',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('users', 'deleted_at',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=1000), nullable=True))
    op.alter_column('users', 'deleted_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('users', 'updated_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_column('users', 'phone_nr')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.add_column('reservations', sa.Column('begin_date', sa.DATE(), nullable=False))
    op.alter_column('reservations', 'deleted_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('reservations', 'updated_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_column('reservations', 'start_date')
    op.alter_column('bungalows', 'deleted_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('bungalows', 'updated_at',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
