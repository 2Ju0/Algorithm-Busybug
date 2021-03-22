# BOJ 2609
# 최대공약수와 최소공배수
import math
m, n = map(int, input().split())


def lcm(a, b):
    return a * b // math.gcd(a, b)


print(math.gcd(m, n))  # 최대 공약수(GCD) 계산
print(lcm(m, n))  # 최소 공배수(LCM) 계산
