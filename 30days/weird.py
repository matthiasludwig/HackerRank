#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(number):
    if (number % 2 == 0):
        if (number >= 2 and number <= 5):
            print("Not Weird")
        if (number >= 6 and number <= 20):
            print("Weird")
        if (number > 20):
            print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    N = int(input())

    is_weird(N)
