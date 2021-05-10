# BOJ 2579△
# 🎇계단 오르기

n = int(input())
floor = [0] + list(int(input()) for i in range(n))
if n == 1:
    print(floor[1])
else:
    d = [0] * (n+1)
    d[1] = floor[1]
    d[2] = floor[1] + floor[2]
    for i in range(3, n+1):
        # 마지막 계단을 기준으로 2가지 경우
        # 1) 마지막 계단 - 3 + 마지막 계단 -1 + 마지막 계단
        # 2) 마지막 계단 - 2 + 마지막 계단
        d[i] = max(d[i-3]+floor[i-1]+floor[i], d[i-2]+floor[i])
    print(d[n])
