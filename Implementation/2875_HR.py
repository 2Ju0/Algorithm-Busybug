# BOJ 2875
# 대회 or 인턴

n, m, k = map(int, input().split())
team = 0
while True:
    if (k <= n - 2 + m - 1 and n >= 2 and m >= 1):
        n -= 2
        m -= 1
        team += 1
    else:
        break
print(team)
