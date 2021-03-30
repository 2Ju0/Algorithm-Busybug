# BOJ 13164
# 행복 유치원

import sys

n, k = list(map(int, sys.stdin.readline().split()))
children = list(map(int, sys.stdin.readline().split()))

arr = []
for i in range(len(children) - 1):
    arr.append(children[i + 1] - children[i])

arr.sort(reverse=True)
answer = sum(arr[k - 1:])

print(answer)
