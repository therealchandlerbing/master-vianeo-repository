"""
Tests for core/validators.py validation functions.
"""

import pytest

from core.validators import (
    # Base validators
    validate_required_field,
    validate_char_limit,
    validate_pattern,
    validate_score_range,
    validate_score_threshold,
    validate_list_count,
    # Content validators
    validate_no_em_dashes,
    validate_solution_neutral,
    validate_quantification,
    validate_no_vague_terms,
    # Structure validators
    validate_markdown_structure,
    validate_table_structure,
    # Cross-step validators
    validate_step_dependencies,
    validate_data_consistency,
    # Dimension validators
    validate_dimension_scores,
)
from core.constants import ValidationPatterns


# =============================================================================
# BASE VALIDATORS TESTS
# =============================================================================

class TestValidateRequiredField:
    """Tests for validate_required_field function."""

    def test_present_field(self):
        result = validate_required_field("value", "my_field")
        assert result.is_valid is True

    def test_none_field(self):
        result = validate_required_field(None, "my_field")
        assert result.is_valid is False
        assert "missing" in result.message

    def test_empty_string(self):
        result = validate_required_field("", "my_field")
        assert result.is_valid is False
        assert "empty" in result.message

    def test_whitespace_only(self):
        result = validate_required_field("   ", "my_field")
        assert result.is_valid is False

    def test_allow_empty_true(self):
        result = validate_required_field("", "my_field", allow_empty=True)
        assert result.is_valid is True


class TestValidateCharLimit:
    """Tests for validate_char_limit function."""

    def test_within_limit(self):
        result = validate_char_limit("short text", 100, "field")
        assert result.is_valid is True
        assert "10/100" in result.message

    def test_over_limit(self):
        result = validate_char_limit("this is too long", 5, "field")
        assert result.is_valid is False
        assert "over by" in result.message

    def test_exact_limit(self):
        result = validate_char_limit("12345", 5, "field")
        assert result.is_valid is True

    def test_details_included(self):
        result = validate_char_limit("test", 100, "field")
        assert result.details["count"] == 4
        assert result.details["limit"] == 100


class TestValidatePattern:
    """Tests for validate_pattern function."""

    def test_matching_pattern(self):
        result = validate_pattern("2025-01-15", ValidationPatterns.ISO_DATE, "date")
        assert result.is_valid is True

    def test_non_matching_pattern(self):
        result = validate_pattern("01/15/2025", ValidationPatterns.ISO_DATE, "date")
        assert result.is_valid is False

    def test_custom_description(self):
        result = validate_pattern("invalid", r"\d+", "number", "numeric format")
        assert "numeric format" in result.message


class TestValidateScoreRange:
    """Tests for validate_score_range function."""

    def test_valid_score(self):
        result = validate_score_range(4.0, "dimension")
        assert result.is_valid is True
        assert "4.0/5" in result.message

    def test_score_below_range(self):
        result = validate_score_range(-1.0, "dimension")
        assert result.is_valid is False
        assert "outside valid range" in result.message

    def test_score_above_range(self):
        result = validate_score_range(6.0, "dimension")
        assert result.is_valid is False

    def test_boundary_scores(self):
        assert validate_score_range(0.0, "test").is_valid is True
        assert validate_score_range(5.0, "test").is_valid is True

    def test_custom_range(self):
        result = validate_score_range(7.0, "custom", min_score=1.0, max_score=10.0)
        assert result.is_valid is True


class TestValidateScoreThreshold:
    """Tests for validate_score_threshold function."""

    def test_meets_threshold(self):
        result = validate_score_threshold(4.0, 3.0, "field", "Legitimacy")
        assert result.is_valid is True
        assert "meets threshold" in result.message

    def test_below_threshold(self):
        result = validate_score_threshold(2.5, 3.0, "field", "Desirability")
        assert result.is_valid is False
        assert "below threshold" in result.message
        assert "gap: 0.5" in result.message

    def test_exactly_at_threshold(self):
        result = validate_score_threshold(3.0, 3.0, "field")
        assert result.is_valid is True


