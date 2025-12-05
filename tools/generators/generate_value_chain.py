#!/usr/bin/env python3
"""
VIANEO Value Chain Network Generator
=====================================

Generates interactive HTML visualization for Step 9 Ecosystem Value Network Analysis.

Usage:
    python generate_value_chain.py --input value_network.yaml --output network.html
"""

import argparse
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from jinja2 import Environment, FileSystemLoader, select_autoescape

from core.constants import CharacterLimits
from core.utils import format_date, safe_filename, clean_text, load_data_file

# Template directory
TEMPLATE_DIR = Path(__file__).parent.parent / "templates"


# =============================================================================
# DATA MODELS
# =============================================================================

@dataclass
class OrganizationData:
    """Data for a single organization in the value network."""
    name: str = ""
    role: str = ""
    requester: str = ""
    acceptability: str = "neutral"  # favorable, neutral, unfavorable
    need_level: str = "None"        # Critical, Important, Secondary, None
    notes: str = ""

    @property
    def acceptability_emoji(self) -> str:
        emojis = {
            "favorable": "green",
            "neutral": "yellow",
            "unfavorable": "red"
        }
        return emojis.get(self.acceptability.lower(), "yellow")

    @property
    def acceptability_color(self) -> str:
        colors = {
            "favorable": "#28a745",
            "neutral": "#ffc107",
            "unfavorable": "#dc3545"
        }
        return colors.get(self.acceptability.lower(), "#ffc107")


@dataclass
class ValueChainData:
    """Data structure for the complete value network."""

    # Document info
    project_name: str = ""
    analysis_date: str = ""
    analyst: str = ""
    project_stage: str = ""

    # Executive summary
    total_organizations: int = 0
    priority_targets: int = 0
    key_insight: str = ""
    strategic_implication: str = ""

    # Project overview
    product_name: str = ""
    tagline: str = ""
    industry: str = ""
    core_solution: str = ""
    key_features: List[str] = field(default_factory=list)

    # Value chain sections
    enablers_influencers: List[OrganizationData] = field(default_factory=list)
    products_solutions: List[OrganizationData] = field(default_factory=list)
    channels_partners: List[OrganizationData] = field(default_factory=list)
    buyers: List[OrganizationData] = field(default_factory=list)
    end_users: List[OrganizationData] = field(default_factory=list)


# =============================================================================
# TEMPLATE LOADING
# =============================================================================

def _get_jinja_env() -> Environment:
    """Get Jinja2 environment configured for HTML templates."""
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(['html', 'xml'])
    )


# =============================================================================
# HTML GENERATION
# =============================================================================

