# BOJ 1946
# 신입 사원

import sys
t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()
    for i in range(n):
        for j in range(n):
            if (arr[i][0] > arr[j][0]) and (arr[i][1] > arr[j][1]):
                break        
        else:
            cnt += 1
    print(cnt)