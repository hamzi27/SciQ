"""empty message

Revision ID: 0e3933519c75
Revises: 2b277b4bb278
Create Date: 2020-05-07 15:57:43.328900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e3933519c75'
down_revision = '2b277b4bb278'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_application_username_fk'), 'application', ['username_fk'], unique=False)
    op.drop_index('ix_application_username', table_name='application')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_application_username', 'application', ['username_fk'], unique=False)
    op.drop_index(op.f('ix_application_username_fk'), table_name='application')
    # ### end Alembic commands ###
