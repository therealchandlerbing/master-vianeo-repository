#!/usr/bin/env python3
"""
VIANEO DOCX to Markdown Converter
=================================

Converts DOCX documents to Markdown format for version control.

Usage:
    python docx_to_md.py --input document.docx --output document.md
"""

import argparse
import re
from pathlib import Path
from typing import Dict, Any, Optional, List

try:
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))


# =============================================================================
# CONVERTER CLASS
# =============================================================================

class DocxToMarkdownConverter:
    """Converts DOCX to Markdown format."""

    def __init__(self):
        self.output_lines = []

    def convert(self, input_path: Path) -> str:
        """
        Convert DOCX to Markdown.

        Args:
            input_path: Path to DOCX file

        Returns:
            Markdown content as string
        """
        if not DOCX_AVAILABLE:
            raise ImportError("python-docx not installed")

        doc = Document(str(input_path))
        self.output_lines = []

        for element in doc.element.body:
            if element.tag.endswith('p'):
                # Paragraph
                para = Paragraph(element, doc)
                self._process_paragraph(para)
            elif element.tag.endswith('tbl'):
                # Table
                table = Table(element, doc)
                self._process_table(table)

        return '\n'.join(self.output_lines)

    def _process_paragraph(self, para: Paragraph) -> None:
        """Process a paragraph element."""
        style_name = para.style.name if para.style else ''
        text = self._get_paragraph_text(para)

        if not text.strip():
            self.output_lines.append('')
            return

        # Handle headings
        if style_name.startswith('Heading'):
            level = self._get_heading_level(style_name)
            self.output_lines.append(f"{'#' * level} {text}")
            self.output_lines.append('')

        # Handle list items
        elif style_name == 'List Number':
            self.output_lines.append(f"1. {text}")

        elif style_name == 'List Bullet':
            self.output_lines.append(f"- {text}")

        # Regular paragraph
        else:
            self.output_lines.append(text)
            self.output_lines.append('')

    def _get_paragraph_text(self, para: Paragraph) -> str:
        """Extract text with inline formatting from paragraph."""
        parts = []

        for run in para.runs:
            text = run.text
            if not text:
                continue

            # Apply formatting
            if run.bold and run.italic:
                text = f"***{text}***"
            elif run.bold:
                text = f"**{text}**"
            elif run.italic:
                text = f"*{text}*"

            # Monospace font -> code
            if run.font.name and 'Consolas' in run.font.name:
                text = f"`{text.strip('*')}`"

            parts.append(text)

        return ''.join(parts)

    def _get_heading_level(self, style_name: str) -> int:
        """Extract heading level from style name."""
        match = re.search(r'Heading\s*(\d)', style_name)
        if match:
            return int(match.group(1))
        if 'Title' in style_name:
            return 1
        return 2

    def _process_table(self, table: Table) -> None:
        """Process a table element."""
        if not table.rows:
            return

        # Extract data
        rows_data = []
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                cell_text = cell.text.strip().replace('\n', ' ')
                row_data.append(cell_text)
            rows_data.append(row_data)

        if not rows_data:
            return

        # Determine column widths
        col_count = len(rows_data[0])

        # Header row
        header = '| ' + ' | '.join(rows_data[0]) + ' |'
        self.output_lines.append(header)

        # Separator
        separator = '|' + '|'.join(['---' for _ in range(col_count)]) + '|'
        self.output_lines.append(separator)

        # Data rows
        for row in rows_data[1:]:
            # Pad row if needed
            while len(row) < col_count:
                row.append('')
            line = '| ' + ' | '.join(row[:col_count]) + ' |'
            self.output_lines.append(line)

        self.output_lines.append('')

    def save(self, output_path: Path) -> None:
        """Save converted content to file."""
        content = '\n'.join(self.output_lines)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def convert_docx_to_md(
    input_path: Path,
    output_path: Optional[Path] = None
) -> Optional[Path]:
    """
    Convert DOCX file to Markdown.

    Args:
        input_path: Path to input DOCX file
        output_path: Path for output MD (default: same name with .md)

    Returns:
        Output path if successful, None otherwise
    """
    input_path = Path(input_path)

    if output_path is None:
        output_path = input_path.with_suffix('.md')

    try:
        converter = DocxToMarkdownConverter()
        markdown = converter.convert(input_path)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"Converted: {input_path} -> {output_path}")
        return output_path

    except Exception as e:
        print(f"Error: {e}")
        return None


# =============================================================================
# CLI
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Convert DOCX to Markdown"
    )
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input DOCX file'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output Markdown file'
    )

    args = parser.parse_args()

    result = convert_docx_to_md(args.input, args.output)
    if result:
        print(f"Success: {result}")
        return 0
    else:
        print("Conversion failed")
        return 1


if __name__ == '__main__':
    exit(main())
