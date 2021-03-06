

"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
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

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
import sys
import calendar
from datetime import datetime

def calendarFunction():
    # grab today's information for when nothing is input by the user
    # today = datetime.now()
    # year = datetime.now().year
    # month = datetime.now().month
    # print("This is the month", str(month))

    today = datetime.today()
    year = today.year
    month = today.month
    # print("This is the month", str(month))

    #make inputs
    inputMonth = input("Please type a month, ex: 8 (only numbers and no spaces)! :")
    inputYear = input("Please type a year, ex: 1995 (only numbers and no spaces)! :")
    # print(inputMonth, inputYear)

    # write conditionals to print calendar
    if len(inputMonth) > 0 and len(inputMonth) <= 2 and inputMonth.isdigit():
        month = int(inputMonth)

    if len(inputYear) > 0 and len(inputYear) <= 4 and inputYear.isdigit():
        year = int(inputYear)

    print(calendar.month(year, month))

calendarFunction()

# works
# test = input("Enter the date: ").split(",")
# print(test)

# works
# print(calendar.weekday(2020, 7, 7))

# works
# tc = calendar.TextCalendar(firstweekday=6)
# print(tc.formatmonth(2020, 7))

# userinputdate = input("Enter the date: ").split(",")

# def calendarfunction():
#     if len(userinputdate) == 0:
#         tc = calendar.TextCalendar(firstweekday=6)
#         testmonth = datetime.datetime.now()
#         print(tc.formatmonth(testmonth.year, testmonth.month))
#     else:
#       return None

# calendarfunction()

# tc = calendar.TextCalendar(firstweekday=6)
# testmonth = datetime.datetime.now()
# print(tc.formatmonth(testmonth.year, testmonth.month))

# cal = calendar.Calendar()
# print(cal.monthdatescalendar(2020, 7))