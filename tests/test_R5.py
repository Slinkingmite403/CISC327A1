import pytest
from library_service import calculate_late_fee_for_book

def test_late_fee_no_overdue():
    result = calculate_late_fee_for_book("123456", 1)
    assert result["fee_amount"] == 0.00
    assert result["days_overdue"] == 0
    assert "no late fee" in result["status"].lower() or "on time" in result["status"].lower()

def test_late_fee_within_7_days():
    result = calculate_late_fee_for_book("123456", 2)  #  5 days overdue
    assert result["days_overdue"] == 5
    assert result["fee_amount"] == 5 * 0.50
    assert "overdue" in result["status"].lower()

def test_late_fee_after_7_days():
    result = calculate_late_fee_for_book("123456", 3)  #  10 days overdue
    assert result["days_overdue"] == 10
    assert result["fee_amount"] == (7 * 0.50) + (3 * 1.00)
    assert "overdue" in result["status"].lower()

def test_late_fee_max_cap():
    result = calculate_late_fee_for_book("123456", 4)  # assume long overdue
    assert result["fee_amount"] == 15.00
    assert result["fee_amount"] <= 15.00
    assert "maximum" in result["status"].lower() or "capped" in result["status"].lower()

def test_late_fee_invalid_input():
    result = calculate_late_fee_for_book("", -1)
    assert result["fee_amount"] == 0.00
    assert "error" in result["status"].lower() or "invalid" in result["status"].lower()
