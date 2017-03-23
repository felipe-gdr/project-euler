'''

Lattice paths
===========================
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''
from problem import Problem

class Pe015(Problem):
    def __init__(self, x, y):
        # Initialize matrix with given dimensions
        self.arr = [[0 for i in range(x + 1)] for j in range(y + 1)]

        self.x = x
        self.y = y

    def execute(self):
        for i in range(0, self.x + 1):
            for j in range(0, self.y + 1):
                if i == 0 or j == 0:
                    # Coordinates at the bottom and right edges have a single
                    # path to get to the destination
                    self.arr[i][j] = 1
                else:
                    self.arr[i][j] = self.arr[i-1][j] + self.arr[i][j-1]

        return self.arr[self.x][self.y]

Pe015(20, 20).main()
