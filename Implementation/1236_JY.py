# BOJ 1236
# 성 지키기

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            column[j] = 1

rowCnt, colCnt = 0, 0
for i in range(n):
    if row[i] == 0:
        rowCnt += 1

for i in range(m):
    if column[i] == 0:
        colCnt += 1

print(max(rowCnt, colCnt))
