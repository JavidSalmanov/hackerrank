#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(arr):
    for i in range(len(arr)):
        print(arr[i])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(res)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
