# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    singles = []
    for i, sock in enumerate(ar):
        if sock not in singles:
            singles.append(sock)
        else:
            singles.remove(sock)
            count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    
    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
