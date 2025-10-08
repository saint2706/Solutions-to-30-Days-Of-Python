"""Curriculum exports for Day 30: Web Scraping."""
from .presidents import scrape_presidents_data, convert_csv_to_json, save_mock_json, main
from .profile_web_scraping import build_pipeline, main
from .web_scraping import ScrapingError, scrape_books, process_book_data, main
from . import web_scraping_bu as _web_scraping_bu

__all__ = ["scrape_presidents_data", "convert_csv_to_json", "save_mock_json", "main", "build_pipeline", "main", "ScrapingError", "scrape_books", "process_book_data", "main"]
