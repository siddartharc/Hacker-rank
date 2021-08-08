# You may see the question big but it is a simple question if you did not understand the question just go through the sample input and sample out put.
# Here out main objective is to find the least number from the given width in b/w the points given in the cases array.
# I made some changes to the arguments which we take to the function servicelane. 
# the code goes like this:
import math
import os
import random
import re
import sys
def serviceLane(width, cases,t): #getting width, cases,t in place of n,cases.(change which i made)
    sid =[] # declearing an empty array to store the min width in the given case
    for i in range(t):
        [x,y]=cases[i]
        minw=min(width[x:y+1])
        sid.append(minw)
    return (sid)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases,t)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
