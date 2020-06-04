ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9

mylist = list(dict.fromkeys(ar))
print(mylist) 
count = 0
for i in range(0, len(mylist)):
    count += (ar.count(mylist[i]))//2
    print(count)
