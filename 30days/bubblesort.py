#!/bin/python3

def swap(a, first, second):
    temp = a[first]
    a[first] = second
    a[second] = temp
    return a

def print_result(numswaps, a):
    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(numswaps, a[0], a[len(a) - 1]))

def bubble_sort(a, n):
    for i in range(n):
        # Track number of elements swapped during a single array traversal
        numberOfSwaps = 0
    
    for j in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            swap(a, j, j+1)
            numberOfSwaps += 1
    
    # If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0):
        return a, numberOfSwaps

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

a, numOfSwaps = bubble_sort(a, n)

print_result(numOfSwaps, a)