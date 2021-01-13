# Given a 6x6 2D Array, 'arr':
# 
#   1 1 1 0 0 0
#   0 1 0 0 0 0
#   1 1 1 0 0 0
#   0 0 0 0 0 0
#   0 0 0 0 0 0
#   0 0 0 0 0 0
# 
# An hourglass is a subset of values with indices falling in this pattern in arr's graphical representation:
#   a b c
#     d
#   e f g

# There are 16 hourglasses in 'arr'. An hourglass sum is the sum of an hourglass' values. 
# Calculate the hourglass sum for every hourglass in 'arr', then print the maximum hourglass sum. 
# The array will always be 6x6.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    total = []
    for i in range(4):
        for j in range(4):
            one   = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            two   = arr[i+1][j+1]
            three = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            total.append(one+two+three)        
    return max(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
