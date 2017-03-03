'''

Smallest multiple
======================

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
from problem import Problem

class Pe005(Problem):
    def __init__(self):
        self.n = 20
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def execute(self):
        # The result has to be a number wich is evenly divisible by all prime numbers.
        # So first we calculate a number, called 'step', which is the product of all
        # prime numbers from 1 to 20. The result has to be evenly divisile by 'step'
        step = reduce(lambda x, y: x*y, self.primes)
        num = 0

        # Limit iterations to 100, to avoid infinite loops
        for i in range(1, 100):
            num += step
            if self.check(num):
                return num

        return "Not Found. Add more iterations to the loop and try again."

    def check(self, num):
        for i in range(self.n, 1, -1):
            if num % i != 0:
                return False

        return True

Pe005().main()
