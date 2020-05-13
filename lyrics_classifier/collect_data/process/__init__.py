"""
Process
=======

This module provides methods for processing scraped data.
"""

# Standard Library ---------------------------------------------------------------------
import csv

# Project ------------------------------------------------------------------------------
from lyrics_classifier import paths
from lyrics_classifier.collect_data import lyrics_com
from lyrics_classifier.collect_data.process.song import Song
from lyrics_classifier.environment import get_artists
from lyrics_classifier.logger import LogLevel, print_table, print_table_entry


def artists_html_pages_to_songs_csv() -> None:
    """Convert artist HTML pages to a CSV file containing all the songs.

    .. warning::
        This function will overwrite existing data.

    Returns
    -------
    :code:`None`
    """
    print_table("CSV SONGS")

    fieldnames = vars(Song()).keys()

    with paths.songs_csv_file_path().open("w") as songs_csv_file:
        writer = csv.DictWriter(songs_csv_file, fieldnames=fieldnames).writeheader()

    for artist in get_artists():

        artist_html_file_path = paths.artist_html_file_path(artist)

        if artist_html_file_path.exists():
            songs = lyrics_com.extract_songs_from_artist_html_page(
                artist, artist_html_file_path.read_text()
            )

            with paths.songs_csv_file_path().open("a") as songs_csv_file:
                csv.DictWriter(songs_csv_file, fieldnames=fieldnames).writerows(
                    map(vars, songs)
                )
            print_table_entry(
                artist, "HTML page parsed and songs saved.", LogLevel.INFO
            )
        else:
            print_table_entry(artist, "HTML page not available.", LogLevel.WARNING)


def songs_html_pages_to_lyrics_text() -> None:
    """Convert song HTML pages to text files containing the lyrics.

    Returns
    -------
    :code:`None`
    """
    print_table("TEXT LYRICS")

    fieldnames = vars(Song()).keys()

    with paths.songs_csv_file_path().open("r") as songs_csv_file:
        reader = csv.DictReader(songs_csv_file)

        for song in map(lambda attributes: Song(**attributes), reader):

            song_html_file_path = paths.song_html_file_path(song)

            if song_html_file_path.exists():
                lyrics = lyrics_com.extract_lyrics_from_song_html_page(
                    song_html_file_path.read_text()
                )
                paths.lyrics_text_file_path(song).write_text(lyrics)

                print_table_entry(
                    song.song_title, "HTML page parsed and songs saved.", LogLevel.INFO,
                )
            else:
                print_table_entry(
                    song.song_title, "HTML page not available.", LogLevel.WARNING
                )
