# BOJ 11047
# 동전 0

n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort(reverse=True)
num = 0
for i in arr:
    num += k//i
    k %= i
print(num)
