"""empty message

Revision ID: df87613c40bf
Revises: 3baef1f489ad
Create Date: 2020-03-30 20:50:23.009155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df87613c40bf'
down_revision = '3baef1f489ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_expression_ibfk_1', 'user_expression', type_='foreignkey')
    op.drop_constraint('user_expression_ibfk_2', 'user_expression', type_='foreignkey')
    op.create_foreign_key(None, 'user_expression', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_expression', 'expression', ['expression_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_expression', type_='foreignkey')
    op.drop_constraint(None, 'user_expression', type_='foreignkey')
    op.create_foreign_key('user_expression_ibfk_2', 'user_expression', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('user_expression_ibfk_1', 'user_expression', 'expression', ['expression_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
