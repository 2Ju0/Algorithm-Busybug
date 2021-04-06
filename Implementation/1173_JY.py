# BOJ 1773
# 폭죽 쇼

import sys
n, c = map(int, sys.stdin.readline().split())
arr = dict()

result = 0
for i in range(n):
    t = int(sys.stdin.readline())
    for j in range(t, c+1, t):
        if not j in arr:
            arr[j] = 0
            result += 1

print(result)
