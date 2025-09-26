import pytest
from library_service import return_book_by_patron

def test_return_book_successful():
    success, msg = return_book_by_patron("123456", 1)
    assert success is True
    assert "returned successfully" in msg

def test_return_book_invalid_patron_id():
    success, msg = return_book_by_patron("12", 1)
    assert success is False
    assert "invalid patron" in msg
    
def test_return_book_invalid_book_id():
    success, msg = return_book_by_patron("123456", -1)
    assert success is False
    assert "book" in msg

def test_return_book_not_borrowed():
    success, msg = return_book_by_patron("123456", 9999)
    assert success is False
    assert "not borrowed" in msg
