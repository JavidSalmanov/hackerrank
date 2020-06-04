#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_arr = 0
    minimum = min(arr)
    maximum = max(arr)
    for i in range(arr):
        sum_arr += i
    minimum_last = sum_arr - maximum
    maximum_last = sum_arr - minimum
    print(minimum_last, maximum_last)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
