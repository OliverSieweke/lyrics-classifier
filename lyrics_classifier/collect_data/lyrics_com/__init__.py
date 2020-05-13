"""
Lyrics.com
==========

This module provides methods for constructing requests and parsing HTML
pages of the `lyrics.com` site.

.. warning::
    Those methods were designed for the state of the `lyrics.com` site
    in May 2020 and may be subject o change.
"""


# Standard Library ---------------------------------------------------------------------
import re
from typing import List
from urllib import parse

# Third Party --------------------------------------------------------------------------
from bs4 import BeautifulSoup

# Project ------------------------------------------------------------------------------
from lyrics_classifier.collect_data.process.song import Song


LYRICS_COM_SCHEME = "https"
LYRICS_COM_NET_LOC = "www.lyrics.com"
LYRICS_COM_ARTIST_PATH = "artist.php"


def artist_url(artist: str):
    """Return `lyrics.com` URL for the artist's song list page.

    Parameters
    ----------
    artist
        Artist name.

    Returns
    -------
    :code:`str`
        `lyrics.com` URL for the artist's song list page.
    """

    # Query string parameters:
    #   - name: artist name     | white-spaces and '/' need to be replaced with "-"
    #   - o: order              | "1" will request the song list view

    querystring = parse.urlencode({"name": re.sub(r"\s|/", "-", artist), "o": "1"})
    return parse.urlunsplit(
        (
            LYRICS_COM_SCHEME,
            LYRICS_COM_NET_LOC,
            LYRICS_COM_ARTIST_PATH,
            querystring,
            None,
        )
    )


def song_url(song_path: str) -> str:
    """Return `lyrics.com` full URL for the song path.

    Parameters
    ----------
    song_path
        Song path (as retrieved from the artists CSV song list).

    Returns
    -------
    :code:`str`
        `lyrics.com` URL for the song's page.
    """
    return parse.urlunsplit(
        (LYRICS_COM_SCHEME, LYRICS_COM_NET_LOC, song_path, None, None)
    )


def extract_songs_from_artist_html_page(artist: str, html: str) -> List[Song]:
    """Parse artist `lyrics.com` HTML page and extract songs.

    .. note::
        The `lyrics.com` artist page includes a single HTML table
        containing all the songs as table rows.

    Parameters
    ----------
    artist
        Artist name.
    html
        Artist html page.

    Returns
    -------
    :code:`List[Song]`
        List of the artist's songs.
    """
    songs = []

    soup = BeautifulSoup(html, "html.parser")

    # There is a single table containing all the songs:
    song_table = soup.find("table")

    # The first row is a header row and can be ignored
    for row in song_table.findAll("tr")[1:]:
        (song_element, album_element, duration_element) = row.findAll("td")

        # The album column also includes the year (which follows a </br> tag):
        year = getattr(album_element.find("br"), "next_sibling", "")
        # The year can be removed from the album title if applicable:
        album_title = (
            re.sub(fr"{year}$", "", album_element.text) if year else album_element.text
        )

        songs.append(
            Song(
                **{
                    "artist": artist,
                    "song_title": song_element.text,
                    "song_path": song_element.a["href"],
                    "year": year,
                    "album_title": album_title,
                    "album_path": album_element.a and album_element.a["href"],
                    "duration": duration_element.text,
                }
            )
        )

    return songs


def extract_lyrics_from_song_html_page(html: str) -> str:
    """Parse song `lyrics.com` HTML page and extract lyrics.

    Parameters
    ----------
    html
        Song HTML page

    Returns
    -------
    :code:`str`
        Lyrics.
    """
    return BeautifulSoup(html, "html.parser").find(id="lyric-body-text").text
