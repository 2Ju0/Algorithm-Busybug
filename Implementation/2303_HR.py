# BOJ 2303
# 숫자 게임

from itertools import combinations
import sys
 
n = int(input())
res = 0
winner = 0
for i in range(n):
    li = map(int, sys.stdin.readline().split(" "))
    temp = set(map(sum, list(combinations(li, 3))))
    for x in temp:
        if res <= x % 10:
            res = x % 10
            winner = i+1
print(winner)