"""
Collect Data
============

This script includes the main steps for retrieving and parsing HTML
pages from `lyrics.com` to extract lyrics.
"""
# Project ------------------------------------------------------------------------------
from lyrics_classifier.collect_data import process, scrap


scrap.retrieve_artists_html_pages()
process.artists_html_pages_to_songs_csv()
scrap.retrieve_songs_html_pages()
process.songs_html_pages_to_lyrics_text()
