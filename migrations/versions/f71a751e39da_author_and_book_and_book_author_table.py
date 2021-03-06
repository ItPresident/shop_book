"""author and book and book_author table

Revision ID: f71a751e39da
Revises: 8eb433a22ea9
Create Date: 2021-03-15 18:17:25.486364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f71a751e39da'
down_revision = '8eb433a22ea9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('booktitle', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('book_author',
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.author_id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], )
    )
    op.add_column('author', sa.Column('author_id', sa.Integer(), nullable=False))
    op.drop_column('author', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_column('author', 'author_id')
    op.drop_table('book_author')
    op.drop_table('book')
    # ### end Alembic commands ###
