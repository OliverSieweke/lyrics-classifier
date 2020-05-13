"""
Paths
=====

This module provides utility methods for retrieving various project
paths, mostly concatenated from environment variables.
"""
# Standard Library ---------------------------------------------------------------------
import os
import re
from pathlib import Path

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv

# Project ------------------------------------------------------------------------------
from lyrics_classifier.collect_data.process.song import Song


load_dotenv()


def project_root_path() -> Path:
    """Return absolute project root path.

    Returns
    -------
    :code:`Path`
        Absolute project root path.
    """
    return Path(__file__).resolve().parents[2]


def module_root_path() -> Path:
    """Return absolute module root path.

    Returns
    -------
    :code:`Path`
        Absolute module root path.
    """
    return Path(__file__).resolve().parents[1]


def data_dir_path() -> Path:
    """Return absolute data directory path.

    The directory name is retrieved from the environment variables and
    created if it does not yet exist.

    Returns
    -------
    :code:`Path`
        Absolute data directory path.
    """
    path = project_root_path().joinpath(os.getenv("DATA_DIR"))
    path.mkdir(exist_ok=True)
    return path


def artists_dir_path() -> Path:
    """Return absolute artists directory path.

    The directory name is retrieved from the environment variables and
    created if it does not yet exist.

    Returns
    -------
    :code:`Path`
        Absolute artists directory path.
    """
    path = data_dir_path().joinpath(os.getenv("ARTISTS_DIR"))
    path.mkdir(exist_ok=True)
    return path


def artist_html_file_path(artist) -> Path:  # Used
    """Return absolute artists HTML file path.

    Parameters
    ----------
    artist
        Artist name.

    Returns
    -------
    :cod:`Path`
        Absolute artists HTML file path.
    """
    artist_file_name = re.sub(r"[\s/]", "_", artist)
    return artists_dir_path().joinpath(f"{artist_file_name}.html")


def lyrics_dir_path() -> Path:
    """Return absolute lyrics directory path.

    The directory name is retrieved from the environment variables and
    created if it does not yet exist.

    Returns
    -------
    :code:`Path`
        Absolute lyrics directory path.
    """
    path = data_dir_path().joinpath(os.getenv("LYRICS_DIR"))
    path.mkdir(exist_ok=True)
    return path


def artist_lyrics_dir_path(artist: str) -> Path:
    """Return absolute artist lyrics directory path.

    The directory is created if it does not yet exist.

    Parameters
    ----------
    artist
        Artist name.

    Returns
    -------
    :cod:`Path`
        Absolute artist lyrics directory path.
    """
    artist_dir_name = re.sub(r"[\s/]", "_", artist)
    path = lyrics_dir_path().joinpath(artist_dir_name)
    path.mkdir(exist_ok=True)
    return path


def lyrics_text_file_path(song) -> Path:
    """Return absolute artist lyrics TEXT file path for song.

    Parameters
    ----------
    song
        Song.

    Returns
    -------
    :cod:`Path`
        Absolute artist lyrics TEXT file path for song.
    """
    song_file_name = re.sub(r"[\s/]", "_", song.song_title)
    return artist_lyrics_dir_path(song.artist).joinpath(f"{song_file_name}.txt")


def songs_csv_file_path() -> Path:
    """Return absolute songs CSV file path.

    Returns
    -------
    :code:`Path`
        Songs CSV file path.
    """
    return data_dir_path().joinpath("songs.csv")


def songs_dir_path() -> Path:
    """Return absolute songs directory path.

    The directory name is retrieved from the environment variables and
    created if it does not yet exist.

    Returns
    -------
    :code:`Path`
        Absolute songs directory path.
    """
    path = data_dir_path().joinpath(os.getenv("SONGS_DIR"))
    path.mkdir(exist_ok=True)
    return path


def artist_songs_dir_path(artist: str) -> Path:
    """Return absolute artist songs directory path.

    The directory is created if it does not yet exist.

    Parameters
    ----------
    artist
        Artist name.

    Returns
    -------
    :cod:`Path`
        Absolute artist songs directory path.
    """
    artist_dir_name = re.sub(r"[\s/]", "_", artist)
    path = songs_dir_path().joinpath(artist_dir_name)
    path.mkdir(exist_ok=True)
    return path


def song_html_file_path(song: Song) -> Path:
    """Return absolute artist song HTML file path.

    Parameters
    ----------
    song
        Song.

    Returns
    -------
    :cod:`Path`
        Absolute artist song HTML file path.
    """
    song_file_name = re.sub(r"[\s/]", "_", song.song_title)
    return artist_songs_dir_path(song.artist).joinpath(f"{song_file_name}.html")
