if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mylist = list(dict.fromkeys(arr))
    fisrt = max(mylist)
    mylist.remove(fisrt)
    print(max(mylist))
    # print(arr)
    # for i in range(0, n):
    #     if arr[i] == fisrt:
    #         arr.remove(arr[i])
    #         n -= 1
    # print((arr))
