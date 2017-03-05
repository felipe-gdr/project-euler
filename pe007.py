'''

10001st prime
======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
from problem import Problem
from math import sqrt

class Pe007(Problem):

    def isPrime(self, num, primes):
        for i in primes:
            if num % i == 0:
                return False
            if sqrt(num) < i:
                break

        return True

    def execute(self):
        primes = [2]
        num = 3

        # 'x' represents how many primes do we want to calculate
        x = 10001

        while len(primes) < x:
            if self.isPrime(num, primes):
                primes.append(num)

            num += 2

        return str((primes[-20:], len(primes)))

Pe007().main()
