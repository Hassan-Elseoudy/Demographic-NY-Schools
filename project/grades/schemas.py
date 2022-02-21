from typing import Optional

from pydantic import BaseModel


class GradeBase(BaseModel):
    dbn: Optional[str] = None
    school_name: Optional[str] = None
    category: Optional[str] = None
    year: Optional[str] = None
    total_enrollment: Optional[str] = None
    grade_k: Optional[str] = None
    grade_1: Optional[str] = None
    grade_2: Optional[str] = None
    grade_3: Optional[str] = None
    grade_4: Optional[str] = None
    grade_5: Optional[str] = None
    grade_6: Optional[str] = None
    grade_7: Optional[str] = None
    grade_8: Optional[str] = None
    female_1: Optional[str] = None
    female_2: Optional[str] = None
    male_1: Optional[str] = None
    male_2: Optional[str] = None
    asian_1: Optional[str] = None
    asian_2: Optional[str] = None
    black_1: Optional[str] = None
    black_2: Optional[str] = None
    hispanic_1: Optional[str] = None
    hispanic_2: Optional[str] = None
    other_1: Optional[str] = None
    other_2: Optional[str] = None
    white_1: Optional[str] = None
    white_2: Optional[str] = None
    ell_spanish_1: Optional[str] = None
    ell_spanish_2: Optional[str] = None
    ell_chinese_1: Optional[str] = None
    ell_chinese_2: Optional[str] = None
    ell_bengali_1: Optional[str] = None
    ell_bengali_2: Optional[str] = None
    ell_arabic_1: Optional[str] = None
    ell_arabic_2: Optional[str] = None
    ell_haitian_creole_1: Optional[str] = None
    ell_haitian_creole_2: Optional[str] = None
    ell_french_1: Optional[str] = None
    ell_french_2: Optional[str] = None
    ell_russian_1: Optional[str] = None
    ell_russian_2: Optional[str] = None
    ell_korean_1: Optional[str] = None
    ell_korean_2: Optional[str] = None
    ell_urdu_1: Optional[str] = None
    ell_urdu_2: Optional[str] = None
    ell_other_1: Optional[str] = None
    ell_other_2: Optional[str] = None
    ela_test_takers: Optional[str] = None
    ela_level_1_1: Optional[str] = None
    ela_level_1_2: Optional[str] = None
    ela_level_2_1: Optional[str] = None
    ela_level_2_2: Optional[str] = None
    ela_level_3_1: Optional[str] = None
    ela_level_3_2: Optional[str] = None
    ela_level_4_1: Optional[str] = None
    ela_level_4_2: Optional[str] = None
    ela_l3_l4_1: Optional[str] = None
    ela_l3_l4_2: Optional[str] = None
    math_test_takers: Optional[str] = None
    math_level_1_1: Optional[str] = None
    math_level_1_2: Optional[str] = None
    math_level_2_1: Optional[str] = None
    math_level_2_2: Optional[str] = None
    math_level_3_1: Optional[str] = None
    math_level_3_2: Optional[str] = None
    math_level_4_1: Optional[str] = None
    math_level_4_2: Optional[str] = None
    math_l3_l4_1: Optional[str] = None
    math_l3_l4_2: Optional[str] = None


class Grade(GradeBase):
    id: int

    class Config:
        orm_mode = True
