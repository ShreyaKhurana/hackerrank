'''

Watson likes to challenge Sherlock's math ability. He will provide a starting
and ending value describing a range of integers. Sherlock must determine the
number of square integers within that range, inclusive of the endpoints.

'''

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    # Take the sqrt of both numbers and basically all numbers in between the square roots will have their squares in between a and b
    return(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
