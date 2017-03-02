'''

Largest palindrome product
======================

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3 digit numbers

'''
from problem import Problem

class Pe004(Problem):

    def execute(self):
        n = 999;

        highest = (0,0,0);

        for i in range(n, 0, -1):
            for j in range(i, 0, -1):
                num = i * j
                if(Pe004.isPalindrome(num) and num > highest[0]):
                    highest = (num, i, j)

        return str(highest)

    @staticmethod
    def isPalindrome(num):
        numStr = str(num)

        a = 0
        b = len(numStr) - 1

        while a < b:
            if numStr[a] != numStr[b]:
                return False
            a += 1
            b -= 1

        return True

Pe004().main()
