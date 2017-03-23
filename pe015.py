'''

Lattice paths
===========================
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''
from problem import Problem

class Pe015(Problem):
    def __init__(self):
        self.count = 0

    def execute(self):
        self.move(0, 0)

        return self.count


    def move(self, pos_x, pos_y):
        max_x, max_y = (3, 3)

        if pos_x < max_x:
            self.move(pos_x + 1, pos_y)

        if pos_y < max_y:
            self.move(pos_x, pos_y + 1)
        elif pos_x == max_x and pos_y == max_y:
            self.count += 1



Pe015().main()
