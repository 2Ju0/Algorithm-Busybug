# BOJ 2110
# 공유기 설치

import sys
n, c = map(int, input().split())
house = list(int(sys.stdin.readline()) for _ in range(n))
house.sort()
start, end = 1, max(house)
res = 0
while(start <= end):
    mid = (start+end) // 2
    cnt = 1
    interval = house[0]
    for i in range(1, n):
        if house[i]-interval >= mid:
            cnt += 1
            interval = house[i]
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)