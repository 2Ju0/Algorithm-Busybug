# BOJ 11004
# K번째 수

n, k = map(int, input().split(' '))
lst = list(map(int, input().split()))
print(sorted(lst)[k-1])
