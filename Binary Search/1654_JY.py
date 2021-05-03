# BOJ 11654
# 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(k)]

start = 0
end = max(lst)

while (start <= end):
    mid = (start + end) // 2
    answer = 0
    for i in lst:
        answer += i // mid
    if answer < n:
        end = mid-1
    else:
        start = mid+1
print(end)
