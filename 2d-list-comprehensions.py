x = int(input())
y = int(input())
n = int(input())
ar = []
p = 0
for i in range(x + 1):
    for j in range(y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [i, j]
            p += 1
print(ar)