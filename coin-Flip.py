def solution(A):
    N = len(A)
    binary1 = 0
    binary2 = 1
    min1 = 0
    min2 = 0
    for i in range(N):
        if A[i] == binary2:
            min1 += 1
        else:
            min2 += 1
        binary1, binary2 = binary2, binary1
    return min(min1, min2)
A =[0, 0, 1, 0]
print(solution(A))
