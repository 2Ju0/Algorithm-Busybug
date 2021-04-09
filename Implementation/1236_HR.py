# BOJ 1236
# 성 지키기

n, m = map(int, input().split())
arr = list(input() for _ in range(n))
row = [0]*n
col = [0]*m
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            col[j] = 1
print(max(row.count(0),col.count(0)))
