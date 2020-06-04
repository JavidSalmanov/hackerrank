
def solution(N):
    if N <= 9:
        result = N
    else:
        nine_count = ((N)// 9)
        second_num = str((N)%9)
        result = int(second_num + nine_count*'9')
    print(result)



N = 7
solution(N)