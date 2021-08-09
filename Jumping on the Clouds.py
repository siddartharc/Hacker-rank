import math
import os
import random
import re
import sys
def jumpingOnClouds(c):
    # Write your code here
    l_p = len(c)-1 # l_p = last position
    l_s_p = len(c)-2 # l_s_p =last second position
    p = 0 #current position
    j = 0 #no of jumps
    while(p<l_s_p): #while p is less than the last second position
        if(c[p+2]==0):
            p=p+2
        else:
            p=p+1
        j=j+1
    if(p!=l_p):
        j=j+1
    return j    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
