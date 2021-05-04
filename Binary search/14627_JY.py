# BOJ 14627
# 파닭파닭
import sys

k, n = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lst)
result = 0

while start <= end:
    mid = (start + end) // 2
    answer = 0
    for i in lst:
        answer += i // mid
    if answer < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(sum(lst) - result * n)
