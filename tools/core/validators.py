"""
VIANEO Framework Base Validators
================================

Base validation functions used across all VIANEO tools.
"""

import re
from typing import List, Tuple, Optional, Dict, Any
from pathlib import Path

from .constants import (
    CharacterLimits,
    ScoreThresholds,
    ValidationPatterns,
    VIANEO_DIMENSIONS,
    STEP_DEPENDENCIES
)
from .utils import (
    count_characters,
    ValidationResult,
    ValidationReport,
    parse_score,
    extract_table,
    extract_sections
)


# =============================================================================
# BASE VALIDATORS
# =============================================================================

def validate_required_field(
    value: Any,
    field_name: str,
    allow_empty: bool = False
) -> ValidationResult:
    """Validate a required field is present and non-empty."""
    if value is None:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Required field is missing",
            severity="error"
        )

    if not allow_empty and isinstance(value, str) and not value.strip():
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Required field is empty",
            severity="error"
        )

    return ValidationResult(
        is_valid=True,
        field=field_name,
        message="Present and non-empty",
        severity="info"
    )


def validate_char_limit(
    text: str,
    limit: int,
    field_name: str
) -> ValidationResult:
    """Validate text is within character limit."""
    count = count_characters(text)

    if count <= limit:
        return ValidationResult(
            is_valid=True,
            field=field_name,
            message=f"{count}/{limit} characters",
            severity="info",
            details={"count": count, "limit": limit}
        )
    else:
        over = count - limit
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"{count}/{limit} characters (over by {over})",
            severity="error",
            details={"count": count, "limit": limit, "over": over}
        )


def validate_pattern(
    text: str,
    pattern: str,
    field_name: str,
    pattern_description: str = "expected format"
) -> ValidationResult:
    """Validate text matches regex pattern."""
    if re.match(pattern, text):
        return ValidationResult(
            is_valid=True,
            field=field_name,
            message=f"Matches {pattern_description}",
            severity="info"
        )
    else:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Does not match {pattern_description}",
            severity="error",
            details={"value": text, "expected_pattern": pattern}
        )


def validate_score_range(
    score: float,
    field_name: str,
    min_score: float = 0.0,
    max_score: float = 5.0
) -> ValidationResult:
    """Validate score is within range."""
    if min_score <= score <= max_score:
        status = ScoreThresholds.get_status_keyword(score)
        return ValidationResult(
            is_valid=True,
            field=field_name,
            message=f"{score:.1f}/5 - {status}",
            severity="info",
            details={"score": score, "status": status}
        )
    else:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Score {score} outside valid range ({min_score}-{max_score})",
            severity="error",
            details={"score": score, "min": min_score, "max": max_score}
        )


def validate_score_threshold(
    score: float,
    threshold: float,
    field_name: str,
    dimension: str = "dimension"
) -> ValidationResult:
    """Validate score meets minimum threshold."""
    if score >= threshold:
        return ValidationResult(
            is_valid=True,
            field=field_name,
            message=f"{dimension} score {score:.1f} meets threshold ({threshold})",
            severity="info"
        )
    else:
        gap = threshold - score
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"{dimension} score {score:.1f} below threshold ({threshold}, gap: {gap:.1f})",
            severity="warning",
            details={"score": score, "threshold": threshold, "gap": gap}
        )


def validate_list_count(
    items: List[Any],
    field_name: str,
    min_count: int = 1,
    max_count: Optional[int] = None
) -> ValidationResult:
    """Validate list has expected number of items."""
    count = len(items)

    if max_count is None:
        if count >= min_count:
            return ValidationResult(
                is_valid=True,
                field=field_name,
                message=f"{count} items (min: {min_count})",
                severity="info"
            )
        else:
            return ValidationResult(
                is_valid=False,
                field=field_name,
                message=f"Only {count} items (need at least {min_count})",
                severity="error"
            )
    else:
        if min_count <= count <= max_count:
            return ValidationResult(
                is_valid=True,
                field=field_name,
                message=f"{count} items (range: {min_count}-{max_count})",
                severity="info"
            )
        else:
            return ValidationResult(
                is_valid=False,
                field=field_name,
                message=f"{count} items outside range ({min_count}-{max_count})",
                severity="error"
            )


# =============================================================================
# CONTENT VALIDATORS
# =============================================================================

def validate_no_em_dashes(text: str, field_name: str) -> ValidationResult:
    """Validate text contains no em dashes."""
    if '—' in text or '–' in text:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message="Contains em dash or en dash (not allowed)",
            severity="error"
        )
    return ValidationResult(
        is_valid=True,
        field=field_name,
        message="No em/en dashes found",
        severity="info"
    )


def validate_solution_neutral(text: str, field_name: str) -> ValidationResult:
    """Validate problem statement is solution-neutral."""
    solution_words = [
        'app', 'platform', 'software', 'ai', 'tool', 'system',
        'solution', 'service', 'product', 'technology', 'algorithm'
    ]

    text_lower = text.lower()
    found_words = [w for w in solution_words if w in text_lower]

    if found_words:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Contains solution language: {', '.join(found_words)}",
            severity="error",
            details={"found_words": found_words}
        )

    return ValidationResult(
        is_valid=True,
        field=field_name,
        message="Solution-neutral language",
        severity="info"
    )


