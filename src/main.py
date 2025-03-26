"""
File: main.py
Author: Alec Hoelscher, Daniel Stone, Grant Valentine, Gabby Strevay, with help from Github Copilot
Date: 03/26/2025
Description: This file accepts user input and computes the next date using the next_date method.
"""

from next_date import next_date

while(True):
    print("Enter a date in the format MM/DD/YYYY")  
    date = input()

    date = date.split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    calculated_next_date = next_date(month, day, year)
    if(calculated_next_date == "Invalid input date"):
        print("Invalid input date. Please enter a valid date.")
    else:
        print(f"The next date is: {next_date}")
        break