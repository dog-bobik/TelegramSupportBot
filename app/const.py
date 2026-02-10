from pathlib import Path
from typing import Final

"""
Application-wide constants
"""

ROOT_DIR: Final[Path] = Path(__file__).parent.parent
ENV_FILE: Final[Path] = ROOT_DIR / ".env"
