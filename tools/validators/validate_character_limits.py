#!/usr/bin/env python3
"""
VIANEO Character Limit Validator
================================

Validates that all text fields in VIANEO outputs comply with character limits.

Character limits enforced:
- Needs statements: 60 characters
- Tasks/Pains/Expectations bullets: 60 characters
- Strategic notes: 250 characters
- Executive Brief sections: 150-300 characters

Usage:
    python validate_character_limits.py --input document.md
    python validate_character_limits.py --input data.yaml --type executive_brief
"""

import argparse
import json
import yaml
import re
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, field

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.constants import CharacterLimits
from core.utils import (
    count_characters,
    ValidationResult,
    ValidationReport,
    load_yaml,
    load_json,
    extract_sections,
    extract_table
)


# =============================================================================
# VALIDATOR CLASS
# =============================================================================

class CharacterLimitValidator:
    """Validator for VIANEO character limits."""

    # Define limits by context
    LIMITS = {
        # Executive Brief sections
        'b1_combined': CharacterLimits.B1_PROJECT_NAME_TAGLINE,
        'b2_problem': CharacterLimits.B2_PROBLEM_STATEMENT,
        'b3_solution': CharacterLimits.B3_SOLUTION_OVERVIEW,
        'b4_market': CharacterLimits.B4_MARKET_DESCRIPTION,
        'b5_revenue': CharacterLimits.B5_REVENUE_MODEL,
        'b6_traction': CharacterLimits.B6_TRACTION_STATUS,
        'b7_team': CharacterLimits.B7_TEAM_OVERVIEW,

        # Needs and Activities
        'need_statement': CharacterLimits.NEED_STATEMENT,
        'task': CharacterLimits.PERSONA_TASK,
        'pain': CharacterLimits.PERSONA_PAIN,
        'expectation': CharacterLimits.PERSONA_EXPECTATION,
        'means': CharacterLimits.MEANS_STATEMENT,

        # Notes
        'note': CharacterLimits.NOTES_FIELD,
        'strategic_note': CharacterLimits.STRATEGIC_NOTE,

        # Value Network
        'organization_name': CharacterLimits.ORGANIZATION_NAME,
        'role_description': CharacterLimits.ROLE_DESCRIPTION,
    }

    def __init__(self):
        self.report = ValidationReport()

    def validate_text(
        self,
        text: str,
        limit_type: str,
        field_name: str
    ) -> ValidationResult:
        """
        Validate a single text field against its character limit.

        Args:
            text: Text to validate
            limit_type: Type of limit to apply (key from LIMITS)
            field_name: Name of field for error messages

        Returns:
            ValidationResult
        """
        limit = self.LIMITS.get(limit_type)
        if limit is None:
            return ValidationResult(
                is_valid=True,
                field=field_name,
                message=f"Unknown limit type: {limit_type}",
                severity="warning"
            )

        count = count_characters(text)

        if count <= limit:
            result = ValidationResult(
                is_valid=True,
                field=field_name,
                message=f"{count}/{limit} characters (OK)",
                severity="info",
                details={"count": count, "limit": limit}
            )
        else:
            over = count - limit
            result = ValidationResult(
                is_valid=False,
                field=field_name,
                message=f"{count}/{limit} characters (OVER by {over})",
                severity="error",
                details={"count": count, "limit": limit, "over": over, "text": text[:100] + "..."}
            )

        self.report.add(result)
        return result

    def validate_list(
        self,
        items: List[str],
        limit_type: str,
        list_name: str
    ) -> List[ValidationResult]:
        """
        Validate a list of text items.

        Args:
            items: List of text items
            limit_type: Type of limit to apply
            list_name: Name of list for error messages

        Returns:
            List of ValidationResults
        """
        results = []
        for i, item in enumerate(items):
            field_name = f"{list_name}[{i}]"
            result = self.validate_text(item, limit_type, field_name)
            results.append(result)
        return results

    def validate_executive_brief(self, data: Dict[str, Any]) -> ValidationReport:
        """
        Validate all character limits in an Executive Brief.

        Args:
            data: Executive Brief data dictionary

        Returns:
            ValidationReport with all results
        """
        # B1: Project Name + Tagline (combined)
        project_name = data.get('project_name', '')
        tagline = data.get('tagline', '')
        combined = f"{project_name}: {tagline}" if tagline else project_name
        self.validate_text(combined, 'b1_combined', 'B1: Name + Tagline')

        # B2: Problem Statement
        problem = data.get('problem_description', '')
        self.validate_text(problem, 'b2_problem', 'B2: Problem Description')

        # B3: Solution Overview
        solution = data.get('solution_description', '')
        self.validate_text(solution, 'b3_solution', 'B3: Solution Description')

        # B4: Market Description
        market = data.get('market_description', '')
        self.validate_text(market, 'b4_market', 'B4: Market Description')

        # B5: Revenue Model
        revenue = data.get('revenue_description', '')
        self.validate_text(revenue, 'b5_revenue', 'B5: Revenue Description')

        # B6: Traction Status
        traction = data.get('status_description', '')
        self.validate_text(traction, 'b6_traction', 'B6: Status Description')

        # B7: Team Overview
        team = data.get('team_overview', '')
        self.validate_text(team, 'b7_team', 'B7: Team Overview')

        return self.report

    def validate_personas(self, data: Dict[str, Any]) -> ValidationReport:
        """
        Validate character limits in persona document.

        Args:
            data: Persona document data dictionary

        Returns:
            ValidationReport with all results
        """
        personas = data.get('personas', [])

        for i, persona in enumerate(personas):
            name = persona.get('first_name', f'Persona {i+1}')

            # Tasks
            tasks = persona.get('tasks', [])
            self.validate_list(tasks, 'task', f'{name}.tasks')

            # Pains
            pains = persona.get('pains', [])
            self.validate_list(pains, 'pain', f'{name}.pains')

            # Expectations
            expectations = persona.get('expectations', [])
            self.validate_list(expectations, 'expectation', f'{name}.expectations')

        return self.report

    def validate_value_network(self, data: Dict[str, Any]) -> ValidationReport:
        """
        Validate character limits in value network document.

        Args:
            data: Value network data dictionary

        Returns:
            ValidationReport with all results
        """
        sections = [
            'enablers_influencers',
            'products_solutions',
            'channels_partners',
            'buyers',
            'end_users'
        ]

        for section in sections:
            orgs = data.get(section, [])
            for i, org in enumerate(orgs):
                # Organization name
                name = org.get('name', f'Org {i+1}')
                self.validate_text(name, 'organization_name', f'{section}[{i}].name')

                # Role/Description
                role = org.get('role', '')
                self.validate_text(role, 'role_description', f'{section}[{i}].role')

                # Notes
                notes = org.get('notes', '')
                self.validate_text(notes, 'strategic_note', f'{section}[{i}].notes')

        return self.report

    def validate_needs_matrix(self, data: Dict[str, Any]) -> ValidationReport:
        """
        Validate character limits in needs qualification matrix.

        Args:
            data: Needs matrix data dictionary

        Returns:
            ValidationReport with all results
        """
        # Validate need statements
        needs = data.get('needs', [])
        for i, need in enumerate(needs):
            statement = need.get('statement', '') if isinstance(need, dict) else need
            self.validate_text(statement, 'need_statement', f'Need[{i}]')

        return self.report

    def validate_markdown(self, markdown: str, doc_type: str = 'generic') -> ValidationReport:
        """
        Validate character limits in markdown document.

        Args:
            markdown: Markdown content
            doc_type: Type of document ('executive_brief', 'persona', 'value_network')

        Returns:
            ValidationReport with all results
        """
        if doc_type == 'executive_brief':
            return self._validate_executive_brief_markdown(markdown)
        elif doc_type == 'value_network':
            return self._validate_value_network_markdown(markdown)
        else:
            return self._validate_generic_markdown(markdown)

    def _validate_executive_brief_markdown(self, markdown: str) -> ValidationReport:
        """Validate Executive Brief markdown."""
        sections = extract_sections(markdown)

        # Map section names to limit types
        section_limits = {
            'Section B1: Project Name and Tagline': 'b1_combined',
            'Section B2: Problem Statement': 'b2_problem',
            'Section B3: Solution Overview': 'b3_solution',
            'Section B4: Market and Users': 'b4_market',
            'Section B5: Business Model': 'b5_revenue',
            'Section B6: Traction and Validation': 'b6_traction',
            'Section B7: Team': 'b7_team',
        }

        for section_name, limit_type in section_limits.items():
            if section_name in sections:
                content = sections[section_name]
                # Extract the description field
                match = re.search(r'\*\*[^*]+:\*\*\s*\n([^\n]+)', content)
                if match:
                    text = match.group(1).strip()
                    self.validate_text(text, limit_type, section_name)

        return self.report

    def _validate_value_network_markdown(self, markdown: str) -> ValidationReport:
        """Validate Value Network markdown."""
        # Extract tables and validate organization names and notes
        tables = re.findall(r'\|[^\n]+\|(?:\n\|[^\n]+\|)+', markdown)

        for table in tables:
            rows = extract_table(table)
            for i, row in enumerate(rows):
                if 'Organization Name' in row:
                    name = row.get('Organization Name', '')
                    self.validate_text(name, 'organization_name', f'Row[{i}].name')

                if 'Notes' in row:
                    notes = row.get('Notes', '')
                    self.validate_text(notes, 'strategic_note', f'Row[{i}].notes')

        return self.report

    def _validate_generic_markdown(self, markdown: str) -> ValidationReport:
        """Validate generic markdown for bullet points."""
        # Extract bullet points
        bullets = re.findall(r'^[-*]\s+(.+)$', markdown, re.MULTILINE)

        for i, bullet in enumerate(bullets):
            # Check if it might be a need/task/pain
            count = count_characters(bullet)
            if count > CharacterLimits.NEED_BULLET:
                self.report.add_warning(
                    field=f'Bullet[{i}]',
                    message=f"{count} characters may exceed 60-char limit for needs/tasks",
                    count=count
                )

        return self.report

    def get_summary(self) -> str:
        """Get summary of validation results."""
        return str(self.report)


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def validate_character_limits(
    input_path: Optional[Path] = None,
    data: Optional[Dict[str, Any]] = None,
    doc_type: str = 'auto'
) -> ValidationReport:
    """
    Validate character limits in VIANEO document.

    Args:
        input_path: Path to input file (YAML, JSON, or MD)
        data: Data dictionary (alternative to input_path)
        doc_type: Document type ('executive_brief', 'persona', 'value_network', 'needs', 'auto')

    Returns:
        ValidationReport with all results
    """
    validator = CharacterLimitValidator()

    # Load data if path provided
    if data is None and input_path is not None:
        input_path = Path(input_path)

        if input_path.suffix in ['.yaml', '.yml']:
            data = load_yaml(input_path)
            # Auto-detect type from data keys
            if doc_type == 'auto':
                if 'problem_description' in data:
                    doc_type = 'executive_brief'
                elif 'personas' in data:
                    doc_type = 'persona'
                elif 'enablers_influencers' in data:
                    doc_type = 'value_network'
                else:
                    doc_type = 'generic'

        elif input_path.suffix == '.json':
            data = load_json(input_path)

        elif input_path.suffix == '.md':
            with open(input_path, 'r', encoding='utf-8') as f:
                markdown = f.read()
            return validator.validate_markdown(markdown, doc_type)

        else:
            raise ValueError(f"Unsupported file type: {input_path.suffix}")

    # Validate based on document type
    if doc_type == 'executive_brief':
        return validator.validate_executive_brief(data)
    elif doc_type == 'persona':
        return validator.validate_personas(data)
    elif doc_type == 'value_network':
        return validator.validate_value_network(data)
    elif doc_type == 'needs':
        return validator.validate_needs_matrix(data)
    else:
        # Generic validation
        return validator.report


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Validate VIANEO character limits"
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input file to validate (YAML, JSON, or MD)'
    )
    parser.add_argument(
        '--type', '-t',
        choices=['executive_brief', 'persona', 'value_network', 'needs', 'auto'],
        default='auto',
        help='Document type (default: auto-detect)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show all results, not just errors'
    )

    args = parser.parse_args()

    # Run validation
    report = validate_character_limits(
        input_path=args.input,
        doc_type=args.type
    )

    # Print results
    print("\n" + "=" * 60)
    print("VIANEO Character Limit Validation Report")
    print("=" * 60)
    print(f"\nFile: {args.input}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print("-" * 60)

    for result in report.results:
        if args.verbose or not result.is_valid or result.severity == 'warning':
            print(result)

    print("-" * 60)
    if report.is_valid:
        print("PASSED: All character limits valid")
    else:
        print(f"FAILED: {report.error_count} character limit violation(s)")

    return 0 if report.is_valid else 1


if __name__ == '__main__':
    exit(main())
