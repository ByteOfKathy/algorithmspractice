#!/bin/python3
# Hackerrank plus minus problem

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def plusMinus(arr):
    """
    thought process: I'm going to initialize each
    proportion as their own float and initially they
    will store the amount of positives, negatives... etc.
    They will then be turned into ratios by dividing the 
    length of arr. Python has a cheeky round function so
    I will end up using that. Otherwise I would have added
    .5*10^(-4) and floored it. I'm not sure that would have
    worked though.
    """
    # Write your code here
    # initialize variables
    positives = negatives = zeros = float(0)
    
    # calculate the number of positives, negatives, and zeros
    for i in range(len(arr)):
        # positive number
        if arr[i] > 0:
            positives += 1
        # negative number
        elif arr[i] < 0:
            negatives += 1
        # zero
        else:
            zeros += 1
    
    # calculate ratios
    positives = round(positives/len(arr), 6)
    negatives = round(negatives/len(arr), 6)
    zeros = round(zeros/len(arr), 6)
    
    # print
    print(positives)
    print(negatives)
    print(zeros)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
