"""
File: next_date.py
Author(s): Alec Hoelscher, Daniel Stone, Grant Valentine, Gabby Strevay, with help from Github Copilot
Date: 03/24/2025
Description: This assignment is to create a program that takes in a date and returns the next date.
"""

def is_leap_year(year) -> bool:
    """
    This function determines if a year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(month, year) -> int:
    """
    This function determines the number of days in a month.
    """
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    
def next_date(month, day, year) -> str:
    """
    This function determines the next date.
    """
    if year < 1900 or year > 2025:
        return "Invalid input date"
    if month < 1 or month > 12:
        return "Invalid input date"
    if day < 1 or day > days_in_month(month, year):
        return "Invalid input date"
    if day < days_in_month(month, year):
        return (f"{month}, {day + 1}, {year}")
    else:
        if month < 12:
            return (f"{month + 1}, 1, {year}")
        else:
            return (f"1, 1, {year + 1}")