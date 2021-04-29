# BOJ 11651
# 좌표 정렬하기 2

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])
arr.sort()
for y, x in arr:
    print(x, y)