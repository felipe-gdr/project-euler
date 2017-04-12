'''

Counting Sundays
===========================

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''
from problem import Problem

class Pe019(Problem):
    def execute(self):
        day, date, month, year, count = [1, 1, 0, 1900, 0]

        while year * 10000 + month * 100 + date <= 20001231:
            days_in_month = self.daysInMonth(year, month)

            year = year + ((month / 11 + date / days_in_month) / 2)
            month = (month + (date / days_in_month)) % 12
            date = (date % days_in_month) + 1
            day = (day + 1) % 7

            if year >= 1901 and date == 1 and day == 0:
                count += 1
                print year, month, date, day

        return count

    def daysInMonth(self, year, month):
        if month == 1:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            elif year % 4 == 0:
                return 29
            else:
                return 28
        elif month in [8, 3, 5, 10]:
            return 30
        else:
            return 31

Pe019().main()
