# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.

#!/bin/python3

import os
import sys

# Complete the timeConversion function below.
def timeConversion(s):
    # Write your code here.
    s = list(s)

    if s[0:2] == ['1','2'] and s[-2:] == ['A','M']:
        s[0:2] = ['0','0']
        
    if s[-2:] == ['P','M'] and s[0:2] != ['1','2']:
        s[0] = str(int(s[0])+1)
        s[1] = str(int(s[1])+2)
        
    s = s[:-2]
    s = ''.join(s)
    return s   
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()

    result = timeConversion(s)

    f.write(result + '\n')
    f.close()
