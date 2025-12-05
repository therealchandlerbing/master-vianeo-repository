"""
Tests for core/utils.py utility functions.
"""

import pytest
from pathlib import Path
from datetime import datetime
import tempfile
import json
import yaml

from core.utils import (
    # Character counting
    count_characters,
    validate_character_limit,
    truncate_to_limit,
    # Text cleaning
    clean_text,
    remove_markdown_formatting,
    to_snake_case,
    to_title_case,
    # Date handling
    format_date,
    parse_date,
    validate_date_format,
    # Score handling
    format_score,
    parse_score,
    validate_score,
    calculate_weighted_score,
    # File handling
    safe_filename,
    generate_filename,
    ensure_directory,
    # Data loading
    load_yaml,
    load_json,
    load_markdown,
    load_data_file,
    save_yaml,
    save_json,
    # Markdown parsing
    extract_frontmatter,
    extract_sections,
    extract_table,
    # Validation classes
    ValidationResult,
    ValidationReport,
)


# =============================================================================
# CHARACTER COUNTING TESTS
# =============================================================================

class TestCountCharacters:
    """Tests for count_characters function."""

    def test_count_with_spaces(self):
        assert count_characters("hello world") == 11

    def test_count_without_spaces(self):
        assert count_characters("hello world", include_spaces=False) == 10

    def test_empty_string(self):
        assert count_characters("") == 0

    def test_none_returns_zero(self):
        assert count_characters(None) == 0

    def test_unicode_characters(self):
        assert count_characters("hello 世界") == 8


class TestValidateCharacterLimit:
    """Tests for validate_character_limit function."""

    def test_within_limit(self):
        is_valid, message = validate_character_limit("short", 100, "field")
        assert is_valid is True
        assert "5/100" in message
        assert "OK" in message

    def test_at_limit(self):
        is_valid, message = validate_character_limit("12345", 5, "field")
        assert is_valid is True

    def test_over_limit(self):
        is_valid, message = validate_character_limit("too long text", 5, "field")
        assert is_valid is False
        assert "OVER" in message

    def test_over_by_count(self):
        is_valid, message = validate_character_limit("1234567", 5, "field")
        assert "OVER by 2" in message


class TestTruncateToLimit:
    """Tests for truncate_to_limit function."""

    def test_no_truncation_needed(self):
        assert truncate_to_limit("short", 10) == "short"

    def test_truncation_with_default_suffix(self):
        result = truncate_to_limit("this is a long text", 10)
        assert len(result) == 10
        assert result.endswith("...")

    def test_truncation_with_custom_suffix(self):
        result = truncate_to_limit("long text here", 10, suffix="…")
        assert result.endswith("…")

    def test_exact_limit(self):
        assert truncate_to_limit("12345", 5) == "12345"


# =============================================================================
# TEXT CLEANING TESTS
# =============================================================================

class TestCleanText:
    """Tests for clean_text function."""

    def test_em_dash_replacement(self):
        assert clean_text("hello—world") == "hello-world"

    def test_en_dash_replacement(self):
        assert clean_text("hello–world") == "hello-world"

    def test_whitespace_normalization(self):
        assert clean_text("hello   world") == "hello world"

    def test_strip_whitespace(self):
        assert clean_text("  hello  ") == "hello"

    def test_empty_string(self):
        assert clean_text("") == ""

    def test_none_returns_empty(self):
        assert clean_text(None) == ""

    def test_combined_cleaning(self, text_with_special_chars):
        result = clean_text(text_with_special_chars)
        assert "—" not in result
        assert "–" not in result
        assert "   " not in result


