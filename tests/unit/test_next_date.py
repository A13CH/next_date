"""
File: test_next_date.py
Author: Alec Hoelscher, Daniel Stone, Grant Valentine, Gabby Strevay, with help from Github Copilot
Date: 03/24/2024
Description: Test cases for the next_date program
"""

from next_date import next_date

def test_case_1():
    """Test Case ID: 1"""
    assert next_date(1, 1, 2000) == "1, 2, 2000"

def test_case_2():
    """Test Case ID: 2"""
    assert next_date(1, 0, 2000) == "Invalid input date"

def test_case_3():
    """Test Case ID: 3"""
    assert next_date(1, 32, 2000) == "Invalid input date"

def test_case_4():
    """Test Case ID: 4"""
    assert next_date(1, 24, 10000) == "Invalid input date"

def test_case_5():
    """Test Case ID: 5"""
    assert next_date(-1, 26, 2025) == "Invalid input date"

def test_case_6():
    """Test Case ID: 6"""
    assert next_date(13, 24, 2025) == "Invalid input date"

def test_case_7():
    """Test Case ID: 7"""
    assert next_date(1, 31, 2023) == "2, 1, 2023"

def test_case_8():
    """Test Case ID: 8"""
    assert next_date(2, 28, 2025) == "3, 1, 2025"

def test_case_9():
    """Test Case ID: 9"""
    assert next_date(2, 28, 2024) == "2, 29, 2024"

def test_case_10():
    """Test Case ID: 10"""
    assert next_date(2, 29, 2024) == "3, 1, 2024"

def test_case_11():
    """Test Case ID: 11"""
    assert next_date(2, 29, 2025) == "Invalid input date"

def test_case_12():
    """Test Case ID: 12"""
    assert next_date(6, 31, 2000) == "Invalid input date"

