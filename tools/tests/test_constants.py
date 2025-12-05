"""
Tests for core/constants.py configuration values.
"""

import pytest

from core.constants import (
    CharacterLimits,
    ScoreThresholds,
    MaturityStage,
    TechnologyReadinessLevel,
    EvidenceQuality,
    VIANEO_DIMENSIONS,
    DocxStyles,
    ValidationPatterns,
    STEP_DEPENDENCIES,
    FileNaming,
)


# =============================================================================
# CHARACTER LIMITS TESTS
# =============================================================================

class TestCharacterLimits:
    """Tests for CharacterLimits class."""

    def test_executive_brief_limits_exist(self):
        assert CharacterLimits.B1_PROJECT_NAME_TAGLINE == 150
        assert CharacterLimits.B2_PROBLEM_STATEMENT == 300
        assert CharacterLimits.B3_SOLUTION_OVERVIEW == 300
        assert CharacterLimits.B4_MARKET_DESCRIPTION == 300
        assert CharacterLimits.B5_REVENUE_MODEL == 300
        assert CharacterLimits.B6_TRACTION_STATUS == 300
        assert CharacterLimits.B7_TEAM_OVERVIEW == 200

    def test_needs_limits_exist(self):
        assert CharacterLimits.NEED_STATEMENT == 60
        assert CharacterLimits.NEED_BULLET == 60
        assert CharacterLimits.MEANS_STATEMENT == 60

    def test_persona_limits_exist(self):
        assert CharacterLimits.PERSONA_TASK == 60
        assert CharacterLimits.PERSONA_PAIN == 60
        assert CharacterLimits.PERSONA_EXPECTATION == 60

    def test_limits_are_positive(self):
        """All character limits should be positive integers."""
        for attr in dir(CharacterLimits):
            if not attr.startswith('_'):
                value = getattr(CharacterLimits, attr)
                assert isinstance(value, int)
                assert value > 0


# =============================================================================
# SCORE THRESHOLDS TESTS
# =============================================================================

class TestScoreThresholds:
    """Tests for ScoreThresholds class."""

    def test_minimum_scores_exist(self):
        assert ScoreThresholds.LEGITIMACY_MIN == 3.0
        assert ScoreThresholds.DESIRABILITY_MIN == 3.0
        assert ScoreThresholds.ACCEPTABILITY_MIN == 3.0
        assert ScoreThresholds.FEASIBILITY_MIN == 3.0
        assert ScoreThresholds.VIABILITY_MIN == 3.0

    def test_investment_ready_threshold(self):
        assert ScoreThresholds.INVESTMENT_READY_MIN == 3.5

    def test_score_ranges_defined(self):
        assert ScoreThresholds.STRONG == (4.5, 5.0)
        assert ScoreThresholds.PROMISING == (3.5, 4.49)
        assert ScoreThresholds.DEVELOPING == (3.0, 3.49)
        assert ScoreThresholds.PROBLEMATIC == (2.0, 2.99)
        assert ScoreThresholds.NON_VIABLE == (0.0, 1.99)

    def test_get_status_keyword_strong(self):
        assert ScoreThresholds.get_status_keyword(5.0) == "Strong"
        assert ScoreThresholds.get_status_keyword(4.5) == "Strong"

    def test_get_status_keyword_promising(self):
        assert ScoreThresholds.get_status_keyword(4.0) == "Promising"
        assert ScoreThresholds.get_status_keyword(3.5) == "Promising"

    def test_get_status_keyword_developing(self):
        assert ScoreThresholds.get_status_keyword(3.2) == "Developing"
        assert ScoreThresholds.get_status_keyword(3.0) == "Developing"

    def test_get_status_keyword_problematic(self):
        assert ScoreThresholds.get_status_keyword(2.5) == "Problematic"
        assert ScoreThresholds.get_status_keyword(2.0) == "Problematic"

    def test_get_status_keyword_non_viable(self):
        assert ScoreThresholds.get_status_keyword(1.5) == "Non-viable"
        assert ScoreThresholds.get_status_keyword(0.0) == "Non-viable"

    def test_get_color_code_green(self):
        color = ScoreThresholds.get_color_code(4.0)
        assert color == "#D4EDDA"

    def test_get_color_code_yellow(self):
        color = ScoreThresholds.get_color_code(3.2)
        assert color == "#FFF3CD"

    def test_get_color_code_red(self):
        color = ScoreThresholds.get_color_code(2.0)
        assert color == "#F8D7DA"