class TestRemoveMarkdownFormatting:
    """Tests for remove_markdown_formatting function."""

    def test_remove_bold(self):
        assert remove_markdown_formatting("**bold**") == "bold"
        assert remove_markdown_formatting("__bold__") == "bold"

    def test_remove_italic(self):
        assert remove_markdown_formatting("*italic*") == "italic"
        assert remove_markdown_formatting("_italic_") == "italic"

    def test_remove_code(self):
        assert remove_markdown_formatting("`code`") == "code"

    def test_remove_links(self):
        result = remove_markdown_formatting("[link](http://example.com)")
        assert result == "link"

    def test_mixed_formatting(self, markdown_with_formatting):
        result = remove_markdown_formatting(markdown_with_formatting)
        assert "**" not in result
        assert "*" not in result
        assert "`" not in result
        assert "[" not in result


class TestToSnakeCase:
    """Tests for to_snake_case function."""

    def test_spaces_to_underscores(self):
        assert to_snake_case("hello world") == "hello_world"

    def test_hyphens_to_underscores(self):
        assert to_snake_case("hello-world") == "hello_world"

    def test_camel_case(self):
        assert to_snake_case("helloWorld") == "hello_world"

    def test_already_snake_case(self):
        assert to_snake_case("hello_world") == "hello_world"

    def test_uppercase(self):
        assert to_snake_case("HELLO WORLD") == "hello_world"


class TestToTitleCase:
    """Tests for to_title_case function."""

    def test_basic_title_case(self):
        assert to_title_case("hello world") == "Hello World"

    def test_minor_words(self):
        assert to_title_case("the quick and the fox") == "The Quick and the Fox"

    def test_first_word_always_capitalized(self):
        assert to_title_case("the beginning") == "The Beginning"


# =============================================================================
# DATE HANDLING TESTS
# =============================================================================

class TestFormatDate:
    """Tests for format_date function."""

    def test_default_format(self, fixed_date):
        result = format_date(fixed_date)
        assert result == "2025-01-15"

    def test_custom_format(self, fixed_date):
        result = format_date(fixed_date, "%B %d, %Y")
        assert result == "January 15, 2025"

    def test_none_uses_today(self):
        result = format_date(None)
        assert len(result) == 10  # YYYY-MM-DD format


class TestParseDate:
    """Tests for parse_date function."""

    def test_iso_format(self):
        result = parse_date("2025-01-15")
        assert result.year == 2025
        assert result.month == 1
        assert result.day == 15

    def test_us_format(self):
        result = parse_date("01/15/2025")
        assert result.month == 1
        assert result.day == 15

    def test_invalid_format(self):
        assert parse_date("invalid") is None

    def test_long_format(self):
        result = parse_date("January 15, 2025")
        assert result.month == 1


class TestValidateDateFormat:
    """Tests for validate_date_format function."""

    def test_valid_iso_format(self):
        is_valid, message = validate_date_format("2025-01-15")
        assert is_valid is True

    def test_invalid_format(self):
        is_valid, message = validate_date_format("01/15/2025")
        assert is_valid is False
        assert "YYYY-MM-DD" in message


# =============================================================================
# SCORE HANDLING TESTS
# =============================================================================

class TestFormatScore:
    """Tests for format_score function."""

    def test_integer_score(self):
        assert format_score(4.0) == "4.0/5"

    def test_decimal_score(self):
        assert format_score(3.5) == "3.5/5"

    def test_zero_score(self):
        assert format_score(0.0) == "0.0/5"


class TestParseScore:
    """Tests for parse_score function."""

    def test_standard_format(self):
        assert parse_score("4.0/5") == 4.0

    def test_integer_format(self):
        assert parse_score("4/5") == 4.0

    def test_plain_number(self):
        assert parse_score("3.5") == 3.5

    def test_invalid_format(self):
        assert parse_score("invalid") is None


class TestValidateScore:
    """Tests for validate_score function."""

    def test_valid_score(self):
        is_valid, message = validate_score(4.0, "test")
        assert is_valid is True
        assert "4.0/5" in message

    def test_score_below_range(self):
        is_valid, message = validate_score(-1.0, "test")
        assert is_valid is False

    def test_score_above_range(self):
        is_valid, message = validate_score(6.0, "test")
        assert is_valid is False

    def test_boundary_scores(self):
        assert validate_score(0.0, "test")[0] is True
        assert validate_score(5.0, "test")[0] is True


