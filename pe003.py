'''

Largest prime factor
======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from problem import Problem

class Pe003(Problem):

    def execute(self):
        num = 600851475143

        def is_prime(num):
            quotient = 1
            while quotient < num / 2:
                quotient += 1
                if num % quotient == 0:
                    # is not prime
                    return False
            # is prime
            return True

        quotient_1 = 1
        while quotient_1 < num / 2:
            quotient_1 += 1
            quotient_2 = num / quotient_1

            if num % quotient_1 == 0 and is_prime(quotient_2):
                return quotient_2
                break

Pe003().main()
