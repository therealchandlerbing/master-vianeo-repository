"""
VIANEO Framework Utilities
==========================

Shared utility functions for document generation, validation, and processing.
"""

import re
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, field

from .constants import CharacterLimits, ScoreThresholds, ValidationPatterns


# =============================================================================
# CHARACTER COUNTING & VALIDATION
# =============================================================================

def count_characters(text: str, include_spaces: bool = True) -> int:
    """
    Count characters in text.

    Args:
        text: Input text to count
        include_spaces: Whether to include spaces in count (default True)

    Returns:
        Character count
    """
    if not text:
        return 0
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def validate_character_limit(
    text: str,
    limit: int,
    field_name: str = "field"
) -> Tuple[bool, str]:
    """
    Validate text against character limit.

    Args:
        text: Text to validate
        limit: Maximum allowed characters
        field_name: Name of field for error message

    Returns:
        Tuple of (is_valid, message)
    """
    count = count_characters(text)
    if count <= limit:
        return True, f"{field_name}: {count}/{limit} characters (OK)"
    else:
        over = count - limit
        return False, f"{field_name}: {count}/{limit} characters (OVER by {over})"


def truncate_to_limit(text: str, limit: int, suffix: str = "...") -> str:
    """
    Truncate text to character limit with suffix.

    Args:
        text: Text to truncate
        limit: Maximum length including suffix
        suffix: Suffix to add when truncating

    Returns:
        Truncated text
    """
    if count_characters(text) <= limit:
        return text
    return text[:limit - len(suffix)].rstrip() + suffix


# =============================================================================
# TEXT CLEANING & FORMATTING
# =============================================================================

def clean_text(text: str) -> str:
    """
    Clean and normalize text.

    - Remove em dashes (replace with regular dashes)
    - Normalize whitespace
    - Strip leading/trailing whitespace
    """
    if not text:
        return ""

    # Replace em dash with regular dash
    text = text.replace("—", "-")
    text = text.replace("–", "-")

    # Normalize whitespace
    text = " ".join(text.split())

    return text.strip()


def remove_markdown_formatting(text: str) -> str:
    """Remove markdown formatting from text."""
    # Remove bold
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'__(.+?)__', r'\1', text)

    # Remove italic
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)

    # Remove inline code
    text = re.sub(r'`(.+?)`', r'\1', text)

    # Remove links
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)

    return text


def to_snake_case(text: str) -> str:
    """Convert text to snake_case."""
    # Replace spaces and hyphens with underscores
    text = re.sub(r'[\s\-]+', '_', text)
    # Handle camelCase
    text = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)
    return text.lower()


def to_title_case(text: str) -> str:
    """Convert text to Title Case, handling common words."""
    minor_words = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor',
                   'on', 'at', 'to', 'by', 'in', 'of', 'with'}

    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in minor_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return ' '.join(result)


# =============================================================================
# DATE HANDLING
# =============================================================================

def format_date(date: Optional[datetime] = None, format_str: str = "%Y-%m-%d") -> str:
    """
    Format date as string.

    Args:
        date: Date to format (defaults to today)
        format_str: strftime format string

    Returns:
        Formatted date string
    """
    if date is None:
        date = datetime.now()
    return date.strftime(format_str)


def parse_date(date_str: str) -> Optional[datetime]:
    """
    Parse date from various formats.

    Supports: YYYY-MM-DD, MM/DD/YYYY, DD-MM-YYYY
    """
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%B %d, %Y"]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def validate_date_format(date_str: str) -> Tuple[bool, str]:
    """
    Validate date is in ISO format (YYYY-MM-DD).

    Returns:
        Tuple of (is_valid, message)
    """
    if re.match(ValidationPatterns.ISO_DATE, date_str):
        return True, f"Date format valid: {date_str}"
    return False, f"Date must be YYYY-MM-DD format, got: {date_str}"


# =============================================================================
# SCORE HANDLING
# =============================================================================

def format_score(score: float) -> str:
    """Format score as X.X/5."""
    return f"{score:.1f}/5"


def parse_score(score_str: str) -> Optional[float]:
    """Parse score from X.X/5 format."""
    match = re.match(r'^(\d+\.?\d*)/5$', score_str)
    if match:
        return float(match.group(1))
    # Try parsing just a number
    try:
        return float(score_str)
    except ValueError:
        return None


def validate_score(score: float, dimension: str = "dimension") -> Tuple[bool, str]:
    """
    Validate score is within valid range.

    Returns:
        Tuple of (is_valid, message)
    """
    if 0 <= score <= 5:
        status = ScoreThresholds.get_status_keyword(score)
        return True, f"{dimension}: {format_score(score)} - {status}"
    return False, f"Score must be 0-5, got: {score}"


def calculate_weighted_score(scores: Dict[str, float]) -> float:
    """
    Calculate weighted overall score from dimension scores.

    Args:
        scores: Dict mapping dimension name to score

    Returns:
        Weighted average score
    """
    from .constants import VIANEO_DIMENSIONS

    total_weight = 0
    weighted_sum = 0

    for dim_key, dim_info in VIANEO_DIMENSIONS.items():
        if dim_key in scores:
            weighted_sum += scores[dim_key] * dim_info["weight"]
            total_weight += dim_info["weight"]

    if total_weight == 0:
        return 0.0

    return weighted_sum / total_weight


# =============================================================================
# FILE HANDLING
# =============================================================================