class TestCalculateWeightedScore:
    """Tests for calculate_weighted_score function."""

    def test_all_dimensions(self, sample_dimension_scores):
        result = calculate_weighted_score(sample_dimension_scores)
        assert 3.0 <= result <= 4.0  # Should be weighted average

    def test_partial_dimensions(self):
        scores = {"legitimacy": 4.0, "desirability": 3.0}
        result = calculate_weighted_score(scores)
        assert result > 0

    def test_empty_scores(self):
        assert calculate_weighted_score({}) == 0.0


# =============================================================================
# FILE HANDLING TESTS
# =============================================================================

class TestSafeFilename:
    """Tests for safe_filename function."""

    def test_spaces_to_underscores(self):
        assert safe_filename("hello world") == "hello_world"

    def test_remove_special_chars(self):
        assert safe_filename("file<>name") == "filename"

    def test_preserve_hyphens(self):
        assert safe_filename("hello-world") == "hello-world"

    def test_preserve_underscores(self):
        assert safe_filename("hello_world") == "hello_world"


class TestGenerateFilename:
    """Tests for generate_filename function."""

    def test_basic_template(self, fixed_date):
        template = "{project_name}_{date}.docx"
        result = generate_filename("Test Project", template, fixed_date)
        assert result == "Test_Project_2025-01-15.docx"

    def test_company_name_alias(self, fixed_date):
        template = "{company_name}_report.pdf"
        result = generate_filename("My Company", template, fixed_date)
        assert result == "My_Company_report.pdf"


class TestEnsureDirectory:
    """Tests for ensure_directory function."""

    def test_create_new_directory(self, tmp_path):
        new_dir = tmp_path / "new" / "nested" / "dir"
        result = ensure_directory(new_dir)
        assert result.exists()
        assert result.is_dir()

    def test_existing_directory(self, tmp_path):
        result = ensure_directory(tmp_path)
        assert result == tmp_path


# =============================================================================
# DATA LOADING TESTS
# =============================================================================

class TestLoadYaml:
    """Tests for load_yaml function."""

    def test_load_valid_yaml(self, tmp_path):
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text("key: value\nlist:\n  - item1\n  - item2")

        result = load_yaml(yaml_file)
        assert result["key"] == "value"
        assert result["list"] == ["item1", "item2"]


class TestLoadJson:
    """Tests for load_json function."""

    def test_load_valid_json(self, tmp_path):
        json_file = tmp_path / "test.json"
        json_file.write_text('{"key": "value", "number": 42}')

        result = load_json(json_file)
        assert result["key"] == "value"
        assert result["number"] == 42


class TestLoadDataFile:
    """Tests for load_data_file function."""

    def test_load_yaml_file(self, tmp_path):
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text("name: test")

        result = load_data_file(yaml_file)
        assert result["name"] == "test"

    def test_load_yml_file(self, tmp_path):
        yml_file = tmp_path / "test.yml"
        yml_file.write_text("name: test")

        result = load_data_file(yml_file)
        assert result["name"] == "test"

    def test_load_json_file(self, tmp_path):
        json_file = tmp_path / "test.json"
        json_file.write_text('{"name": "test"}')

        result = load_data_file(json_file)
        assert result["name"] == "test"

    def test_case_insensitive_extension(self, tmp_path):
        yaml_file = tmp_path / "test.YAML"
        yaml_file.write_text("name: test")

        result = load_data_file(yaml_file)
        assert result["name"] == "test"

    def test_unsupported_format(self, tmp_path):
        txt_file = tmp_path / "test.txt"
        txt_file.write_text("some text")

        with pytest.raises(ValueError, match="Unsupported file format"):
            load_data_file(txt_file)

    def test_file_not_found(self, tmp_path):
        missing_file = tmp_path / "missing.yaml"

        with pytest.raises(FileNotFoundError):
            load_data_file(missing_file)


