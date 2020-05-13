"""
Logger
======

This module contains logging utilities.
"""
# Standard Library ---------------------------------------------------------------------
import os
from enum import Enum
from typing import List

# Third Party --------------------------------------------------------------------------
from colorama import Back, Fore, Style, init
from dotenv import load_dotenv


init()
load_dotenv()


class LogLevel(Enum):
    """Log level enum."""

    INFO = 0
    WARNING = 1
    ERROR = 2


LOG_LEVEL_TO_COLOR_MAP = {
    LogLevel.INFO: Fore.CYAN,
    LogLevel.WARNING: Fore.YELLOW,
    LogLevel.ERROR: Fore.RED,
}
LOG_LEVEL_TO_ICON_MAP = {
    LogLevel.INFO: "✅",
    LogLevel.WARNING: "⚠️",
    LogLevel.ERROR: "❌",
}
LOG_LEVEL_TO_ICON_LENGTH_ADJUSTMENT = {
    LogLevel.INFO: 1,
    LogLevel.WARNING: 0,
    LogLevel.ERROR: 1,
}

PRINT_WIDTH = int(os.getenv("PRINT_WIDTH"))


def print_table(title: str, entries: List[List[str]] = ()) -> None:
    """Print a table with two columns.

    Parameters
    ----------
    title
    entries

    Returns
    -------
    """
    print()
    print(Back.LIGHTBLACK_EX, end="")
    print(f" {title} ".center(PRINT_WIDTH, "="), end="")
    print(Style.RESET_ALL)
    print_table_entries(entries)


def print_table_entries(entries: List[List[str]]) -> None:
    """Print table entries.

    Parameters
    ----------
    entries
        Table entries.

    Returns
    -------
    :code:`None`
    """
    for (i, (key, value, log_level)) in enumerate(entries):
        print_table_entry(key, value, log_level)


def print_table_entry(key, value, log_level) -> None:
    """Print table entry.

    Parameters
    ----------
    key
        Key.
    value
        Value.
    log_level
        Log level.

    Returns
    -------
    :code:`None`
    """
    print(Fore.MAGENTA + key.ljust(int(PRINT_WIDTH / 2)) + Style.RESET_ALL, end="")
    print(
        LOG_LEVEL_TO_COLOR_MAP[log_level]
        + (LOG_LEVEL_TO_ICON_MAP[log_level] + " " + value).rjust(
            int(PRINT_WIDTH / 2 - LOG_LEVEL_TO_ICON_LENGTH_ADJUSTMENT[log_level])
        )
        + Style.RESET_ALL
    )
