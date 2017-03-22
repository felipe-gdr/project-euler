'''

Longest Collatz sequence
===========================
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
from problem import Problem

class Pe014(Problem):
    def execute(self):
        num_with_longest_chain = 0
        longest_chain = 0

        for i in range(500000, 1000000):
            this_chain = self.calculateChain(i)

            if this_chain > longest_chain:
                longest_chain = this_chain
                num_with_longest_chain = i

        return str((num_with_longest_chain, longest_chain))

    def calculateChain(self, num):
        n = num
        count = 1

        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            count += 1

        return count

Pe014().main()
