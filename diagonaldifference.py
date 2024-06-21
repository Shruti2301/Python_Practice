#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/diagonal-difference/problem

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftdiagonal = 0
    rightdiagonal = 0
    for i in range(n):
        leftdiagonal += arr[i][i]
        rightdiagonal += arr[i][n-1-i]
    return abs(leftdiagonal - rightdiagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
