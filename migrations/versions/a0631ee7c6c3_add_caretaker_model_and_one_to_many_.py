"""Add Caretaker model and one-to-many-relationship with Cat

Revision ID: a0631ee7c6c3
Revises: 735e47d855f8
Create Date: 2023-05-08 13:40:19.696602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0631ee7c6c3'
down_revision = '735e47d855f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cat', sa.Column('caretaker_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cat', 'caretaker', ['caretaker_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cat', type_='foreignkey')
    op.drop_column('cat', 'caretaker_id')
    # ### end Alembic commands ###