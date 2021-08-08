# our main objective is to find the minimun no of elements to delete so that we can form an equalised array.
# inn this code i will simply find the what is the maximum no of times an element is repeated and subtract from the len of arr.
import math
import os
import random
import re
import sys
def equalizeArray(arr):
    # Write your code here
    r = len(arr) # finding the length of arr
    arr.sort() 
    s = 0 #initialising s =0
    c = []
    for i in range(r):
        for z in arr:
            if(z==arr[i]):
                s = s+1
        c.append(s)
        s=0 # reinitialising s
    return r - max(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
