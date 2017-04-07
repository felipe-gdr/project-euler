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
        day = 2
        date = 1
        month = 1
        year = 1900


        count = 0
        while year * 10000 + month * 100 + date <= 19020631:
        # while count < 100:
            days_in_month = self.daysInMonth(year, month)

            year = year + ((month) / 12)
            month = month + ((date + 1) / (days_in_month + 1))
            # month = (month % 12) + 1
            date = (date % days_in_month) + 1
            day = (day + 1) % 7

            # count += 1

            print year, month, date, day


        return True

    def daysInMonth(self, year, month):
        if month in [2]:
            if year % 100:
                if year % 400:
                    return 29
                else:
                    return 28
            elif year % 4:
                return 29
            else:
                return 28
        elif month in [9, 4, 6, 11]:
            return 30
        else:
            return 31

    def testDay(self):
        days_in_month = 30
        date = 1
        month = 1

        count = 0
        while count < 100:
            # print  'b', date, month
            month = month + ((date + 1) / (days_in_month + 1))
            date = (date % days_in_month) + 1

            print  'a', date, month
            print  ''
            count += 1



Pe019().main()
# Pe019().testDay()
