#!/usr/bin/env python3
"""
VIANEO Evidence Validator
=========================

Validates evidence citations and confidence levels in VIANEO documents.

Validates:
- Evidence ID format (E001, E002, etc.)
- Quality rating scale (1-5)
- Required evidence for each section
- L1/L2/L3 confidence level assignments

Usage:
    python validate_evidence.py --input executive_brief.yaml
"""

import argparse
import re
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from enum import Enum

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.constants import EvidenceQuality, ValidationPatterns
from core.utils import ValidationResult, ValidationReport, load_yaml


# =============================================================================
# EVIDENCE DEFINITIONS
# =============================================================================

class ConfidenceLevel(Enum):
    """Evidence confidence levels."""
    L1 = "L1"  # Direct evidence (interviews, contracts, metrics)
    L2 = "L2"  # Indirect evidence (market reports, benchmarks)
    L3 = "L3"  # Inferred (assumptions, projections)


@dataclass
class EvidenceRequirement:
    """Evidence requirement for a section."""
    section: str
    min_count: int
    min_quality: int
    preferred_types: List[str]
    description: str


# Evidence requirements by section
EVIDENCE_REQUIREMENTS = {
    'B1': EvidenceRequirement(
        section='B1',
        min_count=0,
        min_quality=3,
        preferred_types=['trademark', 'domain', 'brand_assets'],
        description='Project name - trademark/brand documentation'
    ),
    'B2': EvidenceRequirement(
        section='B2',
        min_count=2,
        min_quality=4,
        preferred_types=['customer_interviews', 'market_research', 'industry_reports'],
        description='Problem statement - customer validation required'
    ),
    'B3': EvidenceRequirement(
        section='B3',
        min_count=1,
        min_quality=3,
        preferred_types=['prototype', 'demo', 'technical_spec'],
        description='Solution - prototype or specification'
    ),
    'B4': EvidenceRequirement(
        section='B4',
        min_count=2,
        min_quality=4,
        preferred_types=['industry_reports', 'government_stats', 'bottom_up_calc'],
        description='Market - third-party validation of size'
    ),
    'B5': EvidenceRequirement(
        section='B5',
        min_count=1,
        min_quality=3,
        preferred_types=['pricing_interviews', 'competitive_analysis', 'unit_economics'],
        description='Business model - pricing validation'
    ),
    'B6': EvidenceRequirement(
        section='B6',
        min_count=3,
        min_quality=4,
        preferred_types=['analytics', 'contracts', 'testimonials', 'financials'],
        description='Traction - verified metrics and commitments'
    ),
    'B7': EvidenceRequirement(
        section='B7',
        min_count=1,
        min_quality=4,
        preferred_types=['linkedin', 'publications', 'company_records'],
        description='Team - publicly verifiable credentials'
    ),
}


# =============================================================================
# VALIDATOR CLASS
# =============================================================================