class ValueChainGenerator:
    """Generator for VIANEO Value Chain HTML visualization."""

    def __init__(self, data: ValueChainData):
        self.data = data

    def generate_html(self, output_path: Path) -> bool:
        """Generate interactive HTML visualization using Jinja2 template."""
        env = _get_jinja_env()
        template = env.get_template('value_network.html.jinja2')

        # Prepare value chain sections for template
        value_chain_sections = [
            {"title": "Enablers & Influencers", "organizations": self.data.enablers_influencers},
            {"title": "Products & Solutions", "organizations": self.data.products_solutions},
            {"title": "Channels & Partners", "organizations": self.data.channels_partners},
            {"title": "Buyers", "organizations": self.data.buyers},
            {"title": "End Users", "organizations": self.data.end_users}
        ]

        # Prepare detail sections for template
        detail_sections = [
            {
                "title": "Section 3: Enablers & Influencers",
                "description": "Organizations that provide infrastructure, funding, regulation, standards, or expertise.",
                "organizations": self._prepare_orgs_for_template(self.data.enablers_influencers)
            },
            {
                "title": "Section 4: Products & Solutions",
                "description": "Organizations that produce complementary or substitute products/solutions.",
                "organizations": self._prepare_orgs_for_template(self.data.products_solutions)
            },
            {
                "title": "Section 5: Channels & Partners",
                "description": "Organizations that facilitate distribution, adoption, or implementation.",
                "organizations": self._prepare_orgs_for_template(self.data.channels_partners)
            },
            {
                "title": "Section 6: Buyers",
                "description": "Organizations or entities that pay for your solution.",
                "organizations": self._prepare_orgs_for_template(self.data.buyers)
            },
            {
                "title": "Section 7: End Users",
                "description": "Individual people or departments who directly use your innovation.",
                "organizations": self._prepare_orgs_for_template(self.data.end_users)
            }
        ]

        html = template.render(
            project_name=self.data.project_name,
            analysis_date=self.data.analysis_date or format_date(),
            analyst=self.data.analyst,
            project_stage=self.data.project_stage,
            total_organizations=self._count_total_orgs(),
            priority_targets=self._count_priority_targets(),
            key_insight=self.data.key_insight,
            strategic_implication=self.data.strategic_implication,
            product_name=self.data.product_name,
            tagline=self.data.tagline,
            industry=self.data.industry,
            core_solution=self.data.core_solution,
            key_features=self.data.key_features,
            value_chain_sections=value_chain_sections,
            detail_sections=detail_sections,
            generation_date=format_date()
        )

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        return True

    def _prepare_orgs_for_template(self, orgs: List[OrganizationData]) -> List[Dict[str, Any]]:
        """Prepare organization data for Jinja2 template."""
        return [
            {
                "name": org.name,
                "role": org.role,
                "requester": org.requester,
                "acceptability": org.acceptability,
                "acceptability_color": org.acceptability_emoji,  # green, yellow, red
                "need_level": org.need_level,
                "notes": org.notes
            }
            for org in orgs
        ]

    def _count_total_orgs(self) -> int:
        return sum(len(section) for section in [
            self.data.enablers_influencers,
            self.data.products_solutions,
            self.data.channels_partners,
            self.data.buyers,
            self.data.end_users
        ])

    def _count_priority_targets(self) -> int:
        count = 0
        for section in [
            self.data.enablers_influencers,
            self.data.products_solutions,
            self.data.channels_partners,
            self.data.buyers,
            self.data.end_users
        ]:
            for org in section:
                if (org.acceptability.lower() == 'favorable' and
                    org.need_level in ['Critical', 'Important']):
                    count += 1
        return count


# =============================================================================
# MARKDOWN GENERATION
# =============================================================================

