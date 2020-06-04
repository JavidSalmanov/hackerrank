#!/bin/python3
import os
import sys


def timeConversion(s):
    last_chars = s[-2:]
    first_chars = s[:2]
    if last_chars == 'AM' and first_chars == '12':
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif last_chars == 'PM' and first_chars == '12':
        return s[:-2]
    else:
        return str(int(s[:2]) + 12)+s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
    s = input()
    result = timeConversion(s)
    print(result)
