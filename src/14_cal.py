"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar(calendar.SUNDAY)


def create_calendar(calendar_input):
    try:
        now = datetime.now()
        input_date = calendar_input.split()
        if(not input_date or len(input_date) not in range(3)):
            print("Please type the date in the following format: MM YYYY")
            return

        cases = {
            0: cal.formatmonth(now.year, now.month),
            1: cal.formatmonth(now.year, int(input_date[0])),
            2: cal.formatmonth(int(input_date[1]), int(input_date[0]))
        }
        print(cases[len(input_date)])
    except Exception as e:
        print(f'Error: {e}')
        print("Please type the date in the following format: MM YYYY")


calendar_input = input('Please input month and year (format: MM YYYY):')
create_calendar(calendar_input)
