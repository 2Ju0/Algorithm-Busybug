# BOJ 13702
# 이상한 술집

import sys
n, m = map(int, input().split())
beer = list(int(sys.stdin.readline()) for _ in range(n))
lt, rt = 1, max(beer)
amount = 0
while(lt <= rt):
    mid = (lt+rt) // 2
    cnt = 0
    for x in beer:
        cnt += x // mid
    if cnt >= m:
        lt = mid + 1
        amount = mid
    else:
        rt = mid - 1
print(amount)