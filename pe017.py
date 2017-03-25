'''

Number letter counts
===========================

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''
from problem import Problem

class Pe017(Problem):
    def __init__(self):
        self.num_map = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'
        }

    def execute(self):
        oneTo99 = len(self.oneTo99('', ''))

        result = oneTo99

        print result

        for i in range (1, 10):
            this_hundred = self.num_map[i] + 'hundred'

            result += len(this_hundred)

            prefix = len(this_hundred + 'and')

            result += (99 * prefix) + oneTo99

            print result

        result += len('onethousand')

        return result

    def oneTo99(self, prefix, num_str):
        for i in range(1, 100):
            if i < 20:
                num_str += prefix + self.num_map[i]
            else:
                num_str += prefix + self.num_map[(i / 10 * 10)]
                if i % 10 != 0:
                    num_str += self.num_map[i % 10]

        print num_str

        return num_str

Pe017().main()
