# BOJ 1292
# 쉽게 푸는 문제

a, b = map(int, input().split())
lst = []

for i in range(1, 1000):  # 1 ~ 46 범위 가능
    lst += [i] * i

print(sum(lst[a-1:b]))
