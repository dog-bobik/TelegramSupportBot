"""
Level-aware logging formatter.
"""

import logging
from logging import Formatter


class LevelAwareFormatter(Formatter):
    """
    Formatter that enforces logging semantics
    """

    BASE_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    DEBUG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s | %(kwargs)s"

    def format(self, record) -> str:
        if record.levelno != logging.INFO and hasattr(record, "kwargs"):
            self._style._fmt = self.DEBUG_FORMAT
        else:
            self._style._fmt = self.BASE_FORMAT

        return super().format(record)
