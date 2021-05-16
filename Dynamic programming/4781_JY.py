#BOJ 4781
#사탕 가게
import sys

while True:
    n, m = map(float, sys.stdin.readline().split())
    n, m = int(n), int(m * 100 + 0.5)

    if n == 0 and m == 0:
        break

    dp = [0 for _ in range(m + 1)]

    for _ in range(n):
        c, p = map(float, sys.stdin.readline().split())
        c, p = int(c), int(p * 100 + 0.5)
        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i-p] + c)

    print(dp[m])
