"""
VIANEO Framework Constants
==========================

Central repository of all constants, limits, and configuration values
used across the VIANEO Framework tools.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Tuple

# =============================================================================
# CHARACTER LIMITS
# =============================================================================

class CharacterLimits:
    """Character limits enforced across VIANEO deliverables."""

    # Step 0: Executive Brief
    B1_PROJECT_NAME_TAGLINE = 150  # Combined total
    B2_PROBLEM_STATEMENT = 300
    B3_SOLUTION_OVERVIEW = 300
    B4_MARKET_DESCRIPTION = 300
    B5_REVENUE_MODEL = 300
    B6_TRACTION_STATUS = 300
    B7_TEAM_OVERVIEW = 200  # Note: shorter than others

    # Step 5-11: Needs and Activities
    NEED_STATEMENT = 60      # Short form for matrices
    NEED_BULLET = 60         # Tasks, Pains, Expectations
    MEANS_STATEMENT = 60     # Legitimacy means
    NOTES_FIELD = 250        # Strategic notes in tables

    # Step 6: Personas
    PERSONA_TASK = 60
    PERSONA_PAIN = 60
    PERSONA_EXPECTATION = 60

    # Step 9: Value Network
    ORGANIZATION_NAME = 60
    ROLE_DESCRIPTION = 100
    STRATEGIC_NOTE = 250


# =============================================================================
# SCORE THRESHOLDS
# =============================================================================

class ScoreThresholds:
    """VIANEO dimension scoring thresholds."""

    # Minimum viable scores for each dimension
    LEGITIMACY_MIN = 3.0
    DESIRABILITY_MIN = 3.0
    ACCEPTABILITY_MIN = 3.0
    FEASIBILITY_MIN = 3.0
    VIABILITY_MIN = 3.0

    # Recommended minimums for investment consideration
    INVESTMENT_READY_MIN = 3.5

    # Score ranges for status keywords
    STRONG = (4.5, 5.0)
    PROMISING = (3.5, 4.49)
    DEVELOPING = (3.0, 3.49)
    PROBLEMATIC = (2.0, 2.99)
    NON_VIABLE = (0.0, 1.99)

    @classmethod
    def get_status_keyword(cls, score: float) -> str:
        """Return status keyword for a given score."""
        if score >= 4.5:
            return "Strong"
        elif score >= 3.5:
            return "Promising"
        elif score >= 3.0:
            return "Developing"
        elif score >= 2.0:
            return "Problematic"
        else:
            return "Non-viable"

    @classmethod
    def get_color_code(cls, score: float) -> str:
        """Return color code for score visualization."""
        if score >= 3.5:
            return "#D4EDDA"  # Green
        elif score >= 3.0:
            return "#FFF3CD"  # Yellow
        else:
            return "#F8D7DA"  # Red


# =============================================================================
# MATURITY STAGES
# =============================================================================

class MaturityStage(Enum):
    """Project maturity stage classifications."""

    IDEA = "IDEA"
    PROTOTYPE = "PROTOTYPE"
    PILOT = "PILOT"
    EARLY_COMMERCIALIZATION = "EARLY_COMMERCIALIZATION"
    GROWTH = "GROWTH"

    @classmethod
    def from_string(cls, value: str) -> 'MaturityStage':
        """Parse maturity stage from string."""
        normalized = value.upper().replace(" ", "_").replace("-", "_")
        for stage in cls:
            if stage.value == normalized:
                return stage
        raise ValueError(f"Unknown maturity stage: {value}")


# =============================================================================
# TECHNOLOGY READINESS LEVELS
# =============================================================================

class TechnologyReadinessLevel:
    """NASA TRL scale adapted for startup assessment."""

    TRL_DESCRIPTIONS = {
        1: "Basic principles observed",
        2: "Technology concept formulated",
        3: "Experimental proof of concept",
        4: "Technology validated in lab",
        5: "Technology validated in relevant environment",
        6: "Technology demonstrated in relevant environment",
        7: "System prototype demonstrated in operational environment",
        8: "System complete and qualified",
        9: "Actual system proven in operational environment"
    }

    # TRL to Maturity Stage mapping
    STAGE_MAPPING = {
        MaturityStage.IDEA: (1, 3),
        MaturityStage.PROTOTYPE: (4, 6),
        MaturityStage.PILOT: (6, 7),
        MaturityStage.EARLY_COMMERCIALIZATION: (7, 8),
        MaturityStage.GROWTH: (8, 9)
    }


# =============================================================================
# EVIDENCE QUALITY RATINGS
# =============================================================================

class EvidenceQuality(Enum):
    """Evidence quality rating scale."""

    GOLD_STANDARD = 5    # Published research, audited financials, signed contracts
    STRONG = 4           # Multiple testimonials, verified metrics
    MODERATE = 3         # Single-source testimonials, founder-reported
    WEAK = 2             # Anecdotal evidence, unverified claims
    VERY_WEAK = 1        # No supporting evidence

    @property
    def description(self) -> str:
        """Get description for this quality level."""
        descriptions = {
            5: "Gold Standard: Published research, audited financials, signed contracts",
            4: "Strong: Multiple testimonials, verified metrics",
            3: "Moderate: Single-source testimonials, founder-reported",
            2: "Weak: Anecdotal evidence, unverified claims",
            1: "Very Weak: No supporting evidence"
        }
        return descriptions[self.value]


# =============================================================================
# DIMENSION DEFINITIONS
# =============================================================================

VIANEO_DIMENSIONS = {
    "legitimacy": {
        "name": "Legitimacy",
        "weight": 0.20,
        "description": "Real problem, genuine solution, capable team",
        "min_score": 3.0
    },
    "desirability": {
        "name": "Desirability",
        "weight": 0.25,
        "description": "Customer want, validated need, market demand",
        "min_score": 3.0
    },
    "acceptability": {
        "name": "Acceptability",
        "weight": 0.20,
        "description": "Ecosystem support, stakeholder alignment, external validation",
        "min_score": 3.0
    },
    "feasibility": {
        "name": "Feasibility",
        "weight": 0.15,
        "description": "Technical capability, operational capacity, execution ability",
        "min_score": 3.0
    },
    "viability": {
        "name": "Viability",
        "weight": 0.20,
        "description": "Business model sustainability, financial health, scalability",
        "min_score": 3.0
    }
}


# =============================================================================
# DOCX STYLING CONSTANTS
# =============================================================================

@dataclass
class DocxStyles:
    """Professional DOCX styling constants."""

    # Colors (hex without #)
    PRIMARY_BLUE: str = "1B365D"
    MEDIUM_GRAY: str = "4A4A4A"
    BODY_GRAY: str = "2D2D2D"
    LIGHT_GRAY: str = "757575"
    TABLE_BORDER: str = "CCCCCC"
    TABLE_HEADER_BG: str = "E8EDF2"
    GREEN_HIGHLIGHT: str = "D4EDDA"
    YELLOW_HIGHLIGHT: str = "FFF3CD"
    RED_HIGHLIGHT: str = "F8D7DA"

    # Font sizes (in points)
    TITLE_SIZE: int = 24
    HEADING1_SIZE: int = 16
    HEADING2_SIZE: int = 14
    BODY_SIZE: int = 11
    METADATA_SIZE: int = 9

    # Font family
    FONT_FAMILY: str = "Calibri"

    # Spacing (in DXA: 1440 = 1 inch)
    MARGIN_INCH: int = 1440
    TITLE_AFTER: int = 240
    H1_BEFORE: int = 360
    H1_AFTER: int = 180
    H2_BEFORE: int = 240
    H2_AFTER: int = 120
    BODY_AFTER: int = 240
    LINE_HEIGHT: int = 360  # 1.6x


# =============================================================================
# VALIDATION PATTERNS
# =============================================================================

class ValidationPatterns:
    """Regex patterns for data validation."""

    # Date formats
    ISO_DATE = r"^\d{4}-\d{2}-\d{2}$"

    # Executive Brief ID
    BRIEF_ID = r"^EB-\d{4}-\d{3}$"

    # Evidence ID
    EVIDENCE_ID = r"^E\d{3}$"

    # Score format
    SCORE_FORMAT = r"^\d\.\d/5$"

    # Acceptability emoji
    ACCEPTABILITY_EMOJI = r"^[🟢🟡🔴]$"

    # Need level
    NEED_LEVEL = r"^(Critical|Important|Secondary|None)$"


# =============================================================================
# STEP DEPENDENCIES
# =============================================================================

STEP_DEPENDENCIES = {
    "step_7": ["step_5"],  # Needs Qualification requires Needs/Requesters
    "step_9": ["step_5", "step_8"],  # Value Network requires Requesters + Players
    "step_11_needs": ["step_5", "step_7"],  # Features/Needs view
    "step_11_means": ["step_4"],  # Features/Means view
}


# =============================================================================
# FILE NAMING CONVENTIONS
# =============================================================================

class FileNaming:
    """File naming conventions for VIANEO deliverables."""

    # Executive Brief
    EXECUTIVE_BRIEF_MD = "Executive_Brief_{project_name}_{date}.md"
    EXECUTIVE_BRIEF_DOCX = "Executive_Brief_{project_name}_{date}.docx"

    # Personas
    PERSONAS_MD = "{company_name}_Personas_{date}.md"
    PERSONAS_DOCX = "{company_name}_Vianeo_Personas_{date}.docx"

    # Value Network
    VALUE_NETWORK_MD = "{project_name}_{date}_09_Value_Network.md"
    VALUE_NETWORK_HTML = "{project_name}_{date}_09_Value_Network.html"

    # Diagnostic
    DIAGNOSTIC_MD = "{project_name}_Vianeo_Diagnostic_Comment.md"
    DIAGNOSTIC_DOCX = "{project_name}_Vianeo_Diagnostic_Comment.docx"
