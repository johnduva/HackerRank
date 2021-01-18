# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. 
# Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
# Given an array 'arr' of len(arr) integers and a number, 'n', perform 'n' left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the rotLeft function below.
def rotLeft(arr, n):
    for num in range(n):
        first = arr.pop(0)
        arr.append(first)
    return arr
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
