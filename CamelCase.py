import math
import os
import random
import re
import sys
def camelcase(s):
    c=0 #to count the words
    for i in range(len(s)):
        if(s[i]==s[i].upper()):
            c= c+1
        else:
            continue
    return c+1 # as camel case starts with 1st word lower case 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
