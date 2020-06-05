def findAverage(student_marks, query_name):
    mark = student_marks[query_name]
    avarage_sum = 0
    for i in range(len(mark)):
        avarage_sum += mark[i]
    avarage_mark = ("%.2f" % round(avarage_sum/3, 2))
    return avarage_mark


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
result = findAverage(student_marks, query_name)
print(result)
