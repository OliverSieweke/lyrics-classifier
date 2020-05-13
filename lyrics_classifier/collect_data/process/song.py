"""
Song
====

Contains the :class:`Song`
"""


class Song:
    """Song.

    Used for having a consistent interface, in particular for  creating
    consistent CSV rows.
    """

    def __init__(self, **attributes) -> None:
        self.artist = attributes.get("artist")
        self.song_title = attributes.get("song_title")
        self.song_path = attributes.get("song_path")
        self.year = attributes.get("year")
        self.album_title = attributes.get("album_title")
        self.album_path = attributes.get("album_path")
        self.duration = attributes.get("duration")
