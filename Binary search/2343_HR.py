# BOJ 2343
# 기타 레슨

import sys
n, m = map(int, input().split())
time = list(map(int, sys.stdin.readline().split()))
res = 0
# ✨ key P => start가 1이 아닌 max(time)으로 최소 한 음악은 들어가도록
start, end = max(time), sum(time) 
while(start <= end):
    mid = (start+end) // 2
    cnt = 1
    total = 0
    for x in time:
        total += x
        if total > mid:
            cnt += 1
            total = x
    if cnt <= m:
        end = mid - 1
        res = mid
    else:
       start = mid + 1
print(res)
