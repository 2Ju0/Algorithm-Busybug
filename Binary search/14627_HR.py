# BOJ 14627
# 파닭파닭

import sys
s, c = map(int, input().split())
arr = list(int(sys.stdin.readline()) for _ in range(s))
start, end = 1, max(arr)
res = 0
while (start <= end):
    mid = (start+end) // 2
    cnt = 0
    for x in arr:
        cnt += x // mid
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(sum(arr)-res*c)
