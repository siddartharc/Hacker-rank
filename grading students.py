#!/bin/python3

import math
import os
import random
import re
import sys
n = int(input().strip())

for i in range(n):
  grade = int(input().strip())
  if grade >= 38:
    # here to find the remainder when divided by 5 
    r = grade%5
    if r>=3:
      grade = grade +(5 - r)
 print(grade)
