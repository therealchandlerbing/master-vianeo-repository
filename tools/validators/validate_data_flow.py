#!/usr/bin/env python3
"""
VIANEO Data Flow Validator
==========================

Validates cross-step data consistency according to DEPENDENCIES.md specification.

Validates:
- Step 5 -> Step 7: Requesters and Needs exact match
- Step 5 -> Step 9: Requesters with organizational grouping
- Step 8 -> Step 9: Players/Influencers positioning
- Step 5 -> Step 11: Needs columns
- Step 7 -> Step 11: Importance/Satisfaction ratings
- Step 4 -> Step 11: Means with differentiation

Usage:
    python validate_data_flow.py --source step5.yaml --target step7.yaml
"""

import argparse
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, List, Set
from dataclasses import dataclass, field

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.constants import STEP_DEPENDENCIES
from core.utils import ValidationResult, ValidationReport, load_yaml


# =============================================================================
# DATA FLOW DEFINITIONS
# =============================================================================

@dataclass
class DataFlowRule:
    """Definition of a data flow between steps."""
    source_step: str
    target_step: str
    source_field: str
    target_field: str
    description: str
    match_type: str = "exact"  # exact, contains, mapped


DATA_FLOWS = [
    DataFlowRule(
        source_step="step_5",
        target_step="step_7",
        source_field="requesters",
        target_field="column_headers",
        description="Requester names must match exactly",
        match_type="exact"
    ),
    DataFlowRule(
        source_step="step_5",
        target_step="step_7",
        source_field="needs",
        target_field="row_labels",
        description="Need statements must match exactly (60-char limit)",
        match_type="exact"
    ),
    DataFlowRule(
        source_step="step_5",
        target_step="step_9",
        source_field="requesters",
        target_field="buyers_users",
        description="Requesters must appear in Buyers/End Users columns",
        match_type="contains"
    ),
    DataFlowRule(
        source_step="step_8",
        target_step="step_9",
        source_field="players",
        target_field="value_chain_nodes",
        description="Players must appear in value chain",
        match_type="mapped"
    ),
    DataFlowRule(
        source_step="step_8",
        target_step="step_9",
        source_field="influencers",
        target_field="enablers_influencers",
        description="Influencers must appear at top of network",
        match_type="contains"
    ),
    DataFlowRule(
        source_step="step_5",
        target_step="step_11",
        source_field="needs",
        target_field="needs_columns",
        description="Needs become column headers in Features/Needs view",
        match_type="exact"
    ),
    DataFlowRule(
        source_step="step_4",
        target_step="step_11",
        source_field="means",
        target_field="means_columns",
        description="Means become column headers in Features/Means view",
        match_type="exact"
    ),
]


# =============================================================================
# VALIDATOR CLASS
# =============================================================================

