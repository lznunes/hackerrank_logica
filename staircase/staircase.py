#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    stair = ''
    for i in range(0, n):
        stair = stair + '#'
        print(stair.rjust(n, ' '))
  
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
 
   