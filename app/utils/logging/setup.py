"""
Application logging setup.
"""

import logging
from app.utils.logging import LevelAwareFormatter


def _disable_external_logs() -> None:
    for logger_name in ["aiogram", "httpx"]:
        logging.getLogger(logger_name).setLevel(logging.WARNING)


def setup_logging() -> None:
    """
    Initialize application logging
    """
    handler = logging.StreamHandler()
    handler.setFormatter(LevelAwareFormatter())

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(handler)

    _disable_external_logs()