def generate_markdown(data: ValueChainData) -> str:
    """Generate markdown version of value network analysis."""
    generator = ValueChainGenerator(data)

    md = f"""# Vianeo Step 8: Ecosystem Value Network Analysis
## {data.project_name}

**Project:** {data.project_name}
**Analysis Date:** {data.analysis_date or format_date()}
**Analyst:** {data.analyst}
**Project Stage:** {data.project_stage}

---

## EXECUTIVE SUMMARY

**Total Organizations Mapped:** {generator._count_total_orgs()} across 5 value chain positions
**Priority Targets Identified:** {generator._count_priority_targets()} organizations (Favorable + Critical/Important needs)
**Key Insight:** {data.key_insight}

**Strategic Implication:**
{data.strategic_implication}

---

## Section 1: PROJECT OVERVIEW

### Core Product/Service

**Product/Service Name:** {data.product_name}

**Tagline:** {data.tagline}

**Industry/Domain:** {data.industry}

**Core Solution:** {data.core_solution}

### Key Features

"""
    for i, feature in enumerate(data.key_features, 1):
        md += f"{i}. {feature}\n"

    # Add sections
    sections = [
        ("Section 3: ENABLERS & INFLUENCERS", data.enablers_influencers,
         "Organizations that provide infrastructure, funding, regulation, standards, or expertise."),
        ("Section 4: PRODUCTS & SOLUTIONS", data.products_solutions,
         "Organizations that produce complementary or substitute products/solutions."),
        ("Section 5: CHANNELS & PARTNERS", data.channels_partners,
         "Organizations that facilitate distribution, adoption, or implementation."),
        ("Section 6: BUYERS", data.buyers,
         "Organizations or entities that pay for your solution."),
        ("Section 7: END USERS", data.end_users,
         "Individual people or departments who directly use your innovation.")
    ]

    for title, orgs, description in sections:
        md += f"\n---\n\n## {title}\n\n*{description}*\n\n"

        if orgs:
            md += "| Organization Name | Role/Description | Requester | Acceptability | Need Level | Notes |\n"
            md += "|-------------------|------------------|-----------|---------------|------------|-------|\n"

            for org in orgs:
                emoji = {"favorable": "[F]", "neutral": "[N]", "unfavorable": "[U]"}.get(
                    org.acceptability.lower(), "[N]"
                )
                notes = org.notes[:100] + "..." if len(org.notes) > 100 else org.notes
                md += f"| {org.name} | {org.role} | {org.requester} | {emoji} | {org.need_level} | {notes} |\n"
        else:
            md += "*No organizations in this category*\n"

    md += f"""
---

**This specification ensures every Step 9 output follows the exact same format for professional consistency and strategic clarity.**

Generated: {format_date()}
"""

    return md


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def generate_value_chain(
    input_path: Optional[Path] = None,
    output_path: Optional[Path] = None,
    data: Optional[ValueChainData] = None,
    output_format: str = "both"
) -> Dict[str, Path]:
    """
    Generate Value Chain visualization(s).

    Args:
        input_path: Path to input data file (JSON/YAML)
        output_path: Path for output file (without extension)
        data: ValueChainData object (alternative to input_path)
        output_format: "html", "md", or "both"

    Returns:
        Dict mapping format to output path
    """
    # Load data if not provided
    if data is None:
        if input_path is None:
            raise ValueError("Either input_path or data must be provided")

        raw_data = load_data_file(input_path)

        # Parse organizations
        def parse_orgs(key: str) -> List[OrganizationData]:
            orgs = []
            for o in raw_data.get(key, []):
                orgs.append(OrganizationData(**o))
            return orgs

        data = ValueChainData(
            project_name=raw_data.get('project_name', 'Project'),
            analysis_date=raw_data.get('analysis_date', ''),
            analyst=raw_data.get('analyst', ''),
            project_stage=raw_data.get('project_stage', ''),
            key_insight=raw_data.get('key_insight', ''),
            strategic_implication=raw_data.get('strategic_implication', ''),
            product_name=raw_data.get('product_name', ''),
            tagline=raw_data.get('tagline', ''),
            industry=raw_data.get('industry', ''),
            core_solution=raw_data.get('core_solution', ''),
            key_features=raw_data.get('key_features', []),
            enablers_influencers=parse_orgs('enablers_influencers'),
            products_solutions=parse_orgs('products_solutions'),
            channels_partners=parse_orgs('channels_partners'),
            buyers=parse_orgs('buyers'),
            end_users=parse_orgs('end_users')
        )

    # Determine output path
    if output_path is None:
        project_name = safe_filename(data.project_name or "Project")
        date_str = format_date()
        output_path = Path(f"{project_name}_{date_str}_09_Value_Network")

    output_path = Path(output_path)
    outputs = {}

    # Generate HTML
    if output_format in ["html", "both"]:
        html_path = output_path.with_suffix('.html')
        generator = ValueChainGenerator(data)
        if generator.generate_html(html_path):
            outputs['html'] = html_path
            print(f"Generated HTML: {html_path}")

    # Generate Markdown
    if output_format in ["md", "both"]:
        md_path = output_path.with_suffix('.md')
        md_content = generate_markdown(data)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        outputs['md'] = md_path
        print(f"Generated Markdown: {md_path}")

    return outputs


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate VIANEO Value Chain Network visualization"
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        help='Input data file (JSON or YAML)'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output file path (without extension)'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['html', 'md', 'both'],
        default='both',
        help='Output format (default: both)'
    )

    args = parser.parse_args()

    if args.input:
        outputs = generate_value_chain(
            input_path=args.input,
            output_path=args.output,
            output_format=args.format
        )
        print(f"\nGenerated {len(outputs)} file(s)")
    else:
        print("No input file provided. Use --input to specify data file.")


if __name__ == '__main__':
    main()
