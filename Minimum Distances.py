import math
import os
import random
import re
import sys
def minimumDistances(a):
    r  = len(a)
    c  = [] # for finding the indices of same numbers in array
    s  = [] # for finding the difference of indices
    for i in range(r):
        for j in range(i+1,r):
            if a[i]==a[j]:
                c.append((i,j))
    if(len(c)!=0):
        for (x,y) in c:
            s.append(abs(y-x))
    else:
        s.append(-1)
    return min(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
