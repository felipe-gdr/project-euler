'''

Multiples of 3 and 5
====================

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
from problem import Problem

class Pe001(Problem):
    def execute(self):
        max = 1000
        m = [3,5]

        result = []
        for n in m:
            num = 0
            while num < max:
                if num != 0 and num not in result :
                    result.append(num)

                num = num + n
        return sum(result)

Pe001().main()
