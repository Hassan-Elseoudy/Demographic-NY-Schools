"""Add Columns

Revision ID: 1de601b346b1
Revises: 0047ac32f579
Create Date: 2022-02-21 12:34:12.013063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1de601b346b1'
down_revision = '0047ac32f579'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'grade',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dbn', sa.String(128), nullable=True),
        sa.Column('school_name', sa.String(128), nullable=True),
        sa.Column('category', sa.String(128), nullable=True),
        sa.Column('year', sa.String(128), nullable=True),
        sa.Column('total_enrollment', sa.String(128), nullable=True),
        sa.Column('grade_k', sa.String(128), nullable=True),
        sa.Column('grade_1', sa.String(128), nullable=True),
        sa.Column('grade_2', sa.String(128), nullable=True),
        sa.Column('grade_3', sa.String(128), nullable=True),
        sa.Column('grade_4', sa.String(128), nullable=True),
        sa.Column('grade_5', sa.String(128), nullable=True),
        sa.Column('grade_6', sa.String(128), nullable=True),
        sa.Column('grade_7', sa.String(128), nullable=True),
        sa.Column('grade_8', sa.String(128), nullable=True),
        sa.Column('female_1', sa.String(128), nullable=True),
        sa.Column('female_2', sa.String(128), nullable=True),
        sa.Column('male_1', sa.String(128), nullable=True),
        sa.Column('male_2', sa.String(128), nullable=True),
        sa.Column('asian_1', sa.String(128), nullable=True),
        sa.Column('asian_2', sa.String(128), nullable=True),
        sa.Column('black_1', sa.String(128), nullable=True),
        sa.Column('black_2', sa.String(128), nullable=True),
        sa.Column('hispanic_1', sa.String(128), nullable=True),
        sa.Column('hispanic_2', sa.String(128), nullable=True),
        sa.Column('other_1', sa.String(128), nullable=True),
        sa.Column('other_2', sa.String(128), nullable=True),
        sa.Column('white_1', sa.String(128), nullable=True),
        sa.Column('white_2', sa.String(128), nullable=True),
        sa.Column('ell_spanish_1', sa.String(128), nullable=True),
        sa.Column('ell_spanish_2', sa.String(128), nullable=True),
        sa.Column('ell_chinese_1', sa.String(128), nullable=True),
        sa.Column('ell_chinese_2', sa.String(128), nullable=True),
        sa.Column('ell_bengali_1', sa.String(128), nullable=True),
        sa.Column('ell_bengali_2', sa.String(128), nullable=True),
        sa.Column('ell_arabic_1', sa.String(128), nullable=True),
        sa.Column('ell_arabic_2', sa.String(128), nullable=True),
        sa.Column('ell_haitian_creole_1', sa.String(128), nullable=True),
        sa.Column('ell_haitian_creole_2', sa.String(128), nullable=True),
        sa.Column('ell_french_1', sa.String(128), nullable=True),
        sa.Column('ell_french_2', sa.String(128), nullable=True),
        sa.Column('ell_russian_1', sa.String(128), nullable=True),
        sa.Column('ell_russian_2', sa.String(128), nullable=True),
        sa.Column('ell_korean_1', sa.String(128), nullable=True),
        sa.Column('ell_korean_2', sa.String(128), nullable=True),
        sa.Column('ell_urdu_1', sa.String(128), nullable=True),
        sa.Column('ell_urdu_2', sa.String(128), nullable=True),
        sa.Column('ell_other_1', sa.String(128), nullable=True),
        sa.Column('ell_other_2', sa.String(128), nullable=True),
        sa.Column('ela_test_takers', sa.String(128), nullable=True),
        sa.Column('ela_level_1_1', sa.String(128), nullable=True),
        sa.Column('ela_level_1_2', sa.String(128), nullable=True),
        sa.Column('ela_level_2_1', sa.String(128), nullable=True),
        sa.Column('ela_level_2_2', sa.String(128), nullable=True),
        sa.Column('ela_level_3_1', sa.String(128), nullable=True),
        sa.Column('ela_level_3_2', sa.String(128), nullable=True),
        sa.Column('ela_level_4_1', sa.String(128), nullable=True),
        sa.Column('ela_level_4_2', sa.String(128), nullable=True),
        sa.Column('ela_l3_l4_1', sa.String(128), nullable=True),
        sa.Column('ela_l3_l4_2', sa.String(128), nullable=True),
        sa.Column('math_test_takers', sa.String(128), nullable=True),
        sa.Column('math_level_1_1', sa.String(128), nullable=True),
        sa.Column('math_level_1_2', sa.String(128), nullable=True),
        sa.Column('math_level_2_1', sa.String(128), nullable=True),
        sa.Column('math_level_2_2', sa.String(128), nullable=True),
        sa.Column('math_level_3_1', sa.String(128), nullable=True),
        sa.Column('math_level_3_2', sa.String(128), nullable=True),
        sa.Column('math_level_4_1', sa.String(128), nullable=True),
        sa.Column('math_level_4_2', sa.String(128), nullable=True),
        sa.Column('math_l3_l4_1', sa.String(128), nullable=True),
        sa.Column('math_l3_l4_2', sa.String(128), nullable=True)
    )

def downgrade():
    op.drop_table('account')
