"""empty message

Revision ID: ea1ea6f1aeb1
Revises: 09927b467369
Create Date: 2021-08-16 20:32:28.310717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea1ea6f1aeb1'
down_revision = '09927b467369'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_user_profile'), 'user', ['profile'])
    op.create_unique_constraint(op.f('uq_user_signature'), 'user', ['signature'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_signature'), 'user', type_='unique')
    op.drop_constraint(op.f('uq_user_profile'), 'user', type_='unique')
    # ### end Alembic commands ###
