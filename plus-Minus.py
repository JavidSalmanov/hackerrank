#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    N = len(arr)
    for i in range(N):
        if arr[i] ==0:
            zero += 1
        elif( arr[i] > 0):
            positive += 1
        else:
            negative += 1
    print(positive/N)
    print(negative/N)
    print(zero/N)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
