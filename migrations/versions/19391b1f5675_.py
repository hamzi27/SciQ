"""empty message

Revision ID: 19391b1f5675
Revises: df87613c40bf
Create Date: 2020-03-30 20:58:50.745628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19391b1f5675'
down_revision = 'df87613c40bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_expression_ibfk_2', 'user_expression', type_='foreignkey')
    op.drop_constraint('user_expression_ibfk_1', 'user_expression', type_='foreignkey')
    op.create_foreign_key(None, 'user_expression', 'expression', ['expression_id'], ['id'], ondelete='cascade')
    op.create_foreign_key(None, 'user_expression', 'user', ['user_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_expression', type_='foreignkey')
    op.drop_constraint(None, 'user_expression', type_='foreignkey')
    op.create_foreign_key('user_expression_ibfk_1', 'user_expression', 'user', ['user_id'], ['id'])
    op.create_foreign_key('user_expression_ibfk_2', 'user_expression', 'expression', ['expression_id'], ['id'])
    # ### end Alembic commands ###
