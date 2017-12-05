# -*- coding: utf-8 -*-
"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then
counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to
square 1 (the location of the only access port for this memory system) by programs that can only
move up, down, left, or right. They always take the shortest path: the Manhattan Distance between
the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all
the way to the access port?

Your puzzle input is 277678.

JBH: Note:
    This is a, "Ulam Spiral". http://primorial-sieve.com/3_Ulam%20spiral%20Coordinates.php
    "Data from square 1024 must be carried 31 steps" Interesting that 1024 = 30^2
    Diagonal SE from the center th evalues are squares of odd number progression
        e.g. 1^2 = 1, 3^2 = 9, 5^2 = 25. The next value in the line would be 49. Does this continue?


--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in
square 1. Then, in the same allocation order as shown above, they store the sum of the values in all
adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their
values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive
the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?
"""

import math


def calculate_required_steps(spiral_num):
    """
    Calculates the number of steps (manhattan) to get from spiral_num to the center of the
    ulam spiral.
    Note:   This code was influenced by a solution in the reddit r/adventofcode solution megathread
            for day 3.
    """

    layer = math.floor(math.ceil(math.sqrt(spiral_num)) / 2) + 1
    distance_to_closest_edge = max_val = (2 * layer - 1)

    for i in range(5):
        if abs(max_val**2 - i * (max_val - 1) - spiral_num) < distance_to_closest_edge:
            distance_to_closest_edge = abs(max_val**2 - i * (max_val - 1) - spiral_num)

    return max_val - 1 - distance_to_closest_edge



if __name__ == '__main__':
    INPUT = 277678
    print(calculate_required_steps(INPUT))