class EvidenceValidator:
    """Validator for VIANEO evidence citations."""

    def __init__(self):
        self.report = ValidationReport()

    def validate_evidence_id(self, evidence_id: str) -> ValidationResult:
        """Validate evidence ID format."""
        pattern = r'^E\d{3}$'

        if re.match(pattern, evidence_id):
            return ValidationResult(
                is_valid=True,
                field=evidence_id,
                message="Valid evidence ID format",
                severity="info"
            )
        else:
            return ValidationResult(
                is_valid=False,
                field=evidence_id,
                message=f"Invalid format. Expected EXXX (e.g., E001)",
                severity="error"
            )

    def validate_quality_rating(
        self,
        rating: int,
        evidence_id: str
    ) -> ValidationResult:
        """Validate quality rating is within scale."""
        if 1 <= rating <= 5:
            quality = EvidenceQuality(rating)
            return ValidationResult(
                is_valid=True,
                field=f"{evidence_id}.quality",
                message=f"Rating {rating}: {quality.description}",
                severity="info"
            )
        else:
            return ValidationResult(
                is_valid=False,
                field=f"{evidence_id}.quality",
                message=f"Rating {rating} outside valid range (1-5)",
                severity="error"
            )

    def validate_evidence_entry(self, entry: Dict[str, Any]) -> List[ValidationResult]:
        """Validate a single evidence entry."""
        results = []

        # Check required fields
        required_fields = ['id', 'section', 'source_type', 'quality_rating']
        for field_name in required_fields:
            if field_name not in entry:
                results.append(ValidationResult(
                    is_valid=False,
                    field=f"evidence.{field_name}",
                    message=f"Missing required field: {field_name}",
                    severity="error"
                ))

        # Validate ID format
        if 'id' in entry:
            result = self.validate_evidence_id(entry['id'])
            results.append(result)
            self.report.add(result)

        # Validate quality rating
        if 'quality_rating' in entry:
            result = self.validate_quality_rating(
                entry['quality_rating'],
                entry.get('id', 'unknown')
            )
            results.append(result)
            self.report.add(result)

        # Validate date format if present
        if 'date' in entry:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', entry['date']):
                result = ValidationResult(
                    is_valid=False,
                    field=f"{entry.get('id', 'unknown')}.date",
                    message=f"Invalid date format. Expected YYYY-MM-DD",
                    severity="warning"
                )
                results.append(result)
                self.report.add(result)

        return results

    def validate_evidence_log(self, evidence_log: List[Dict[str, Any]]) -> ValidationReport:
        """Validate complete evidence log."""
        if not evidence_log:
            self.report.add_warning(
                field="evidence_log",
                message="Evidence log is empty - all claims should be supported"
            )
            return self.report

        # Validate each entry
        for entry in evidence_log:
            self.validate_evidence_entry(entry)

        # Check for unique IDs
        ids = [e.get('id') for e in evidence_log if 'id' in e]
        if len(ids) != len(set(ids)):
            self.report.add_error(
                field="evidence_log",
                message="Duplicate evidence IDs found"
            )

        # Check minimum count
        if len(evidence_log) < 3:
            self.report.add_warning(
                field="evidence_log",
                message=f"Only {len(evidence_log)} evidence entries. Recommend minimum 3."
            )

        return self.report

    def validate_section_evidence(
        self,
        evidence_log: List[Dict[str, Any]],
        section: str
    ) -> ValidationReport:
        """Validate evidence coverage for a specific section."""
        requirement = EVIDENCE_REQUIREMENTS.get(section)
        if not requirement:
            return self.report

        # Count evidence for this section
        section_evidence = [
            e for e in evidence_log
            if e.get('section', '').upper() == section.upper()
        ]

        count = len(section_evidence)
        if count < requirement.min_count:
            self.report.add_error(
                field=f"{section}.evidence",
                message=f"Only {count} evidence entries (need {requirement.min_count}). {requirement.description}"
            )
        else:
            self.report.add_success(
                field=f"{section}.evidence",
                message=f"{count} evidence entries meet requirement"
            )

        # Check quality
        if section_evidence:
            avg_quality = sum(e.get('quality_rating', 1) for e in section_evidence) / len(section_evidence)
            if avg_quality < requirement.min_quality:
                self.report.add_warning(
                    field=f"{section}.evidence_quality",
                    message=f"Average quality {avg_quality:.1f} below recommended {requirement.min_quality}"
                )

        return self.report

    def validate_confidence_level(
        self,
        level: str,
        field_name: str
    ) -> ValidationResult:
        """Validate confidence level assignment."""
        valid_levels = ['L1', 'L2', 'L3']

        if level.upper() in valid_levels:
            descriptions = {
                'L1': 'Direct evidence (interviews, contracts, metrics)',
                'L2': 'Indirect evidence (market reports, benchmarks)',
                'L3': 'Inferred (assumptions, projections)'
            }
            return ValidationResult(
                is_valid=True,
                field=field_name,
                message=f"{level.upper()}: {descriptions[level.upper()]}",
                severity="info"
            )
        else:
            return ValidationResult(
                is_valid=False,
                field=field_name,
                message=f"Invalid confidence level '{level}'. Use L1, L2, or L3",
                severity="error"
            )

    def validate_executive_brief_evidence(self, data: Dict[str, Any]) -> ValidationReport:
        """Validate evidence in Executive Brief document."""
        evidence_log = data.get('evidence_log', [])

        # Validate log structure
        self.validate_evidence_log(evidence_log)

        # Validate per-section coverage
        for section in EVIDENCE_REQUIREMENTS.keys():
            self.validate_section_evidence(evidence_log, section)

        return self.report

    def get_evidence_summary(self, evidence_log: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Get summary statistics for evidence log."""
        if not evidence_log:
            return {"count": 0, "sections": {}, "avg_quality": 0}

        by_section = {}
        total_quality = 0

        for entry in evidence_log:
            section = entry.get('section', 'Unknown')
            if section not in by_section:
                by_section[section] = []
            by_section[section].append(entry)
            total_quality += entry.get('quality_rating', 1)

        return {
            "count": len(evidence_log),
            "sections": {s: len(e) for s, e in by_section.items()},
            "avg_quality": total_quality / len(evidence_log) if evidence_log else 0,
            "by_quality": {
                q.value: len([e for e in evidence_log if e.get('quality_rating') == q.value])
                for q in EvidenceQuality
            }
        }


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def validate_evidence(
    input_path: Optional[Path] = None,
    data: Optional[Dict[str, Any]] = None,
    evidence_log: Optional[List[Dict[str, Any]]] = None
) -> ValidationReport:
    """
    Validate evidence in VIANEO document.

    Args:
        input_path: Path to input file
        data: Data dictionary
        evidence_log: Direct evidence log list

    Returns:
        ValidationReport
    """
    validator = EvidenceValidator()

    # Load data if path provided
    if data is None and input_path is not None:
        data = load_yaml(input_path)

    # Extract evidence log
    if evidence_log is None and data is not None:
        evidence_log = data.get('evidence_log', [])

    if evidence_log is not None:
        validator.validate_evidence_log(evidence_log)

        # If full document, validate section coverage
        if data is not None and 'evidence_log' in data:
            validator.validate_executive_brief_evidence(data)

    return validator.report


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Validate VIANEO evidence citations"
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input file to validate (YAML)'
    )
    parser.add_argument(
        '--summary', '-s',
        action='store_true',
        help='Show evidence summary statistics'
    )

    args = parser.parse_args()

    # Load and validate
    data = load_yaml(args.input)
    report = validate_evidence(data=data)

    # Print results
    print("\n" + "=" * 60)
    print("VIANEO Evidence Validation Report")
    print("=" * 60)
    print(f"File: {args.input}")

    if args.summary:
        validator = EvidenceValidator()
        summary = validator.get_evidence_summary(data.get('evidence_log', []))
        print(f"\nSummary:")
        print(f"  Total entries: {summary['count']}")
        print(f"  Average quality: {summary['avg_quality']:.1f}/5")
        print(f"  By section: {summary['sections']}")
        print(f"  By quality: {summary['by_quality']}")

    print("-" * 60)

    for result in report.results:
        print(result)

    print("-" * 60)
    if report.is_valid:
        print("PASSED: Evidence citations valid")
    else:
        print(f"NEEDS ATTENTION: {report.error_count} evidence issue(s)")

    return 0 if report.is_valid else 1


if __name__ == '__main__':
    exit(main())