# =============================================================================
# MATURITY STAGE TESTS
# =============================================================================

class TestMaturityStage:
    """Tests for MaturityStage enum."""

    def test_all_stages_defined(self):
        stages = [stage.value for stage in MaturityStage]
        assert "IDEA" in stages
        assert "PROTOTYPE" in stages
        assert "PILOT" in stages
        assert "EARLY_COMMERCIALIZATION" in stages
        assert "GROWTH" in stages

    def test_from_string_exact_match(self):
        assert MaturityStage.from_string("IDEA") == MaturityStage.IDEA
        assert MaturityStage.from_string("GROWTH") == MaturityStage.GROWTH

    def test_from_string_case_insensitive(self):
        assert MaturityStage.from_string("idea") == MaturityStage.IDEA
        assert MaturityStage.from_string("Prototype") == MaturityStage.PROTOTYPE

    def test_from_string_with_spaces(self):
        result = MaturityStage.from_string("Early Commercialization")
        assert result == MaturityStage.EARLY_COMMERCIALIZATION

    def test_from_string_invalid(self):
        with pytest.raises(ValueError, match="Unknown maturity stage"):
            MaturityStage.from_string("INVALID")


# =============================================================================
# TECHNOLOGY READINESS LEVEL TESTS
# =============================================================================

class TestTechnologyReadinessLevel:
    """Tests for TechnologyReadinessLevel class."""

    def test_trl_descriptions_complete(self):
        descriptions = TechnologyReadinessLevel.TRL_DESCRIPTIONS
        assert len(descriptions) == 9
        for level in range(1, 10):
            assert level in descriptions
            assert isinstance(descriptions[level], str)

    def test_stage_mapping_covers_all_stages(self):
        mapping = TechnologyReadinessLevel.STAGE_MAPPING
        for stage in MaturityStage:
            assert stage in mapping
            trl_range = mapping[stage]
            assert len(trl_range) == 2
            assert trl_range[0] <= trl_range[1]


# =============================================================================
# EVIDENCE QUALITY TESTS
# =============================================================================

class TestEvidenceQuality:
    """Tests for EvidenceQuality enum."""

    def test_quality_values(self):
        assert EvidenceQuality.GOLD_STANDARD.value == 5
        assert EvidenceQuality.STRONG.value == 4
        assert EvidenceQuality.MODERATE.value == 3
        assert EvidenceQuality.WEAK.value == 2
        assert EvidenceQuality.VERY_WEAK.value == 1

    def test_description_property(self):
        desc = EvidenceQuality.GOLD_STANDARD.description
        assert "Gold Standard" in desc
        assert "Published research" in desc

    def test_all_have_descriptions(self):
        for quality in EvidenceQuality:
            assert len(quality.description) > 0


# =============================================================================
# VIANEO DIMENSIONS TESTS
# =============================================================================

class TestVIANEODimensions:
    """Tests for VIANEO_DIMENSIONS configuration."""

    def test_all_dimensions_defined(self):
        expected = ["legitimacy", "desirability", "acceptability", "feasibility", "viability"]
        for dim in expected:
            assert dim in VIANEO_DIMENSIONS

    def test_dimension_structure(self):
        for dim_key, dim_info in VIANEO_DIMENSIONS.items():
            assert "name" in dim_info
            assert "weight" in dim_info
            assert "description" in dim_info
            assert "min_score" in dim_info

    def test_weights_sum_to_one(self):
        total_weight = sum(d["weight"] for d in VIANEO_DIMENSIONS.values())
        assert abs(total_weight - 1.0) < 0.01  # Allow small float error

    def test_minimum_scores_consistent(self):
        for dim_info in VIANEO_DIMENSIONS.values():
            assert dim_info["min_score"] == 3.0


