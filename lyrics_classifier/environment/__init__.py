"""
Environment
===========

This module provides utility methods for retrieving environment variables.
"""

# Standard Library ---------------------------------------------------------------------
import os
from typing import List

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv


load_dotenv()


def get_artists() -> List[str]:
    """Return list of artists.

    Returns
    -------
    :code:`List[str]`
        List of artists.
    """
    return os.getenv("ARTISTS").split(",")
