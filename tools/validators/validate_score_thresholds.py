#!/usr/bin/env python3
"""
VIANEO Score Threshold Validator
================================

Validates that dimension scores meet minimum thresholds.

Thresholds enforced:
- Minimum viable: >= 3.0 for all dimensions
- Investment ready: >= 3.5 for all dimensions

Usage:
    python validate_score_thresholds.py --input assessment.yaml
    python validate_score_thresholds.py --input diagnostic.md
"""

import argparse
import json
import yaml
import re
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.constants import ScoreThresholds, VIANEO_DIMENSIONS
from core.utils import ValidationResult, ValidationReport, load_yaml, load_json


# =============================================================================
# VALIDATOR CLASS
# =============================================================================

@dataclass
class DimensionThreshold:
    """Threshold configuration for a dimension."""
    name: str
    min_viable: float = 3.0
    investment_ready: float = 3.5


class ScoreThresholdValidator:
    """Validator for VIANEO dimension score thresholds."""

    DIMENSIONS = {
        'legitimacy': DimensionThreshold('Legitimacy'),
        'desirability': DimensionThreshold('Desirability'),
        'acceptability': DimensionThreshold('Acceptability'),
        'feasibility': DimensionThreshold('Feasibility'),
        'viability': DimensionThreshold('Viability'),
    }

    def __init__(self, threshold_level: str = 'viable'):
        """
        Initialize validator.

        Args:
            threshold_level: 'viable' (>= 3.0) or 'investment' (>= 3.5)
        """
        self.threshold_level = threshold_level
        self.report = ValidationReport()

    def get_threshold(self, dimension: str) -> float:
        """Get threshold for dimension based on level."""
        dim = self.DIMENSIONS.get(dimension.lower())
        if dim is None:
            return 3.0

        if self.threshold_level == 'investment':
            return dim.investment_ready
        return dim.min_viable

    def validate_score(
        self,
        dimension: str,
        score: float,
        field_name: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate a single dimension score.

        Args:
            dimension: Dimension name
            score: Score value (0-5)
            field_name: Override field name for reporting

        Returns:
            ValidationResult
        """
        field = field_name or dimension
        threshold = self.get_threshold(dimension)
        status = ScoreThresholds.get_status_keyword(score)

        # Validate range
        if not 0 <= score <= 5:
            result = ValidationResult(
                is_valid=False,
                field=field,
                message=f"Score {score} outside valid range (0-5)",
                severity="error"
            )
            self.report.add(result)
            return result

        # Validate threshold
        if score >= threshold:
            result = ValidationResult(
                is_valid=True,
                field=field,
                message=f"{score:.1f}/5 ({status}) - meets {self.threshold_level} threshold ({threshold})",
                severity="info",
                details={
                    "score": score,
                    "threshold": threshold,
                    "status": status,
                    "margin": score - threshold
                }
            )
        else:
            gap = threshold - score
            result = ValidationResult(
                is_valid=False,
                field=field,
                message=f"{score:.1f}/5 ({status}) - below {self.threshold_level} threshold ({threshold}, gap: {gap:.1f})",
                severity="error" if gap >= 0.5 else "warning",
                details={
                    "score": score,
                    "threshold": threshold,
                    "status": status,
                    "gap": gap
                }
            )

        self.report.add(result)
        return result

    def validate_all_dimensions(self, scores: Dict[str, float]) -> ValidationReport:
        """
        Validate all dimension scores.

        Args:
            scores: Dict mapping dimension name to score

        Returns:
            ValidationReport
        """
        for dimension in self.DIMENSIONS.keys():
            if dimension in scores:
                self.validate_score(dimension, scores[dimension])
            elif dimension.capitalize() in scores:
                self.validate_score(dimension, scores[dimension.capitalize()])
            else:
                self.report.add_warning(
                    field=dimension,
                    message=f"Dimension score not provided"
                )

        # Calculate overall
        provided_scores = []
        for dim in self.DIMENSIONS.keys():
            if dim in scores:
                provided_scores.append(scores[dim])
            elif dim.capitalize() in scores:
                provided_scores.append(scores[dim.capitalize()])

        if provided_scores:
            avg = sum(provided_scores) / len(provided_scores)
            self.report.add_success(
                field="Overall Average",
                message=f"{avg:.2f}/5 across {len(provided_scores)} dimensions"
            )

        return self.report

    def validate_diagnostic_data(self, data: Dict[str, Any]) -> ValidationReport:
        """
        Validate scores in diagnostic data.

        Args:
            data: Diagnostic data dictionary

        Returns:
            ValidationReport
        """
        dimension_scores = data.get('dimension_scores', [])

        scores = {}
        for dim in dimension_scores:
            name = dim.get('name', '').lower()
            score = dim.get('score', 0)
            if name in self.DIMENSIONS:
                scores[name] = score

        return self.validate_all_dimensions(scores)

    def validate_markdown(self, markdown: str) -> ValidationReport:
        """
        Validate scores in markdown diagnostic document.

        Args:
            markdown: Markdown content

        Returns:
            ValidationReport
        """
        # Find dimension table
        pattern = r'\|\s*\*?\*?(\w+)\*?\*?\s*\|\s*(\d+\.?\d*)/5\s*\|'
        matches = re.findall(pattern, markdown)

        scores = {}
        for name, score_str in matches:
            name_lower = name.lower()
            if name_lower in self.DIMENSIONS:
                try:
                    scores[name_lower] = float(score_str)
                except ValueError:
                    pass

        return self.validate_all_dimensions(scores)

    def get_recommendations(self) -> List[str]:
        """Get recommendations based on validation results."""
        recommendations = []

        for result in self.report.results:
            if not result.is_valid:
                dimension = result.field
                gap = result.details.get('gap', 0)

                if gap >= 1.0:
                    recommendations.append(
                        f"{dimension}: Critical gap ({gap:.1f}). Requires significant work before proceeding."
                    )
                elif gap >= 0.5:
                    recommendations.append(
                        f"{dimension}: Moderate gap ({gap:.1f}). Focus area for improvement."
                    )
                else:
                    recommendations.append(
                        f"{dimension}: Minor gap ({gap:.1f}). Close to threshold."
                    )

        return recommendations


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def validate_score_thresholds(
    input_path: Optional[Path] = None,
    data: Optional[Dict[str, Any]] = None,
    scores: Optional[Dict[str, float]] = None,
    threshold_level: str = 'viable'
) -> ValidationReport:
    """
    Validate dimension score thresholds.

    Args:
        input_path: Path to input file
        data: Data dictionary
        scores: Direct scores dictionary
        threshold_level: 'viable' or 'investment'

    Returns:
        ValidationReport
    """
    validator = ScoreThresholdValidator(threshold_level)

    # Direct scores provided
    if scores is not None:
        return validator.validate_all_dimensions(scores)

    # Load data
    if data is None and input_path is not None:
        input_path = Path(input_path)

        if input_path.suffix in ['.yaml', '.yml']:
            data = load_yaml(input_path)
        elif input_path.suffix == '.json':
            data = load_json(input_path)
        elif input_path.suffix == '.md':
            with open(input_path, 'r', encoding='utf-8') as f:
                return validator.validate_markdown(f.read())
        else:
            raise ValueError(f"Unsupported file type: {input_path.suffix}")

    # Validate data
    if data is not None:
        if 'dimension_scores' in data:
            return validator.validate_diagnostic_data(data)
        else:
            # Try to find scores in data
            scores = {}
            for key, value in data.items():
                if key.lower() in validator.DIMENSIONS and isinstance(value, (int, float)):
                    scores[key.lower()] = float(value)
            if scores:
                return validator.validate_all_dimensions(scores)

    return validator.report


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Validate VIANEO dimension score thresholds"
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        help='Input file to validate'
    )
    parser.add_argument(
        '--threshold', '-t',
        choices=['viable', 'investment'],
        default='viable',
        help='Threshold level: viable (>=3.0) or investment (>=3.5)'
    )
    parser.add_argument(
        '--scores', '-s',
        type=str,
        help='Direct scores as JSON (e.g., \'{"legitimacy": 3.5, "desirability": 4.0}\')'
    )

    args = parser.parse_args()

    # Parse direct scores if provided
    scores = None
    if args.scores:
        scores = json.loads(args.scores)

    # Run validation
    report = validate_score_thresholds(
        input_path=args.input,
        scores=scores,
        threshold_level=args.threshold
    )

    # Print results
    print("\n" + "=" * 60)
    print(f"VIANEO Score Threshold Validation ({args.threshold.upper()} level)")
    print("=" * 60)

    if args.input:
        print(f"File: {args.input}")

    print(f"Threshold: >= {3.5 if args.threshold == 'investment' else 3.0}")
    print("-" * 60)

    for result in report.results:
        status_icon = "" if result.is_valid else ""
        if result.severity == "warning":
            status_icon = ""
        print(f"{status_icon} {result}")

    print("-" * 60)

    # Get recommendations
    validator = ScoreThresholdValidator(args.threshold)
    validator.report = report
    recommendations = validator.get_recommendations()

    if recommendations:
        print("\nRecommendations:")
        for rec in recommendations:
            print(f"  - {rec}")

    print("-" * 60)
    if report.is_valid:
        print("PASSED: All scores meet threshold")
    else:
        print(f"NEEDS ATTENTION: {report.error_count} dimension(s) below threshold")

    return 0 if report.is_valid else 1


if __name__ == '__main__':
    exit(main())
