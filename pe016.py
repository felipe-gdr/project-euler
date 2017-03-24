'''

Power digit sum
===========================

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

'''
from problem import Problem

class Pe016(Problem):
    def execute(self):
        result = 0

        for d in str(2**1000):
            result += int(d)

        return result

Pe016().main()
