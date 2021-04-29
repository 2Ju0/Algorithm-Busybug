# BOJ 5635
# 생일

n = int(input())
students = []
for i in range(n):
    temp = list(input().split())
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    students.append(temp)

students.sort(key=lambda students: (
    students[3], students[2], students[1]), reverse=True)
print(students[0][0])
print(students[4][0])
