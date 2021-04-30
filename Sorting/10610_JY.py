# BOJ 10610
# 30
import sys

lst = list(map(int, sys.stdin.readline().rstrip()))
if lst.count(0) == 0 or sum(lst) % 3 != 0:
    print(-1)
else:
    lst.sort(reverse=True)
    for i in lst:
        print(i, end='')
