# BOJ 13702
# 이상한 술집
import sys

n, k = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(n)]

start, end = 1, max(lst)
answer = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in lst:
        total += i // mid

    if total < k:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
print(answer)