class TestValidateListCount:
    """Tests for validate_list_count function."""

    def test_meets_minimum(self):
        result = validate_list_count([1, 2, 3], "items", min_count=2)
        assert result.is_valid is True
        assert "3 items" in result.message

    def test_below_minimum(self):
        result = validate_list_count([1], "items", min_count=3)
        assert result.is_valid is False
        assert "need at least 3" in result.message

    def test_within_range(self):
        result = validate_list_count([1, 2, 3], "items", min_count=2, max_count=5)
        assert result.is_valid is True

    def test_above_maximum(self):
        result = validate_list_count([1, 2, 3, 4, 5, 6], "items", min_count=1, max_count=3)
        assert result.is_valid is False

    def test_empty_list(self):
        result = validate_list_count([], "items", min_count=1)
        assert result.is_valid is False


# =============================================================================
# CONTENT VALIDATORS TESTS
# =============================================================================

class TestValidateNoEmDashes:
    """Tests for validate_no_em_dashes function."""

    def test_no_dashes(self):
        result = validate_no_em_dashes("normal text with regular hyphen-dash", "field")
        assert result.is_valid is True

    def test_with_em_dash(self):
        result = validate_no_em_dashes("text—with em dash", "field")
        assert result.is_valid is False

    def test_with_en_dash(self):
        result = validate_no_em_dashes("text–with en dash", "field")
        assert result.is_valid is False


class TestValidateSolutionNeutral:
    """Tests for validate_solution_neutral function."""

    def test_neutral_text(self):
        # Note: avoid words that contain solution keywords
        # e.g., "daily" contains "ai", "leading" contains "ai"
        result = validate_solution_neutral(
            "Users spend 4 hours each day on manual data entry, causing errors",
            "problem"
        )
        assert result.is_valid is True

    def test_with_solution_words(self):
        result = validate_solution_neutral(
            "Users need a better app to manage their tasks",
            "problem"
        )
        assert result.is_valid is False
        assert "app" in result.message

    def test_multiple_solution_words(self):
        result = validate_solution_neutral(
            "We need an AI platform with new technology",
            "problem"
        )
        assert result.is_valid is False
        assert len(result.details["found_words"]) >= 2


class TestValidateQuantification:
    """Tests for validate_quantification function."""

    def test_sufficient_numbers(self):
        result = validate_quantification(
            "Users report spending 4 hours (60% of their day) on this task",
            "field",
            min_numbers=2
        )
        assert result.is_valid is True

    def test_insufficient_numbers(self):
        result = validate_quantification(
            "Many users report spending time on this task",
            "field",
            min_numbers=2
        )
        assert result.is_valid is False

    def test_currency_values(self):
        result = validate_quantification(
            "Annual revenue of $5,000,000 with 25% growth",
            "field",
            min_numbers=2
        )
        assert result.is_valid is True

    def test_no_numbers(self):
        result = validate_quantification(
            "This is text without any numeric values",
            "field",
            min_numbers=1
        )
        assert result.is_valid is False


class TestValidateNoVagueTerms:
    """Tests for validate_no_vague_terms function."""

    def test_specific_text(self):
        result = validate_no_vague_terms(
            "We conducted 15 interviews with 3 enterprise clients",
            "field"
        )
        assert result.is_valid is True

    def test_vague_text(self):
        result = validate_no_vague_terms(
            "Many users have reported various significant problems",
            "field"
        )
        assert result.is_valid is False
        assert "many" in result.message.lower()

    def test_word_boundary(self):
        # "someone" contains "some" but shouldn't match
        result = validate_no_vague_terms(
            "Someone from the team confirmed this",
            "field"
        )
        assert result.is_valid is True


# =============================================================================
# STRUCTURE VALIDATORS TESTS
# =============================================================================

class TestValidateMarkdownStructure:
    """Tests for validate_markdown_structure function."""

    def test_all_sections_present(self, sample_markdown_document):
        report = validate_markdown_structure(
            sample_markdown_document,
            required_sections=["Section One", "Section Two"]
        )
        assert report.is_valid is True
        assert report.error_count == 0

    def test_missing_section(self, sample_markdown_document):
        report = validate_markdown_structure(
            sample_markdown_document,
            required_sections=["Section One", "Missing Section"]
        )
        assert report.is_valid is False
        assert report.error_count == 1

    def test_empty_required_sections(self, sample_markdown_document):
        report = validate_markdown_structure(
            sample_markdown_document,
            required_sections=[]
        )
        assert report.is_valid is True


