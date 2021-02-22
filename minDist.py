# The distance between two array values is the number of indices between them. 
# Given 'a', find the minimum distance between any pair of equal elements in the array. If no such value exists, return 1.

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    MIN = 1e6
    for i, ele in enumerate(a): 
        for space in range(1,len(a)): #1 -> 3
            try:
                if a[i+space] == ele and space < MIN:
                    MIN = space
            except:
                continue
            
    if MIN < 1e6:
        return MIN
    else:
        return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()
