# BOJ 1225
# 이상한 곱셈

# 분배법칙 이용
import sys

a, b = sys.stdin.readline().split()
a = list(map(int, a))
b = list(map(int, b))
print(sum(a)*sum(b))
