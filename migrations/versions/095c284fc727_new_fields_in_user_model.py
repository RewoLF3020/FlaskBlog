"""new fields in user model

Revision ID: 095c284fc727
Revises: b65d0ec02b5c
Create Date: 2023-10-31 00:18:47.811660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '095c284fc727'
down_revision = 'b65d0ec02b5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
