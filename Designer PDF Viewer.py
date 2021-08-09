import math
import os
import random
import re
import sys
def designerPdfViewer(h, word):
    maxHeight=0
    for i in range(len(word)):
        if(h[ord(word[i])-97] > maxHeight): # ord is a python function which converts into ascii values
            maxHeight=h[ord(word[i])-97]
    return(len(word)*1*maxHeight)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
