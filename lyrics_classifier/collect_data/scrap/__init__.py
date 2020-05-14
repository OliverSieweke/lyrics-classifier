"""
Scrap
=====

This module provides various methods for retrieving artist and song HTML
pages.

.. note::
    The functionality specific to `lyrics.com` page is contained in
    :mod:`lyrics_com`
"""
# Standard Library ---------------------------------------------------------------------
import csv
import re

# Third Party --------------------------------------------------------------------------
import requests as req

# Project ------------------------------------------------------------------------------
import lyrics_classifier.paths as paths
from lyrics_classifier.collect_data import lyrics_com
from lyrics_classifier.collect_data.process.song import Song
from lyrics_classifier.environment import get_artists
from lyrics_classifier.logger import LogLevel, print_table, print_table_entry


class CommunicationError(Exception):
    """Raised on unsuccessful HTTP requests.

    Unsuccessful is interpreted here as a non `200-299` status code
    response.
    """

    def __init__(self, message: str, status_code: int = None) -> None:
        super().__init__(message)
        self.status_code = status_code


def fetch(url: str) -> str:
    """Fetch URL.

    Parameters
    ----------
    url
        URL.

    Raises
    ------
    :code:`CommunicationError`
        If the HTTP request is unsuccessful.

    Returns
    -------
    :code:`str`
        Body.
    """
    res = req.get(url, allow_redirects=False)
    if re.match(r"^2\d{2}$", str(res.status_code)):
        return res.text
    else:
        raise CommunicationError(
            f"Unexpected error in fetching html page: {url}\n"
            f"\tStatus Code: {res.status_code}\n",
            status_code=res.status_code,
        )


def retrieve_artists_html_pages(force: bool = False) -> None:
    """Retrieve and save artist HTML pages from `lyrics.com`.

    Parameters
    ----------
    force
        Overwrite HTML pages that have already been retrieved.

    Returns
    -------
    :code:`None`
    """
    print_table("ARTISTS HTML PAGES")

    for artist in get_artists():

        artist_html_file_path = paths.artist_html_file_path(artist)

        if artist_html_file_path.exists() and not force:
            print_table_entry(artist, "HTML page already retrieved.", LogLevel.INFO)
        else:
            artist_url = lyrics_com.artist_url(artist)
            try:
                artist_html_page = fetch(artist_url)
                artist_html_file_path.write_text(artist_html_page)
                print_table_entry(
                    artist, "HTML page retrieved and saved.", LogLevel.INFO
                )
            except CommunicationError as err:
                print_table_entry(
                    artist,
                    f"Error in retrieving HTML page [{err.status_code}].",
                    LogLevel.ERROR,
                )


def retrieve_songs_html_pages(force: bool = False) -> None:
    """Retrieve and save song HTML pages from `lyrics.com`.

    Parameters
    ----------
    force
        Overwrite HTML pages that have already been retrieved.

    Returns
    -------
    :code:`None`
    """
    print_table("SONGS HTML PAGES")

    with paths.songs_csv_file_path().open("r") as songs_csv_file:
        reader = csv.DictReader(songs_csv_file)

        for song in map(lambda attributes: Song(**attributes), reader):
            song_html_file_path = paths.song_html_file_path(song)
            if song_html_file_path.exists() and not force:
                print_table_entry(
                    song.song_title, "HTML page already retrieved.", LogLevel.INFO
                )
            else:
                song_url = lyrics_com.song_url(song.song_path)
                try:
                    song_html_page = fetch(song_url)
                    song_html_file_path.write_text(song_html_page)
                    print_table_entry(
                        song.song_title, "HTML page retrieved and saved.", LogLevel.INFO
                    )

                except CommunicationError as err:
                    print_table_entry(
                        song.song_title,
                        f"Error in retrieving HTML page [{err.status_code}].",
                        LogLevel.ERROR,
                    )
