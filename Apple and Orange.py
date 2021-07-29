#!/bin/python3

import math
import os
import random
import re
import sys
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    r = len(apples)
    c = len(oranges)
    d=0 # to count no of apples
    e=0 # to count no of oranges
    for i in range(r):
        if(a+apples[i]<=t and a+apples[i]>=s):#adding the distances that each apple falls from point
            d = d+1
    for i in range(c):
        if(b+oranges[i]<=t and b+oranges[i]>=s):##adding the distances that each orange falls from point
            e = e+1
    print(d)
    print(e)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
