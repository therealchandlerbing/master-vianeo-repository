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

from core.constants import CharacterLimits
from core.utils import format_date, safe_filename, clean_text


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
# HTML TEMPLATES
# =============================================================================

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name} - Value Network Analysis</title>
    <style>
        :root {{
            --primary-blue: #1B365D;
            --accent-blue: #2E5C8A;
            --green: #28a745;
            --yellow: #ffc107;
            --red: #dc3545;
            --gray-100: #f8f9fa;
            --gray-200: #e9ecef;
            --gray-600: #6c757d;
            --gray-800: #343a40;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', Calibri, sans-serif;
            line-height: 1.6;
            color: var(--gray-800);
            background: var(--gray-100);
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        header {{
            background: var(--primary-blue);
            color: white;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 8px;
        }}

        header h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}

        header .subtitle {{
            opacity: 0.8;
            font-size: 1rem;
        }}

        .metadata {{
            display: flex;
            gap: 2rem;
            margin-top: 1rem;
            font-size: 0.875rem;
            opacity: 0.9;
        }}

        .card {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }}

        .card h2 {{
            color: var(--primary-blue);
            font-size: 1.25rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--gray-200);
            padding-bottom: 0.5rem;
        }}

        .card h3 {{
            color: var(--accent-blue);
            font-size: 1rem;
            margin: 1rem 0 0.5rem 0;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1rem;
        }}

        .summary-item {{
            background: var(--gray-100);
            padding: 1rem;
            border-radius: 4px;
            text-align: center;
        }}

        .summary-item .value {{
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary-blue);
        }}

        .summary-item .label {{
            font-size: 0.875rem;
            color: var(--gray-600);
        }}

        .value-chain {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1rem;
            margin: 2rem 0;
        }}

        @media (max-width: 1024px) {{
            .value-chain {{
                grid-template-columns: repeat(3, 1fr);
            }}
        }}

        @media (max-width: 768px) {{
            .value-chain {{
                grid-template-columns: 1fr;
            }}
        }}

        .chain-column {{
            background: var(--gray-100);
            border-radius: 8px;
            padding: 1rem;
        }}

        .chain-column h3 {{
            color: var(--primary-blue);
            font-size: 0.875rem;
            text-align: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--primary-blue);
        }}

        .org-card {{
            background: white;
            border-radius: 4px;
            padding: 0.75rem;
            margin-bottom: 0.5rem;
            border-left: 4px solid var(--gray-200);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }}

        .org-card:hover {{
            transform: translateX(4px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }}

        .org-card.favorable {{
            border-left-color: var(--green);
        }}

        .org-card.neutral {{
            border-left-color: var(--yellow);
        }}

        .org-card.unfavorable {{
            border-left-color: var(--red);
        }}

        .org-card .name {{
            font-weight: 600;
            font-size: 0.875rem;
            margin-bottom: 0.25rem;
        }}

        .org-card .role {{
            font-size: 0.75rem;
            color: var(--gray-600);
            margin-bottom: 0.5rem;
        }}

        .org-card .badges {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        .badge {{
            font-size: 0.625rem;
            padding: 0.125rem 0.5rem;
            border-radius: 10px;
            font-weight: 600;
        }}

        .badge-green {{
            background: #d4edda;
            color: #155724;
        }}

        .badge-yellow {{
            background: #fff3cd;
            color: #856404;
        }}

        .badge-red {{
            background: #f8d7da;
            color: #721c24;
        }}

        .badge-blue {{
            background: #cce5ff;
            color: #004085;
        }}

        .badge-gray {{
            background: var(--gray-200);
            color: var(--gray-600);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
            font-size: 0.875rem;
        }}

        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid var(--gray-200);
        }}

        th {{
            background: var(--gray-100);
            font-weight: 600;
            color: var(--primary-blue);
        }}

        tr:hover {{
            background: var(--gray-100);
        }}

        .acceptability-dot {{
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 0.5rem;
        }}

        .dot-green {{ background: var(--green); }}
        .dot-yellow {{ background: var(--yellow); }}
        .dot-red {{ background: var(--red); }}

        .legend {{
            display: flex;
            gap: 1.5rem;
            margin: 1rem 0;
            font-size: 0.875rem;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .features-list {{
            list-style: none;
            padding: 0;
        }}

        .features-list li {{
            padding: 0.5rem 0;
            border-bottom: 1px solid var(--gray-200);
        }}

        .features-list li:last-child {{
            border-bottom: none;
        }}

        footer {{
            text-align: center;
            padding: 2rem;
            color: var(--gray-600);
            font-size: 0.875rem;
        }}

        .tooltip {{
            position: fixed;
            background: var(--gray-800);
            color: white;
            padding: 1rem;
            border-radius: 4px;
            max-width: 300px;
            font-size: 0.75rem;
            z-index: 1000;
            display: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}

        .tooltip.visible {{
            display: block;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Vianeo Step 9: Ecosystem Value Network Analysis</h1>
            <div class="subtitle">{project_name}</div>
            <div class="metadata">
                <span><strong>Project:</strong> {project_name}</span>
                <span><strong>Analysis Date:</strong> {analysis_date}</span>
                <span><strong>Analyst:</strong> {analyst}</span>
                <span><strong>Stage:</strong> {project_stage}</span>
            </div>
        </header>

        <div class="card">
            <h2>Executive Summary</h2>
            <div class="summary-grid">
                <div class="summary-item">
                    <div class="value">{total_organizations}</div>
                    <div class="label">Organizations Mapped</div>
                </div>
                <div class="summary-item">
                    <div class="value">{priority_targets}</div>
                    <div class="label">Priority Targets</div>
                </div>
            </div>
            <h3>Key Insight</h3>
            <p>{key_insight}</p>
            <h3>Strategic Implication</h3>
            <p>{strategic_implication}</p>
        </div>

        <div class="card">
            <h2>Project Overview</h2>
            <p><strong>{product_name}</strong>: {tagline}</p>
            <p><strong>Industry:</strong> {industry}</p>
            <p><strong>Core Solution:</strong> {core_solution}</p>
            <h3>Key Features</h3>
            <ul class="features-list">
                {features_html}
            </ul>
        </div>

        <div class="card">
            <h2>Value Network Visualization</h2>
            <div class="legend">
                <div class="legend-item">
                    <span class="acceptability-dot dot-green"></span> Favorable
                </div>
                <div class="legend-item">
                    <span class="acceptability-dot dot-yellow"></span> Neutral
                </div>
                <div class="legend-item">
                    <span class="acceptability-dot dot-red"></span> Unfavorable
                </div>
            </div>
            <div class="value-chain">
                {value_chain_html}
            </div>
        </div>

        {detail_tables_html}

        <footer>
            <p>VIANEO Framework v2.0 | Generated {generation_date}</p>
        </footer>
    </div>

    <div id="tooltip" class="tooltip"></div>

    <script>
        // Tooltip functionality
        const tooltip = document.getElementById('tooltip');
        const orgCards = document.querySelectorAll('.org-card');

        orgCards.forEach(card => {{
            card.addEventListener('mouseenter', (e) => {{
                const notes = card.dataset.notes;
                if (notes) {{
                    tooltip.textContent = notes;
                    tooltip.classList.add('visible');
                }}
            }});

            card.addEventListener('mousemove', (e) => {{
                tooltip.style.left = e.pageX + 15 + 'px';
                tooltip.style.top = e.pageY + 15 + 'px';
            }});

            card.addEventListener('mouseleave', () => {{
                tooltip.classList.remove('visible');
            }});
        }});
    </script>
</body>
</html>
"""


# =============================================================================
# HTML GENERATION
# =============================================================================

class ValueChainGenerator:
    """Generator for VIANEO Value Chain HTML visualization."""

    def __init__(self, data: ValueChainData):
        self.data = data

    def generate_html(self, output_path: Path) -> bool:
        """Generate interactive HTML visualization."""
        html = HTML_TEMPLATE.format(
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
            features_html=self._generate_features_html(),
            value_chain_html=self._generate_value_chain_html(),
            detail_tables_html=self._generate_detail_tables_html(),
            generation_date=format_date()
        )

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        return True

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

    def _generate_features_html(self) -> str:
        items = []
        for feature in self.data.key_features:
            items.append(f"<li>{feature}</li>")
        return "\n".join(items)

    def _generate_org_card(self, org: OrganizationData) -> str:
        acceptability_class = org.acceptability.lower()
        need_badge = self._get_need_badge(org.need_level)

        return f"""
        <div class="org-card {acceptability_class}" data-notes="{org.notes}">
            <div class="name">{org.name}</div>
            <div class="role">{org.role}</div>
            <div class="badges">
                {need_badge}
                <span class="badge badge-gray">{org.requester}</span>
            </div>
        </div>
        """

    def _get_need_badge(self, need_level: str) -> str:
        badges = {
            'Critical': '<span class="badge badge-red">Critical</span>',
            'Important': '<span class="badge badge-yellow">Important</span>',
            'Secondary': '<span class="badge badge-blue">Secondary</span>',
            'None': ''
        }
        return badges.get(need_level, '')

    def _generate_value_chain_html(self) -> str:
        sections = [
            ("Enablers & Influencers", self.data.enablers_influencers),
            ("Products & Solutions", self.data.products_solutions),
            ("Channels & Partners", self.data.channels_partners),
            ("Buyers", self.data.buyers),
            ("End Users", self.data.end_users)
        ]

        columns = []
        for title, orgs in sections:
            cards = "\n".join(self._generate_org_card(org) for org in orgs)
            columns.append(f"""
            <div class="chain-column">
                <h3>{title}</h3>
                {cards if cards else '<p style="text-align:center;color:#6c757d;font-size:0.75rem;">No organizations</p>'}
            </div>
            """)

        return "\n".join(columns)

    def _generate_detail_tables_html(self) -> str:
        sections = [
            ("Section 3: Enablers & Influencers", self.data.enablers_influencers,
             "Organizations that provide infrastructure, funding, regulation, standards, or expertise."),
            ("Section 4: Products & Solutions", self.data.products_solutions,
             "Organizations that produce complementary or substitute products/solutions."),
            ("Section 5: Channels & Partners", self.data.channels_partners,
             "Organizations that facilitate distribution, adoption, or implementation."),
            ("Section 6: Buyers", self.data.buyers,
             "Organizations or entities that pay for your solution."),
            ("Section 7: End Users", self.data.end_users,
             "Individual people or departments who directly use your innovation.")
        ]

        tables = []
        for title, orgs, description in sections:
            if not orgs:
                continue

            rows = []
            for org in orgs:
                dot_class = f"dot-{org.acceptability_emoji}"
                rows.append(f"""
                <tr>
                    <td>{org.name}</td>
                    <td>{org.role}</td>
                    <td>{org.requester}</td>
                    <td><span class="acceptability-dot {dot_class}"></span>{org.acceptability.title()}</td>
                    <td>{org.need_level}</td>
                    <td>{org.notes}</td>
                </tr>
                """)

            tables.append(f"""
            <div class="card">
                <h2>{title}</h2>
                <p><em>{description}</em></p>
                <table>
                    <thead>
                        <tr>
                            <th>Organization</th>
                            <th>Role</th>
                            <th>Requester</th>
                            <th>Acceptability</th>
                            <th>Need Level</th>
                            <th>Notes</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(rows)}
                    </tbody>
                </table>
            </div>
            """)

        return "\n".join(tables)


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

        input_path = Path(input_path)
        if input_path.suffix in ['.yaml', '.yml']:
            with open(input_path) as f:
                raw_data = yaml.safe_load(f)
        elif input_path.suffix == '.json':
            with open(input_path) as f:
                raw_data = json.load(f)
        else:
            raise ValueError(f"Unsupported input format: {input_path.suffix}")

        # Parse organizations
        def parse_orgs(key):
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