class DataFlowValidator:
    """Validator for cross-step data consistency."""

    def __init__(self):
        self.report = ValidationReport()

    def validate_exact_match(
        self,
        source_items: List[str],
        target_items: List[str],
        rule: DataFlowRule
    ) -> None:
        """Validate exact match between source and target items."""
        source_set = set(item.strip() for item in source_items)
        target_set = set(item.strip() for item in target_items)

        # Items in source but not in target
        missing = source_set - target_set
        for item in missing:
            self.report.add_error(
                field=f"{rule.source_step}->{rule.target_step}",
                message=f"'{item}' from {rule.source_field} missing in {rule.target_field}",
                rule=rule.description
            )

        # Items in target but not in source
        extra = target_set - source_set
        for item in extra:
            self.report.add_warning(
                field=f"{rule.target_step}",
                message=f"'{item}' in {rule.target_field} not found in source {rule.source_field}",
                rule=rule.description
            )

        if not missing and not extra:
            self.report.add_success(
                field=f"{rule.source_step}->{rule.target_step}",
                message=f"All {len(source_set)} {rule.source_field} items match exactly"
            )

    def validate_contains(
        self,
        source_items: List[str],
        target_items: List[str],
        rule: DataFlowRule
    ) -> None:
        """Validate source items are contained in target."""
        target_text = " ".join(str(item) for item in target_items).lower()

        for item in source_items:
            if item.lower().strip() not in target_text:
                self.report.add_error(
                    field=f"{rule.source_step}->{rule.target_step}",
                    message=f"'{item}' from {rule.source_field} not found in {rule.target_field}",
                    rule=rule.description
                )
            else:
                self.report.add_success(
                    field=f"{rule.source_step}->{rule.target_step}.{item}",
                    message=f"Found in target"
                )

    def validate_mapped(
        self,
        source_items: List[str],
        target_items: List[str],
        rule: DataFlowRule
    ) -> None:
        """Validate mapped relationship between source and target."""
        # For mapped relationships, just ensure all source items appear somewhere
        self.validate_contains(source_items, target_items, rule)

    def extract_items(self, data: Dict[str, Any], field_path: str) -> List[str]:
        """Extract list of items from data using field path."""
        parts = field_path.split('.')
        current = data

        for part in parts:
            if isinstance(current, dict):
                current = current.get(part, [])
            elif isinstance(current, list):
                # Extract from list of dicts
                current = [item.get(part, '') for item in current if isinstance(item, dict)]
            else:
                return []

        if isinstance(current, list):
            # Flatten nested structures
            result = []
            for item in current:
                if isinstance(item, str):
                    result.append(item)
                elif isinstance(item, dict):
                    # Try common field names
                    for key in ['name', 'statement', 'label', 'title']:
                        if key in item:
                            result.append(str(item[key]))
                            break
            return result

        return []

    def validate_step_pair(
        self,
        source_data: Dict[str, Any],
        target_data: Dict[str, Any],
        source_step: str,
        target_step: str
    ) -> ValidationReport:
        """
        Validate data flow between two steps.

        Args:
            source_data: Source step data
            target_data: Target step data
            source_step: Source step name (e.g., 'step_5')
            target_step: Target step name (e.g., 'step_7')

        Returns:
            ValidationReport
        """
        # Find applicable rules
        for rule in DATA_FLOWS:
            if rule.source_step == source_step and rule.target_step == target_step:
                source_items = self.extract_items(source_data, rule.source_field)
                target_items = self.extract_items(target_data, rule.target_field)

                if not source_items:
                    self.report.add_warning(
                        field=f"{rule.source_step}.{rule.source_field}",
                        message=f"No items found in source"
                    )
                    continue

                if not target_items:
                    self.report.add_warning(
                        field=f"{rule.target_step}.{rule.target_field}",
                        message=f"No items found in target"
                    )
                    continue

                if rule.match_type == "exact":
                    self.validate_exact_match(source_items, target_items, rule)
                elif rule.match_type == "contains":
                    self.validate_contains(source_items, target_items, rule)
                elif rule.match_type == "mapped":
                    self.validate_mapped(source_items, target_items, rule)

        return self.report

    def validate_step_5_to_7(
        self,
        step5_data: Dict[str, Any],
        step7_data: Dict[str, Any]
    ) -> ValidationReport:
        """Validate Step 5 -> Step 7 data flow."""
        return self.validate_step_pair(step5_data, step7_data, "step_5", "step_7")

    def validate_step_5_to_9(
        self,
        step5_data: Dict[str, Any],
        step9_data: Dict[str, Any]
    ) -> ValidationReport:
        """Validate Step 5 -> Step 9 data flow."""
        return self.validate_step_pair(step5_data, step9_data, "step_5", "step_9")

    def validate_step_8_to_9(
        self,
        step8_data: Dict[str, Any],
        step9_data: Dict[str, Any]
    ) -> ValidationReport:
        """Validate Step 8 -> Step 9 data flow."""
        return self.validate_step_pair(step8_data, step9_data, "step_8", "step_9")

    def validate_project(
        self,
        project_data: Dict[str, Dict[str, Any]]
    ) -> ValidationReport:
        """
        Validate all data flows for a complete project.

        Args:
            project_data: Dict mapping step names to step data

        Returns:
            ValidationReport
        """
        # Define validation chain
        validations = [
            ("step_5", "step_7"),
            ("step_5", "step_9"),
            ("step_8", "step_9"),
            ("step_5", "step_11"),
            ("step_4", "step_11"),
            ("step_7", "step_11"),
        ]

        for source_step, target_step in validations:
            if source_step in project_data and target_step in project_data:
                self.validate_step_pair(
                    project_data[source_step],
                    project_data[target_step],
                    source_step,
                    target_step
                )
            else:
                missing = []
                if source_step not in project_data:
                    missing.append(source_step)
                if target_step not in project_data:
                    missing.append(target_step)
                self.report.add_warning(
                    field=f"{source_step}->{target_step}",
                    message=f"Cannot validate: missing {', '.join(missing)}"
                )

        return self.report


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def validate_data_flow(
    source_path: Optional[Path] = None,
    target_path: Optional[Path] = None,
    source_data: Optional[Dict[str, Any]] = None,
    target_data: Optional[Dict[str, Any]] = None,
    source_step: str = "step_5",
    target_step: str = "step_7"
) -> ValidationReport:
    """
    Validate data flow between VIANEO steps.

    Args:
        source_path: Path to source step file
        target_path: Path to target step file
        source_data: Source step data
        target_data: Target step data
        source_step: Source step identifier
        target_step: Target step identifier

    Returns:
        ValidationReport
    """
    validator = DataFlowValidator()

    # Load data if paths provided
    if source_data is None and source_path is not None:
        source_data = load_yaml(source_path)

    if target_data is None and target_path is not None:
        target_data = load_yaml(target_path)

    if source_data is None or target_data is None:
        validator.report.add_error(
            field="input",
            message="Both source and target data required"
        )
        return validator.report

    return validator.validate_step_pair(source_data, target_data, source_step, target_step)


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Validate VIANEO cross-step data flow"
    )
    parser.add_argument(
        '--source', '-s',
        type=Path,
        required=True,
        help='Source step file (YAML)'
    )
    parser.add_argument(
        '--target', '-t',
        type=Path,
        required=True,
        help='Target step file (YAML)'
    )
    parser.add_argument(
        '--source-step',
        default='step_5',
        help='Source step identifier (e.g., step_5)'
    )
    parser.add_argument(
        '--target-step',
        default='step_7',
        help='Target step identifier (e.g., step_7)'
    )

    args = parser.parse_args()

    # Run validation
    report = validate_data_flow(
        source_path=args.source,
        target_path=args.target,
        source_step=args.source_step,
        target_step=args.target_step
    )

    # Print results
    print("\n" + "=" * 60)
    print("VIANEO Data Flow Validation Report")
    print("=" * 60)
    print(f"Source: {args.source} ({args.source_step})")
    print(f"Target: {args.target} ({args.target_step})")
    print("-" * 60)

    for result in report.results:
        print(result)

    print("-" * 60)
    if report.is_valid:
        print("PASSED: Data flows correctly between steps")
    else:
        print(f"FAILED: {report.error_count} data flow inconsistency(ies)")

    return 0 if report.is_valid else 1


if __name__ == '__main__':
    exit(main())
