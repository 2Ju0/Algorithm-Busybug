# BOJ 1773
# [T]폭죽쇼

n, c = map(int, input().split())
arr = [0]*(c+1)
for i in range(n):
    k = int(input())
    for j in range(k, c+1, k):
        arr[j] = 1
print(arr.count(1))
# ===================================
# 🎇 다른 풀이법(시간 초과 X) => pypy

import sys
n, c = map(int, sys.stdin.readline().split())
arr = [False]*(c+1)
cnt = 0
for i in range(n):
    k = int(sys.stdin.readline())
    for j in range(k, c+1, k):
        if not arr[j]:
            arr[j] = True
            cnt +=1
print(cnt)
