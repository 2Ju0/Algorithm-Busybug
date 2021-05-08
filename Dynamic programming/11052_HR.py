# BOJ 11052
# 🎇카드 구매하기

# 점화식 => d[i] = p[k] + d[i-k]
import sys
n = int(input())
p = [0] + list(map(int, sys.stdin.readline().split()))
d = [0] * (n+1)
d[1] = p[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j]+p[j])
print(d[n])