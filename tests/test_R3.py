import pytest
from library_service import borrow_book_by_patron
from database import insert_book, insert_borrow_record


def test_borrow_valid():
    success, msg = borrow_book_by_patron("123456", 1)
    assert success
    assert "Successfully borrowed" in msg

def test_valid_book_id():
    success, msg = borrow_book_by_patron("123456", 999)  # ID that doesn't exist
    assert not success
    assert "Book not found" in msg

def test_invalid_patron_id():
    success, msg = borrow_book_by_patron("12a45", 1)
    assert not success
    assert "Invalid patron ID" in msg

def test_borrow_invalid_unavailable_book():
    success, msg = borrow_book_by_patron("123456", 2)  # ID of the book with 0 copies
    assert not success
    assert "not available" in msg
