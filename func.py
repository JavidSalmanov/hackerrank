def solution(A):
    minim = min(A)
    if minim < 0:
        minim = 1
    while minim in A :
        minim += 1
    print(minim)


A = [ -3, -2, 0, 1, 2]
solution(A)
A = [1, 3, 6, 4, 1, 2]
solution(A)