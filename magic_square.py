#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    all_possible = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    all_costs = []
    for square in all_possible:
        cost = 0
        for i_p, i_s in zip(square, s):
            for j_p, j_s in zip(i_p, i_s):
                cost += abs(j_p - j_s)
        all_costs.append(cost)

    return min(all_costs)