def validate_quantification(text: str, field_name: str, min_numbers: int = 2) -> ValidationResult:
    """Validate text contains quantified data."""
    # Find all numbers (including percentages, currency, etc.)
    numbers = re.findall(r'\d+(?:\.\d+)?%?|\$\d+(?:,\d{3})*(?:\.\d{2})?|\d+[KMB]?', text)

    if len(numbers) >= min_numbers:
        return ValidationResult(
            is_valid=True,
            field=field_name,
            message=f"Contains {len(numbers)} quantified values",
            severity="info",
            details={"numbers_found": numbers}
        )
    else:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Only {len(numbers)} numbers (need at least {min_numbers})",
            severity="error",
            details={"numbers_found": numbers, "required": min_numbers}
        )


def validate_no_vague_terms(text: str, field_name: str) -> ValidationResult:
    """Validate text doesn't use vague terms."""
    vague_terms = [
        'many', 'several', 'some', 'lots', 'various', 'numerous',
        'significant', 'considerable', 'substantial', 'good', 'great'
    ]

    text_lower = text.lower()
    found_terms = []

    for term in vague_terms:
        # Match whole words only
        if re.search(rf'\b{term}\b', text_lower):
            found_terms.append(term)

    if found_terms:
        return ValidationResult(
            is_valid=False,
            field=field_name,
            message=f"Contains vague terms: {', '.join(found_terms)}",
            severity="warning",
            details={"found_terms": found_terms}
        )

    return ValidationResult(
        is_valid=True,
        field=field_name,
        message="No vague terms found",
        severity="info"
    )


# =============================================================================
# STRUCTURE VALIDATORS
# =============================================================================

def validate_markdown_structure(
    markdown: str,
    required_sections: List[str],
    doc_name: str = "document"
) -> ValidationReport:
    """Validate markdown has required sections."""
    report = ValidationReport()
    sections = extract_sections(markdown)

    for section in required_sections:
        if section in sections:
            report.add_success(
                field=section,
                message="Section present"
            )
        else:
            report.add_error(
                field=section,
                message=f"Required section missing from {doc_name}"
            )

    return report


def validate_table_structure(
    markdown: str,
    expected_columns: List[str],
    table_name: str = "table"
) -> ValidationReport:
    """Validate table has expected columns."""
    report = ValidationReport()
    table = extract_table(markdown)

    if not table:
        report.add_error(
            field=table_name,
            message="No table found"
        )
        return report

    # Get actual columns from first row
    if table:
        actual_columns = list(table[0].keys())

        for col in expected_columns:
            if col in actual_columns:
                report.add_success(
                    field=f"{table_name}.{col}",
                    message="Column present"
                )
            else:
                report.add_error(
                    field=f"{table_name}.{col}",
                    message=f"Expected column '{col}' not found"
                )

    return report


# =============================================================================
# CROSS-STEP VALIDATORS
# =============================================================================

def validate_step_dependencies(
    step: str,
    available_steps: List[str]
) -> ValidationReport:
    """Validate required upstream steps are available."""
    report = ValidationReport()

    required = STEP_DEPENDENCIES.get(step, [])

    for req_step in required:
        if req_step in available_steps:
            report.add_success(
                field=f"dependency.{req_step}",
                message=f"Required step {req_step} available"
            )
        else:
            report.add_error(
                field=f"dependency.{req_step}",
                message=f"Required upstream step {req_step} not available"
            )

    return report


def validate_data_consistency(
    source_items: List[str],
    target_items: List[str],
    source_name: str,
    target_name: str
) -> ValidationReport:
    """Validate items match exactly between source and target."""
    report = ValidationReport()

    source_set = set(item.strip() for item in source_items)
    target_set = set(item.strip() for item in target_items)

    # Items in source but not in target
    missing_in_target = source_set - target_set
    for item in missing_in_target:
        report.add_error(
            field=f"{source_name}->{target_name}",
            message=f"'{item}' from {source_name} missing in {target_name}"
        )

    # Items in target but not in source
    extra_in_target = target_set - source_set
    for item in extra_in_target:
        report.add_warning(
            field=f"{target_name}",
            message=f"'{item}' in {target_name} not found in {source_name}"
        )

    if not missing_in_target and not extra_in_target:
        report.add_success(
            field=f"{source_name}->{target_name}",
            message=f"All {len(source_set)} items match exactly"
        )

    return report


# =============================================================================
# DIMENSION VALIDATORS
# =============================================================================

def validate_dimension_scores(scores: Dict[str, float]) -> ValidationReport:
    """Validate all VIANEO dimension scores."""
    report = ValidationReport()

    for dim_key, dim_info in VIANEO_DIMENSIONS.items():
        dim_name = dim_info["name"]
        min_score = dim_info["min_score"]

        if dim_key in scores:
            score = scores[dim_key]

            # Validate range
            range_result = validate_score_range(score, dim_name)
            report.add(range_result)

            # Validate threshold
            threshold_result = validate_score_threshold(
                score, min_score, dim_name, dim_name
            )
            report.add(threshold_result)
        else:
            report.add_warning(
                field=dim_name,
                message=f"Dimension score not provided"
            )

    return report