class TestSaveYaml:
    """Tests for save_yaml function."""

    def test_save_and_reload(self, tmp_path):
        yaml_file = tmp_path / "output.yaml"
        data = {"key": "value", "list": [1, 2, 3]}

        save_yaml(data, yaml_file)
        reloaded = load_yaml(yaml_file)

        assert reloaded == data


class TestSaveJson:
    """Tests for save_json function."""

    def test_save_and_reload(self, tmp_path):
        json_file = tmp_path / "output.json"
        data = {"key": "value", "number": 42}

        save_json(data, json_file)
        reloaded = load_json(json_file)

        assert reloaded == data


# =============================================================================
# MARKDOWN PARSING TESTS
# =============================================================================

class TestExtractFrontmatter:
    """Tests for extract_frontmatter function."""

    def test_valid_frontmatter(self, sample_markdown_document):
        frontmatter, content = extract_frontmatter(sample_markdown_document)
        assert frontmatter["title"] == "Test Document"
        # YAML may parse dates as datetime.date objects
        assert str(frontmatter["date"]) == "2025-01-15"
        assert "# Section One" in content

    def test_no_frontmatter(self):
        markdown = "# Just a heading\n\nSome content."
        frontmatter, content = extract_frontmatter(markdown)
        assert frontmatter == {}
        assert content == markdown


class TestExtractSections:
    """Tests for extract_sections function."""

    def test_extract_headings(self, sample_markdown_document):
        sections = extract_sections(sample_markdown_document)
        assert "Section One" in sections
        assert "Section Two" in sections

    def test_section_content(self, sample_markdown_document):
        sections = extract_sections(sample_markdown_document)
        assert "first section content" in sections["Section One"]


class TestExtractTable:
    """Tests for extract_table function."""

    def test_extract_simple_table(self, sample_markdown_document):
        rows = extract_table(sample_markdown_document)
        assert len(rows) == 2
        assert rows[0]["Header 1"] == "Cell 1"
        assert rows[1]["Header 2"] == "Cell 4"

    def test_no_table(self):
        markdown = "# Just a heading\n\nNo table here."
        rows = extract_table(markdown)
        assert rows == []


# =============================================================================
# VALIDATION CLASSES TESTS
# =============================================================================

class TestValidationResult:
    """Tests for ValidationResult dataclass."""

    def test_create_result(self):
        result = ValidationResult(
            is_valid=True,
            message="All good",
            field_name="test_field",
            severity="info"
        )
        assert result.is_valid is True
        assert result.field == "test_field"  # Test backwards-compatible property
        assert result.field_name == "test_field"

    def test_string_representation(self):
        result = ValidationResult(
            is_valid=False,
            message="Error occurred",
            field_name="my_field",
            severity="error"
        )
        str_repr = str(result)
        assert "ERROR" in str_repr
        assert "my_field" in str_repr


class TestValidationReport:
    """Tests for ValidationReport dataclass."""

    def test_empty_report_is_valid(self):
        report = ValidationReport()
        assert report.is_valid is True
        assert report.error_count == 0

    def test_add_error(self):
        report = ValidationReport()
        report.add_error("field", "Something went wrong")

        assert report.is_valid is False
        assert report.error_count == 1

    def test_add_warning(self):
        report = ValidationReport()
        report.add_warning("field", "Minor issue")

        assert report.is_valid is True  # Warnings don't invalidate
        assert report.warning_count == 1

    def test_add_success(self):
        report = ValidationReport()
        report.add_success("field", "All good")

        assert report.is_valid is True
        assert len(report.results) == 1

    def test_mixed_results(self):
        report = ValidationReport()
        report.add_success("field1", "OK")
        report.add_warning("field2", "Warning")
        report.add_error("field3", "Error")

        assert report.is_valid is False
        assert report.error_count == 1
        assert report.warning_count == 1

    def test_string_representation(self):
        report = ValidationReport()
        report.add_error("field", "Error message")

        str_repr = str(report)
        assert "1 errors" in str_repr
        assert "0 warnings" in str_repr
