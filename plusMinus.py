# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    neg = 0; pos = 0; zeros = 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zeros += 1
    neg /= length
    pos /= length
    zeros /= length
    print(pos)
    print(neg)
    print(zeros)
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
