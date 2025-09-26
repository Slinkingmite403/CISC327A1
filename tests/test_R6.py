import pytest
from library_service import search_books_in_catalog

def test_search_by_title_partial_match():
    results = search_books_in_catalog("python", "title")
    assert isinstance(results, list)
    assert any("python" in book["title"].lower() for book in results)

def test_search_by_author_partial_match():
    results = search_books_in_catalog("doe", "author")
    assert isinstance(results, list)
    assert any("doe" in book["author"].lower() for book in results)

def test_search_by_isbn_exact_match():
    results = search_books_in_catalog("1234567890123", "isbn")
    assert isinstance(results, list)
    assert all(book["isbn"] == "1234567890123" for book in results)

def test_search_with_no_results():
    results = search_books_in_catalog("zzzzzz", "title")
    assert isinstance(results, list)
    assert len(results) == 0

def test_search_with_invalid_type():
    results = search_books_in_catalog("anything", "unknown_type")
    assert results == [] or isinstance(results, list)
