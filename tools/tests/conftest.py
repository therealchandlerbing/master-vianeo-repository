"""
Pytest configuration and shared fixtures for VIANEO tools tests.
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime

# Add tools directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


# =============================================================================
# PATH FIXTURES
# =============================================================================

@pytest.fixture
def fixtures_dir() -> Path:
    """Return path to test fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def temp_output_dir(tmp_path) -> Path:
    """Return temporary directory for test outputs."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


# =============================================================================
# SAMPLE DATA FIXTURES
# =============================================================================

@pytest.fixture
def sample_executive_brief_data() -> dict:
    """Sample Executive Brief data for testing."""
    return {
        "project_name": "TestProject",
        "date_prepared": "2025-01-15",
        "prepared_by": "Test Analyst",
        "brief_id": "EB-2025-001",
        "tagline": "A short tagline for testing",
        "problem_description": "Users struggle with manual data entry.",
        "problem_severity": 4,
        "problem_frequency": "Daily",
        "affected_population": "10,000 office workers",
        "solution_description": "Automated data capture system.",
        "solution_type": "Software",
        "key_features": ["OCR scanning", "Auto-fill", "Validation"],
        "market_description": "Enterprise document management",
        "primary_users": "Data entry clerks",
        "primary_buyers": "IT departments",
        "users_are_buyers": False,
        "tam": "$5B",
        "sam": "$500M",
        "som": "$50M",
        "sizing_method": "Bottom-up",
        "revenue_description": "SaaS subscription model",
        "revenue_streams": ["Monthly subscriptions", "Enterprise licenses"],
        "cac": "$500",
        "ltv": "$5,000",
        "ltv_cac_ratio": "10:1",
        "status_description": "Beta testing with 3 enterprise clients",
        "key_metrics": {"MRR": "$10,000", "Users": "500"},
        "customer_interviews": 25,
        "pilot_users": 100,
        "paying_customers": 3,
        "revenue_to_date": "$30,000",
        "team_overview": "Experienced SaaS team of 5",
        "team_members": [
            {"name": "Jane Doe", "role": "CEO", "experience": "10 years SaaS"}
        ],
        "team_strengths": ["Technical expertise", "Domain knowledge"],
        "maturity_stage": "PILOT",
        "trl": 6,
        "evidence_log": []
    }


@pytest.fixture
def sample_persona_data() -> dict:
    """Sample Persona document data for testing."""
    return {
        "company_name": "TestCorp",
        "project_subtitle": "User Research Phase 1",
        "prepared_date": "January 2025",
        "research_overview": "Conducted 15 interviews across 3 user segments.",
        "critical_gaps": "Need more data on enterprise buyers.",
        "personas": [
            {
                "first_name": "Sarah",
                "age": 35,
                "life_motivations": "Career advancement and work-life balance",
                "personality_values": "Detail-oriented, efficiency-focused",
                "thinks_feels": "Frustrated with repetitive tasks",
                "observes": "Colleagues using outdated tools",
                "does": "Manual data entry 4 hours daily",
                "others_say": "Sarah is the go-to for accuracy",
                "tasks": ["Enter invoice data", "Verify records", "Generate reports"],
                "pains": ["Tedious work", "Error-prone process", "No automation"],
                "expectations": ["Save time", "Reduce errors", "Easy to learn"],
                "current_solutions_description": "Excel and paper forms",
                "current_tools": [
                    {"name": "Excel", "limitation": "Manual and error-prone"}
                ],
                "interview_count": 8,
                "interview_date_range": "Jan 5-15, 2025"
            }
        ]
    }


@pytest.fixture
def sample_dimension_scores() -> dict:
    """Sample dimension scores for testing."""
    return {
        "legitimacy": 3.5,
        "desirability": 4.0,
        "acceptability": 3.2,
        "feasibility": 3.8,
        "viability": 3.0
    }


# =============================================================================
# DATE FIXTURES
# =============================================================================

@pytest.fixture
def fixed_date() -> datetime:
    """Fixed date for consistent testing."""
    return datetime(2025, 1, 15, 10, 30, 0)


# =============================================================================
# TEXT FIXTURES
# =============================================================================

@pytest.fixture
def text_with_special_chars() -> str:
    """Text containing special characters for cleaning tests."""
    return "Test—with em–dash and   extra   spaces"


@pytest.fixture
def markdown_with_formatting() -> str:
    """Markdown text with various formatting."""
    return "**Bold** and *italic* with `code` and [link](http://example.com)"


@pytest.fixture
def sample_markdown_document() -> str:
    """Sample markdown document for parsing tests."""
    return """---
title: Test Document
date: 2025-01-15
---

# Section One

This is the first section content.

## Subsection A

More content here.

# Section Two

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
"""
