'''

Special Pythagorean triplet
===========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

===========================


'''
from problem import Problem

class Pe009(Problem):
    def execute(self):
        num = 1000
        a, b = [1, 2]

        for a in range(1, num):
            for b in range(a + 1, num - a):
                c = num - a - b

                if c <= b:
                    break

                if a**2 + b**2 == c ** 2:
                    return str((a, b, c, a * b * c))



Pe009().main()