class TestValidateTableStructure:
    """Tests for validate_table_structure function."""

    def test_all_columns_present(self, sample_markdown_document):
        report = validate_table_structure(
            sample_markdown_document,
            expected_columns=["Header 1", "Header 2"]
        )
        assert report.is_valid is True

    def test_missing_column(self, sample_markdown_document):
        report = validate_table_structure(
            sample_markdown_document,
            expected_columns=["Header 1", "Missing Column"]
        )
        assert report.is_valid is False

    def test_no_table(self):
        markdown = "# Just a heading\n\nNo table here."
        report = validate_table_structure(
            markdown,
            expected_columns=["Col1"]
        )
        assert report.is_valid is False
        assert "No table found" in str(report)


# =============================================================================
# CROSS-STEP VALIDATORS TESTS
# =============================================================================

class TestValidateStepDependencies:
    """Tests for validate_step_dependencies function."""

    def test_dependencies_met(self):
        report = validate_step_dependencies(
            "step_7",
            available_steps=["step_5", "step_6"]
        )
        assert report.is_valid is True

    def test_dependencies_not_met(self):
        report = validate_step_dependencies(
            "step_7",
            available_steps=["step_1", "step_2"]
        )
        assert report.is_valid is False

    def test_no_dependencies(self):
        report = validate_step_dependencies(
            "step_1",  # Step 1 has no dependencies
            available_steps=[]
        )
        assert report.is_valid is True


class TestValidateDataConsistency:
    """Tests for validate_data_consistency function."""

    def test_exact_match(self):
        source = ["Alice", "Bob", "Charlie"]
        target = ["Alice", "Bob", "Charlie"]
        report = validate_data_consistency(
            source, target, "Step5_Requesters", "Step7_Requesters"
        )
        assert report.is_valid is True
        assert "All 3 items match exactly" in str(report)

    def test_missing_in_target(self):
        source = ["Alice", "Bob", "Charlie"]
        target = ["Alice", "Bob"]
        report = validate_data_consistency(
            source, target, "Step5", "Step7"
        )
        assert report.is_valid is False
        assert "Charlie" in str(report)

    def test_extra_in_target(self):
        source = ["Alice", "Bob"]
        target = ["Alice", "Bob", "David"]
        report = validate_data_consistency(
            source, target, "Step5", "Step7"
        )
        # Extra items are warnings, not errors
        assert report.error_count == 0
        assert report.warning_count == 1

    def test_whitespace_handling(self):
        source = ["Alice ", " Bob"]
        target = ["Alice", "Bob"]
        report = validate_data_consistency(
            source, target, "Source", "Target"
        )
        assert report.is_valid is True


# =============================================================================
# DIMENSION VALIDATORS TESTS
# =============================================================================

class TestValidateDimensionScores:
    """Tests for validate_dimension_scores function."""

    def test_all_dimensions_valid(self, sample_dimension_scores):
        report = validate_dimension_scores(sample_dimension_scores)
        # All scores are in valid range and meet minimum thresholds
        assert report.error_count == 0

    def test_score_below_threshold(self):
        scores = {
            "legitimacy": 2.5,  # Below 3.0 threshold
            "desirability": 4.0,
            "acceptability": 3.5,
            "feasibility": 3.2,
            "viability": 3.0
        }
        report = validate_dimension_scores(scores)
        # Should have warning for legitimacy being below threshold
        assert report.warning_count >= 1

    def test_missing_dimension(self):
        scores = {
            "legitimacy": 4.0,
            "desirability": 4.0,
            # Missing other dimensions
        }
        report = validate_dimension_scores(scores)
        # Should have warnings for missing dimensions
        assert report.warning_count >= 3

    def test_empty_scores(self):
        report = validate_dimension_scores({})
        # All 5 dimensions should generate warnings
        assert report.warning_count == 5

    def test_score_outside_range(self):
        scores = {"legitimacy": 6.0}  # Above 5.0 max
        report = validate_dimension_scores(scores)
        assert report.error_count >= 1
