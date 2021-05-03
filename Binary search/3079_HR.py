# BOJ 3079
# 입국심사

import sys
n, m = map(int, input().split())
time = list(int(sys.stdin.readline()) for _ in range(n))
start, end = 1, min(time) * m
result = float('inf')
time.sort()
while(start <= end):
    mid = (start+end) // 2
    num = 0
    for x in time:
        num += mid // x
    if num >= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid + 1
print(result)
