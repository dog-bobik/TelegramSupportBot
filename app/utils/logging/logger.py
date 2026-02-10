"""
Custom application logger enforcing level semantics.
"""

import logging
from logging import Logger


class AppLogger:
    """
    Application logger with strict level behavior.
    """

    def __init__(self, name: str) -> None:
        self._logger: Logger = logging.getLogger(name=name)

    def info(self, message: str, **_: any) -> None:
        """Log high-level application event."""
        self._logger.info(msg=message)

    def debug(self, message: str, **kwargs: any) -> None:
        """Log diagnostic debug information."""
        self._logger.debug(msg=message, extra={"kwargs": kwargs})

    def warning(self, message: str, **kwargs: any) -> None:
        """Log recoverable anomaly."""
        self._logger.warning(msg=message, extra={"kwargs": kwargs})

    def error(self, message: str, **kwargs: any) -> None:
        """Log error with diagnostic context."""
        self._logger.error(msg=message, extra={"kwargs": kwargs})
