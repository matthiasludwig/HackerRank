#!/bin/python3

import math
import os
import random
import re
import sys

def sum_hourglass(arr, hourglass, row, col):
    sum = 0
    for i in range(0, len(hourglass[0])):
        sum += arr[hourglass[0][i] + row][hourglass[1][i] + col]

    return sum



if __name__ == '__main__':
    arr = []
    hourglass = [[0, 0, 0, 1, 2, 2, 2], [0, 1, 2, 1, 0, 1, 2]]
    sum = 0

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Initialize to the first hourglass
    high = sum_hourglass(arr, hourglass, 0, 0)

    for col in range(0, 4):
        for row in range(0, 4):
            sum = sum_hourglass(arr, hourglass, row, col)

            if sum > high:
                high = sum
            sum = 0

    print(high)