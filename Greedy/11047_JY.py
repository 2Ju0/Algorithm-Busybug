# BOJ 11047
# 동전 0

n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))

for i in coin[::-1]:
    cnt += k//i
    k %= i

print(cnt)
