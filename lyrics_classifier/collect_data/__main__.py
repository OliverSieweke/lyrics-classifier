"""
Collect Data
============

This script includes the main steps for retrieving and parsing HTML
pages from `lyrics.com` to extract lyrics.
"""
# Data Science
import pandas as pd

# Project ------------------------------------------------------------------------------
from lyrics_classifier import paths
from lyrics_classifier.collect_data import clean, process, scrap


scrap.retrieve_artists_html_pages()
process.artists_html_pages_to_songs_csv()
clean.drop_duplicate_songs(pd.read_csv(paths.songs_csv_file_path())).to_csv(
    paths.songs_csv_file_path()
)
scrap.retrieve_songs_html_pages()
process.songs_html_pages_to_lyrics_text()
