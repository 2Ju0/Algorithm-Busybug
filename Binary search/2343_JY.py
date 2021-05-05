# BOJ 2343
# 기타 레슨
import sys

n, m = map(int, sys.stdin.readline().split(' '))
lst = list(map(int, sys.stdin.readline().split(' ')))

start, end = max(lst), sum(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    total = 0
    for time in lst:
        total += time
        if total > mid:
            cnt += 1
            total = time
    if cnt <= m:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)
