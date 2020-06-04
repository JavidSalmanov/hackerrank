if __name__ == '__main__':
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        students.append([name, score])
    students.sort()
    min_score = min(grades)
    min_index = []
    while min_score in grades:
        grades.remove(min_score)

    second_score = min(grades)
    for studen in range(len(students)):
        if second_score in students[studen]:
            print(students[studen][0])
