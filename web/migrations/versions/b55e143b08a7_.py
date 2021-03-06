"""empty message

Revision ID: b55e143b08a7
Revises: 19391b1f5675
Create Date: 2020-04-05 13:00:27.819798

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b55e143b08a7'
down_revision = '19391b1f5675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expression', sa.Column('integral', sa.String(length=128), nullable=True))
    op.add_column('expression', sa.Column('limits', sa.String(length=128), nullable=True))
    op.add_column('expression', sa.Column('partial_derivates', sa.String(length=128), nullable=True))
    op.add_column('expression', sa.Column('plots', sa.String(length=128), nullable=True))
    op.add_column('expression', sa.Column('results', sa.String(length=128), nullable=True))
    op.add_column('expression', sa.Column('symbolic_solutions', sa.String(length=128), nullable=True))
    op.drop_index('ix_expression_expression_type', table_name='expression')
    op.drop_column('expression', 'plot')
    op.drop_column('expression', 'expression_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expression', sa.Column('expression_type', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('expression', sa.Column('plot', mysql.VARCHAR(length=128), nullable=True))
    op.create_index('ix_expression_expression_type', 'expression', ['expression_type'], unique=False)
    op.drop_column('expression', 'symbolic_solutions')
    op.drop_column('expression', 'results')
    op.drop_column('expression', 'plots')
    op.drop_column('expression', 'partial_derivates')
    op.drop_column('expression', 'limits')
    op.drop_column('expression', 'integral')
    # ### end Alembic commands ###
