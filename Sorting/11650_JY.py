# BOJ 11650
# 좌표 정렬하기

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda lst: (lst[0], lst[1]))

for i in lst:
    print(i[0], i[1])
