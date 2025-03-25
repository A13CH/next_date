"""
File: test_next_date.py
Author: Alec Hoelscher, Daniel Stone, Grant Valentine, Gabby Strevay, with help from Github Copilot
Date: 03/24/2024
Description: Test cases for the next_date program
"""

from next_date import next_date

def test_case_1():
    """TC1"""
    assert next_date(2, 28, 2024) == "2, 29, 2024"

def test_case_2():
    """TC2"""
    assert next_date(-1, 1, 2024) == "Invalid input date"