"""
Clean
-----

This module provides various methods for cleaning up the scraped data.
"""

# Standard Library ---------------------------------------------------------------------
import itertools
import re
import string

# Third Party --------------------------------------------------------------------------
from fuzzywuzzy import fuzz

# Data Science
import pandas as pd


def drop_duplicate_songs(
    df: pd.DataFrame, fuzzy_score_threshold: int = 85
) -> pd.DataFrame:
    """Drop duplicate songs with manual filtering and fuzzy_wuzzy comparison.

    Parameters
    ----------
    df
        Songs dataframe.
    fuzzy_score_threshold
        Fuzzy score threshold.

    Returns
    -------
    :code:`pd.DataFrame`
        Songs Dataframe with removed duplicates.
    """
    # Manual title uniformization
    df["uniformized_song_title"] = df["song_title"].transform(uniformize_song_title)
    df.drop_duplicates(subset=["artist", "uniformized_song_title"], inplace=True)

    # Fuzzy wuzzy matching
    df["fuzzy_score"] = 0
    df = df.groupby("artist").apply(compute_fuzzy_score)
    df.drop(df[df["fuzzy_score"] > fuzzy_score_threshold].index, inplace=True)

    # Clean up
    df.drop(["uniformized_song_title", "fuzzy_score"], axis=1, inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df


def uniformize_song_title(song_title: str) -> str:
    """Apply basic manual title uniformization transformations.

    .. note::
        This function is meant to be used in conjunction with
        :meth:`fuzzy_score` and can serve for a rough first filtering
        step.

    Parameters
    ----------
    song_title
        Song title.

    Returns
    -------
    :code:`str`
        Uniformized song title.
    """
    # Make everything lower case:
    uniformized_song_title = song_title.lower()
    # Remove bracket/brace content from the end of titles:
    uniformized_song_title = re.sub(
        r"((\s*\[[^]]*\])|(\s*\([^)]*\)))+$", "", uniformized_song_title
    )
    # Remove punctuation:
    uniformized_song_title = uniformized_song_title.translate(
        str.maketrans("", "", string.punctuation)
    )
    # Strip white-space:
    uniformized_song_title = uniformized_song_title.strip()

    return uniformized_song_title


def compute_fuzzy_score(df: pd.DataFrame) -> pd.DataFrame:
    """Perform pairwise comparisons and save maximum fuzzy score.

    .. note::
        This function is meant to be used in conjunction with
        :meth:`uniformize_song_title` and can serve for a a second more
        precise filtering step.

    Parameters
    ----------
    df
        Songs dataframe with a "uniformized_song_title" column and a
        zero-filled "fuzzy_score" column.

    Returns
    -------
    :code:`pd.DataFrame`
        Dataframe with computed "fuzzy_score".

    References
    ----------
    .. _fuzzy_wuzzy: https://github.com/seatgeek/fuzzywuzzy
    """
    for (idx1, song_title1), (idx2, song_title2) in itertools.combinations(
        df["uniformized_song_title"].items(), 2
    ):
        df.loc[idx1, "fuzzy_score"] = max(
            df.loc[idx1, "fuzzy_score"], fuzz.ratio(song_title1, song_title2)
        )
    return df