# =============================================================================
# DOCX STYLES TESTS
# =============================================================================

class TestDocxStyles:
    """Tests for DocxStyles dataclass."""

    def test_colors_are_valid_hex(self):
        styles = DocxStyles()
        hex_attrs = [
            styles.PRIMARY_BLUE, styles.MEDIUM_GRAY, styles.BODY_GRAY,
            styles.LIGHT_GRAY, styles.TABLE_BORDER, styles.TABLE_HEADER_BG,
            styles.GREEN_HIGHLIGHT, styles.YELLOW_HIGHLIGHT, styles.RED_HIGHLIGHT
        ]
        for color in hex_attrs:
            assert len(color) == 6
            assert all(c in "0123456789ABCDEFabcdef" for c in color)

    def test_font_sizes_are_positive(self):
        styles = DocxStyles()
        assert styles.TITLE_SIZE > 0
        assert styles.HEADING1_SIZE > 0
        assert styles.HEADING2_SIZE > 0
        assert styles.BODY_SIZE > 0
        assert styles.METADATA_SIZE > 0

    def test_font_family_defined(self):
        styles = DocxStyles()
        assert styles.FONT_FAMILY == "Calibri"


# =============================================================================
# VALIDATION PATTERNS TESTS
# =============================================================================

class TestValidationPatterns:
    """Tests for ValidationPatterns regex patterns."""

    def test_iso_date_pattern(self):
        import re
        pattern = ValidationPatterns.ISO_DATE
        assert re.match(pattern, "2025-01-15")
        assert not re.match(pattern, "01/15/2025")
        assert not re.match(pattern, "2025-1-15")

    def test_brief_id_pattern(self):
        import re
        pattern = ValidationPatterns.BRIEF_ID
        assert re.match(pattern, "EB-2025-001")
        assert not re.match(pattern, "EB2025001")

    def test_evidence_id_pattern(self):
        import re
        pattern = ValidationPatterns.EVIDENCE_ID
        assert re.match(pattern, "E001")
        assert re.match(pattern, "E123")
        assert not re.match(pattern, "E1")

    def test_score_format_pattern(self):
        import re
        pattern = ValidationPatterns.SCORE_FORMAT
        assert re.match(pattern, "4.5/5")
        assert re.match(pattern, "3.0/5")
        assert not re.match(pattern, "4.5")


# =============================================================================
# STEP DEPENDENCIES TESTS
# =============================================================================

class TestStepDependencies:
    """Tests for STEP_DEPENDENCIES configuration."""

    def test_dependencies_defined(self):
        assert "step_7" in STEP_DEPENDENCIES
        assert "step_9" in STEP_DEPENDENCIES
        assert "step_11_needs" in STEP_DEPENDENCIES
        assert "step_11_means" in STEP_DEPENDENCIES

    def test_step_7_dependencies(self):
        assert "step_5" in STEP_DEPENDENCIES["step_7"]

    def test_step_9_dependencies(self):
        deps = STEP_DEPENDENCIES["step_9"]
        assert "step_5" in deps
        assert "step_8" in deps


# =============================================================================
# FILE NAMING TESTS
# =============================================================================

class TestFileNaming:
    """Tests for FileNaming class."""

    def test_executive_brief_templates(self):
        assert "{project_name}" in FileNaming.EXECUTIVE_BRIEF_MD
        assert "{date}" in FileNaming.EXECUTIVE_BRIEF_MD
        assert FileNaming.EXECUTIVE_BRIEF_MD.endswith(".md")
        assert FileNaming.EXECUTIVE_BRIEF_DOCX.endswith(".docx")

    def test_personas_templates(self):
        assert "{company_name}" in FileNaming.PERSONAS_MD
        assert "{date}" in FileNaming.PERSONAS_DOCX

    def test_diagnostic_templates(self):
        assert "{project_name}" in FileNaming.DIAGNOSTIC_MD
        assert FileNaming.DIAGNOSTIC_DOCX.endswith(".docx")
