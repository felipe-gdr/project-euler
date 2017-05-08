'''

Factorial digit sum
===========================

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''
from problem import Problem

class Pe020(Problem):
    def execute(self):
        result = 1
        n = 100

        while n > 0:
            result *= n
            n -= 1

        return sum([int(d) for d in str(result)])


Pe020().main()
