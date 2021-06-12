"""empty message

Revision ID: 7efefd475d11
Revises: 674c43ef7815
Create Date: 2021-06-11 18:13:31.482086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7efefd475d11'
down_revision = '674c43ef7815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id')
    )
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('looking_for_talent', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_Description', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.alter_column('Venue', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_column('Venue', 'website_link')
    op.drop_column('Artist', 'seeking_Description')
    op.drop_column('Artist', 'looking_for_talent')
    op.drop_column('Artist', 'website_link')
    op.drop_table('Shows')
    # ### end Alembic commands ###
