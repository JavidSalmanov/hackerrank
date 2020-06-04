#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mylist = list(dict.fromkeys(ar))
    count = 0
    for i in range(0, len(mylist)):
        count += (ar.count(mylist[i]))//2
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
