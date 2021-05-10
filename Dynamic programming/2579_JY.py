# BOJ 2579
# 계단 오르기
import sys
n = int(sys.stdin.readline())
lst = [0] * 300
for i in range(n):
    lst[i] = int(sys.stdin.readline())

d = [0]*300
d[0] = lst[0]
d[1] = lst[0] + lst[1]
d[2] = max(lst[2] + lst[0], lst[2] + lst[1])
for i in range(3, n):
    d[i] = max(lst[i] + d[i-2], lst[i] + lst[i-1] + d[i-3])

print(d[n-1])
