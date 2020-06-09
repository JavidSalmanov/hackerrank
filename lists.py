def listAction(biglist):
    l = []
    for i in range(len(biglist)):
        line = biglist[i].split()
        if line[0] == 'insert':
            l.insert(int(line[1]), int(line[2]))
        elif line[0] == 'append':
            l.append(int(line[1]))
        elif line[0] == 'remove':
            l.remove(int(line[1]))
        elif line[0] == 'sort':
            l.sort()
        elif line[0] == 'reverse':
            l.reverse()
        elif line[0] == 'pop':
            l.pop()
        elif line[0] == 'print':
            print(l)

if __name__ == '__main__':
    N = int(input())
    biglist = []

    for _ in range(N):
        item = (input().strip())
        biglist.append(item)
listAction(biglist)






'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialilinee your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''