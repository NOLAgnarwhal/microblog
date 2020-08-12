"""new fields in user model

Revision ID: 718cc0f1e7f4
Revises: 41bbb7601650
Create Date: 2020-08-12 15:42:18.624654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '718cc0f1e7f4'
down_revision = '41bbb7601650'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
