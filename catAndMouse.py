#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    leftCat = min(x,y)
    rightCat = max(x,y)

    if z < leftCat:
        if x == y:
            return "Mouse C"
        if x == leftCat:
            return "Cat A"
        return "Cat B"

    if z > max(x,y):
        if x == y:
            return "Mouse C"
        if x == rightCat:
            return "Cat A"
        return "Cat B"

    if z - leftCat == rightCat - z:
        return "Mouse C"
    if z - leftCat > rightCat - z:
        if x == rightCat:
            return "Cat A"
        return "Cat B"
    if x == leftCat:
        return "Cat A"
    return "Cat B"
