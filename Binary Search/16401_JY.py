# BOJ 16401
# 과자 나눠주기
import sys

m, n = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(lst)
answer = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2
    if mid == 0:
        break
    for i in lst:
        total += i // mid
    if total < m:
        end = mid-1
    else:
        start = mid+1
        answer = mid
print(answer)
