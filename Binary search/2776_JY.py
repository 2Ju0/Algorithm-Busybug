# BOJ 2776
# 암기왕
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    book1 = set(map(int, sys.stdin.readline().split(' ')))
    m = int(sys.stdin.readline())
    book2 = list(map(int, sys.stdin.readline().split(' ')))

    for i in book2:
        if i in book1:
            print(1)
        else:
            print(0)
