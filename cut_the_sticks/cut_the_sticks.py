#https://www.hackerrank.com/challenges/cut-the-sticks/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    result = []
    
    
    while arr:
        result.append(len(arr))
        min_stick = min(arr)
        arr = [x - min_stick for x in arr if x != min_stick]
    return result

if __name__ == '__main__':
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'cut_the_sticks/cut_the_sticks.txt')
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    
    with open(file_path, 'w') as fptr:
        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