def ensure_directory(path: Union[str, Path]) -> Path:
    """Ensure directory exists, create if needed."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def safe_filename(name: str) -> str:
    """
    Convert name to safe filename.

    - Replace spaces with underscores
    - Remove special characters
    - Maintain capitalization
    """
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    # Remove special characters except underscores and hyphens
    name = re.sub(r'[^\w\-]', '', name)
    return name


def generate_filename(
    project_name: str,
    template: str,
    date: Optional[datetime] = None,
    **kwargs: str
) -> str:
    """
    Generate filename from template.

    Args:
        project_name: Project/company name
        template: Filename template with placeholders
        date: Date for filename (defaults to today)
        **kwargs: Additional template variables

    Returns:
        Generated filename string
    """
    if date is None:
        date = datetime.now()

    return template.format(
        project_name=safe_filename(project_name),
        company_name=safe_filename(project_name),
        date=format_date(date),
        **kwargs
    )


# =============================================================================
# DATA LOADING
# =============================================================================

def load_yaml(path: Union[str, Path]) -> Dict[str, Any]:
    """Load YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_json(path: Union[str, Path]) -> Dict[str, Any]:
    """Load JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_markdown(path: Union[str, Path]) -> str:
    """Load markdown file as string."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def load_data_file(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load data file based on extension (YAML or JSON).

    Args:
        path: Path to data file (.yaml, .yml, or .json)

    Returns:
        Parsed data dictionary

    Raises:
        ValueError: If file extension is not supported
        FileNotFoundError: If file does not exist
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    suffix = path.suffix.lower()
    if suffix in ['.yaml', '.yml']:
        return load_yaml(path)
    elif suffix == '.json':
        return load_json(path)
    else:
        raise ValueError(
            f"Unsupported file format: {path.suffix}. "
            f"Expected .yaml, .yml, or .json"
        )


def save_yaml(data: Dict[str, Any], path: Union[str, Path]) -> None:
    """Save data as YAML file."""
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def save_json(data: Dict[str, Any], path: Union[str, Path]) -> None:
    """Save data as JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# =============================================================================
# MARKDOWN PARSING
# =============================================================================

def extract_frontmatter(markdown: str) -> Tuple[Dict[str, Any], str]:
    """
    Extract YAML frontmatter from markdown.

    Returns:
        Tuple of (frontmatter_dict, remaining_markdown)
    """
    if not markdown.startswith('---'):
        return {}, markdown

    # Find end of frontmatter
    end_match = re.search(r'\n---\s*\n', markdown[3:])
    if not end_match:
        return {}, markdown

    frontmatter_str = markdown[3:end_match.start() + 3]
    remaining = markdown[end_match.end() + 3:]

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter or {}, remaining
    except yaml.YAMLError:
        return {}, markdown


def extract_sections(markdown: str) -> Dict[str, str]:
    """
    Extract sections from markdown by heading.

    Returns dict mapping heading text to section content.
    """
    sections = {}
    current_heading = None
    current_content = []

    for line in markdown.split('\n'):
        # Check for heading
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            # Save previous section
            if current_heading:
                sections[current_heading] = '\n'.join(current_content).strip()

            current_heading = match.group(2)
            current_content = []
        else:
            current_content.append(line)

    # Save last section
    if current_heading:
        sections[current_heading] = '\n'.join(current_content).strip()

    return sections


def extract_table(markdown: str) -> List[Dict[str, str]]:
    """
    Extract first markdown table as list of dicts.

    Returns:
        List of row dicts with column headers as keys
    """
    lines = markdown.split('\n')
    table_lines = []
    in_table = False

    for line in lines:
        if '|' in line and not line.strip().startswith('```'):
            in_table = True
            table_lines.append(line)
        elif in_table and not line.strip():
            break

    if len(table_lines) < 2:
        return []

    # Parse headers
    headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]

    # Skip separator line
    rows = []
    for line in table_lines[2:]:
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))

    return rows


# =============================================================================
# VALIDATION RESULT DATACLASS
# =============================================================================

@dataclass
class ValidationResult:
    """Result of a validation check."""

    is_valid: bool
    message: str
    field_name: str = ""
    severity: str = "error"  # error, warning, info
    details: Dict[str, Any] = field(default_factory=dict)

    # Alias for backwards compatibility
    @property
    def field(self) -> str:
        return self.field_name

    def __str__(self) -> str:
        prefix = {"error": "ERROR", "warning": "WARN", "info": "INFO"}
        return f"[{prefix.get(self.severity, 'INFO')}] {self.field_name}: {self.message}"


@dataclass
class ValidationReport:
    """Collection of validation results."""

    results: List[ValidationResult] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """Check if all validations passed (no errors)."""
        return all(r.is_valid or r.severity != "error" for r in self.results)

    @property
    def error_count(self) -> int:
        """Count of errors."""
        return sum(1 for r in self.results if not r.is_valid and r.severity == "error")

    @property
    def warning_count(self) -> int:
        """Count of warnings."""
        return sum(1 for r in self.results if r.severity == "warning")

    def add(self, result: ValidationResult) -> None:
        """Add a validation result."""
        self.results.append(result)

    def add_error(self, field: str, message: str, **details) -> None:
        """Add an error result."""
        self.add(ValidationResult(
            is_valid=False,
            field_name=field,
            message=message,
            severity="error",
            details=details
        ))

    def add_warning(self, field: str, message: str, **details) -> None:
        """Add a warning result."""
        self.add(ValidationResult(
            is_valid=True,
            field_name=field,
            message=message,
            severity="warning",
            details=details
        ))

    def add_success(self, field: str, message: str, **details) -> None:
        """Add a success result."""
        self.add(ValidationResult(
            is_valid=True,
            field_name=field,
            message=message,
            severity="info",
            details=details
        ))

    def __str__(self) -> str:
        lines = [
            f"Validation Report: {self.error_count} errors, {self.warning_count} warnings",
            "-" * 60
        ]
        for result in self.results:
            lines.append(str(result))
        return '\n'.join(lines)
