#!/bin/python3
def starsTree(n):
    for i in range(n):
        print(' '*(n-i-1)+'* '*(i+1))


if __name__ == '__main__':
    n = int(input())

    starsTree(n)
