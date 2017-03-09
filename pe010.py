'''

Summation of primes
===========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from problem import Problem
from math import sqrt

class Pe010(Problem):


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

        # Primes have to be lower than 'x'
        x = 2000000

        while num < x:
            if self.isPrime(num, primes):
                primes.append(num)

            num += 2

        return sum(primes)



Pe010().main()
