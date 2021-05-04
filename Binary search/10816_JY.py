# BOJ 10816
# 숫자 카드2
import sys

a = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(b):
    if find[i] in dic:
        print(dic[find[i]], end=' ')
    else:
        print(0, end=' ')
# 시간초과로 이진탐색 포기
