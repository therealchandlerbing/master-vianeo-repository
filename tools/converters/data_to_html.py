#!/usr/bin/env python3
"""
VIANEO Data to HTML Converter
=============================

Converts JSON/CSV/YAML data to interactive HTML dashboards and visualizations.

Supports:
- Dimension score heatmaps
- Needs qualification matrices
- Evidence quality charts
- Value network diagrams

Usage:
    python data_to_html.py --input data.yaml --type scores --output dashboard.html
"""

import argparse
import json
import csv
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.constants import ScoreThresholds, VIANEO_DIMENSIONS
from core.utils import format_date


# =============================================================================
# HTML TEMPLATES
# =============================================================================

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --primary: #1B365D;
            --secondary: #2E5C8A;
            --success: #28a745;
            --warning: #ffc107;
            --danger: #dc3545;
            --light: #f8f9fa;
            --gray: #6c757d;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', Calibri, sans-serif;
            line-height: 1.6;
            color: #333;
            background: var(--light);
            padding: 2rem;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: var(--primary); margin-bottom: 1rem; }}
        h2 {{ color: var(--secondary); margin: 1.5rem 0 1rem; }}
        .card {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }}
        .grid {{ display: grid; gap: 1rem; }}
        .grid-2 {{ grid-template-columns: repeat(2, 1fr); }}
        .grid-3 {{ grid-template-columns: repeat(3, 1fr); }}
        .grid-5 {{ grid-template-columns: repeat(5, 1fr); }}
        @media (max-width: 768px) {{
            .grid-2, .grid-3, .grid-5 {{ grid-template-columns: 1fr; }}
        }}
        .score-card {{
            text-align: center;
            padding: 1.5rem;
            border-radius: 8px;
            transition: transform 0.2s;
        }}
        .score-card:hover {{ transform: translateY(-2px); }}
        .score-card .value {{ font-size: 2.5rem; font-weight: bold; }}
        .score-card .label {{ font-size: 0.875rem; color: var(--gray); margin-top: 0.5rem; }}
        .score-card .status {{ font-size: 0.75rem; margin-top: 0.25rem; font-weight: 600; }}
        .score-green {{ background: #d4edda; color: #155724; }}
        .score-yellow {{ background: #fff3cd; color: #856404; }}
        .score-red {{ background: #f8d7da; color: #721c24; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }}
        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{ background: var(--light); font-weight: 600; color: var(--primary); }}
        tr:hover {{ background: #f5f5f5; }}
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .badge-green {{ background: #d4edda; color: #155724; }}
        .badge-yellow {{ background: #fff3cd; color: #856404; }}
        .badge-red {{ background: #f8d7da; color: #721c24; }}
        .progress-bar {{
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s;
        }}
        .meta {{ color: var(--gray); font-size: 0.875rem; margin-bottom: 1rem; }}
        footer {{ text-align: center; padding: 2rem; color: var(--gray); font-size: 0.875rem; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <p class="meta">Generated: {generated_date}</p>
        {content}
        <footer>VIANEO Framework v2.0</footer>
    </div>
</body>
</html>
"""

SCORE_CARD_TEMPLATE = """
<div class="score-card {score_class}">
    <div class="value">{score:.1f}</div>
    <div class="label">{dimension}</div>
    <div class="status">{status}</div>
</div>
"""


# =============================================================================
# CONVERTER CLASS
# =============================================================================

class DataToHtmlConverter:
    """Converts data to interactive HTML dashboards."""

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def generate_scores_dashboard(self) -> str:
        """Generate dimension scores dashboard."""
        scores = self.data.get('dimension_scores', self.data.get('scores', {}))

        # Build score cards
        cards_html = []
        for dim_key, dim_info in VIANEO_DIMENSIONS.items():
            score = 0.0
            if dim_key in scores:
                score = float(scores[dim_key])
            elif dim_info['name'] in scores:
                score = float(scores[dim_info['name']])
            elif 'dimension_scores' in self.data:
                for d in self.data['dimension_scores']:
                    if d.get('name', '').lower() == dim_key:
                        score = float(d.get('score', 0))
                        break

            status = ScoreThresholds.get_status_keyword(score)
            score_class = self._get_score_class(score)

            cards_html.append(SCORE_CARD_TEMPLATE.format(
                score=score,
                dimension=dim_info['name'],
                status=status,
                score_class=score_class
            ))

        # Calculate overall
        all_scores = []
        for dim_key in VIANEO_DIMENSIONS.keys():
            if dim_key in scores:
                all_scores.append(float(scores[dim_key]))

        overall = sum(all_scores) / len(all_scores) if all_scores else 0
        overall_status = ScoreThresholds.get_status_keyword(overall)

        content = f"""
        <div class="card">
            <h2>Dimension Scores</h2>
            <div class="grid grid-5">
                {''.join(cards_html)}
            </div>
        </div>
        <div class="card">
            <h2>Overall Assessment</h2>
            <div class="score-card {self._get_score_class(overall)}" style="max-width: 200px; margin: 0 auto;">
                <div class="value">{overall:.2f}</div>
                <div class="label">Overall Score</div>
                <div class="status">{overall_status}</div>
            </div>
        </div>
        """

        return self._wrap_html("VIANEO Dimension Scores", content)

    def generate_evidence_dashboard(self) -> str:
        """Generate evidence quality dashboard."""
        evidence = self.data.get('evidence_log', [])

        # Count by quality
        quality_counts = {i: 0 for i in range(1, 6)}
        section_counts = {}

        for e in evidence:
            q = e.get('quality_rating', 1)
            quality_counts[q] = quality_counts.get(q, 0) + 1

            s = e.get('section', 'Unknown')
            section_counts[s] = section_counts.get(s, 0) + 1

        # Quality distribution
        quality_html = ""
        for q in range(5, 0, -1):
            count = quality_counts.get(q, 0)
            pct = (count / len(evidence) * 100) if evidence else 0
            color = "#28a745" if q >= 4 else "#ffc107" if q >= 3 else "#dc3545"
            quality_html += f"""
            <div style="margin-bottom: 0.5rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                    <span>Quality {q}</span>
                    <span>{count} ({pct:.0f}%)</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {pct}%; background: {color};"></div>
                </div>
            </div>
            """

        # Evidence table
        table_rows = ""
        for e in evidence:
            q = e.get('quality_rating', 1)
            badge_class = "badge-green" if q >= 4 else "badge-yellow" if q >= 3 else "badge-red"
            table_rows += f"""
            <tr>
                <td>{e.get('id', '')}</td>
                <td>{e.get('section', '')}</td>
                <td>{e.get('source_type', '')}</td>
                <td><span class="badge {badge_class}">{q}/5</span></td>
                <td>{e.get('description', '')[:100]}</td>
                <td>{e.get('date', '')}</td>
            </tr>
            """

        content = f"""
        <div class="card">
            <h2>Evidence Quality Distribution</h2>
            {quality_html}
            <p style="margin-top: 1rem; color: var(--gray);">
                Total: {len(evidence)} evidence entries
            </p>
        </div>
        <div class="card">
            <h2>Evidence Log</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Section</th>
                        <th>Source Type</th>
                        <th>Quality</th>
                        <th>Description</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        """

        return self._wrap_html("VIANEO Evidence Dashboard", content)

    def generate_needs_matrix(self) -> str:
        """Generate needs qualification matrix visualization."""
        needs = self.data.get('needs', [])
        requesters = self.data.get('requesters', [])

        if not needs or not requesters:
            return self._wrap_html("Needs Matrix", "<p>No needs data available</p>")

        # Build matrix header
        header = "<th>Need</th>"
        for r in requesters:
            name = r if isinstance(r, str) else r.get('name', '')
            header += f"<th>{name}</th>"

        # Build matrix rows
        rows = ""
        for need in needs:
            need_text = need if isinstance(need, str) else need.get('statement', '')
            row = f"<td>{need_text}</td>"

            for r in requesters:
                # Check for rating data
                rating = ""
                if isinstance(need, dict) and 'ratings' in need:
                    r_name = r if isinstance(r, str) else r.get('name', '')
                    rating = need['ratings'].get(r_name, '')

                if rating:
                    badge_class = "badge-green" if rating == "High" else "badge-yellow"
                    row += f"<td><span class='badge {badge_class}'>{rating}</span></td>"
                else:
                    row += "<td>-</td>"

            rows += f"<tr>{row}</tr>"

        content = f"""
        <div class="card">
            <h2>Needs Qualification Matrix</h2>
            <table>
                <thead><tr>{header}</tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
        """

        return self._wrap_html("VIANEO Needs Matrix", content)

    def generate_generic_table(self) -> str:
        """Generate generic table from data."""
        # Try to find tabular data
        table_data = None
        for key in ['data', 'items', 'rows', 'records']:
            if key in self.data and isinstance(self.data[key], list):
                table_data = self.data[key]
                break

        if not table_data:
            table_data = [self.data] if isinstance(self.data, dict) else self.data

        if not table_data or not isinstance(table_data[0], dict):
            return self._wrap_html("Data Table", "<p>No tabular data found</p>")

        # Get columns
        columns = list(table_data[0].keys())

        # Build table
        header = "".join(f"<th>{col}</th>" for col in columns)
        rows = ""
        for item in table_data:
            row = "".join(f"<td>{item.get(col, '')}</td>" for col in columns)
            rows += f"<tr>{row}</tr>"

        content = f"""
        <div class="card">
            <h2>Data Table</h2>
            <table>
                <thead><tr>{header}</tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
        """

        return self._wrap_html("VIANEO Data", content)

    def _get_score_class(self, score: float) -> str:
        """Get CSS class for score value."""
        if score >= 3.5:
            return "score-green"
        elif score >= 3.0:
            return "score-yellow"
        else:
            return "score-red"

    def _wrap_html(self, title: str, content: str) -> str:
        """Wrap content in base HTML template."""
        return BASE_TEMPLATE.format(
            title=title,
            generated_date=format_date(),
            content=content
        )


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def convert_data_to_html(
    input_path: Path,
    output_path: Optional[Path] = None,
    visualization_type: str = 'auto'
) -> Optional[Path]:
    """
    Convert data file to HTML dashboard.

    Args:
        input_path: Path to input data file (JSON/YAML/CSV)
        output_path: Path for output HTML
        visualization_type: 'scores', 'evidence', 'needs', 'table', or 'auto'

    Returns:
        Output path if successful
    """
    input_path = Path(input_path)

    if output_path is None:
        output_path = input_path.with_suffix('.html')

    # Load data
    if input_path.suffix in ['.yaml', '.yml']:
        with open(input_path) as f:
            data = yaml.safe_load(f)
    elif input_path.suffix == '.json':
        with open(input_path) as f:
            data = json.load(f)
    elif input_path.suffix == '.csv':
        with open(input_path, newline='') as f:
            reader = csv.DictReader(f)
            data = {'data': list(reader)}
    else:
        print(f"Unsupported file type: {input_path.suffix}")
        return None

    # Create converter
    converter = DataToHtmlConverter(data)

    # Auto-detect type
    if visualization_type == 'auto':
        if 'dimension_scores' in data or 'scores' in data:
            visualization_type = 'scores'
        elif 'evidence_log' in data:
            visualization_type = 'evidence'
        elif 'needs' in data and 'requesters' in data:
            visualization_type = 'needs'
        else:
            visualization_type = 'table'

    # Generate HTML
    if visualization_type == 'scores':
        html = converter.generate_scores_dashboard()
    elif visualization_type == 'evidence':
        html = converter.generate_evidence_dashboard()
    elif visualization_type == 'needs':
        html = converter.generate_needs_matrix()
    else:
        html = converter.generate_generic_table()

    # Save
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated: {output_path}")
    return output_path


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Convert data to HTML dashboard"
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input data file (JSON/YAML/CSV)'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output HTML file'
    )
    parser.add_argument(
        '--type', '-t',
        choices=['scores', 'evidence', 'needs', 'table', 'auto'],
        default='auto',
        help='Visualization type'
    )

    args = parser.parse_args()

    result = convert_data_to_html(args.input, args.output, args.type)
    if result:
        print(f"Success: {result}")
        return 0
    else:
        print("Conversion failed")
        return 1


if __name__ == '__main__':
    exit(main())
