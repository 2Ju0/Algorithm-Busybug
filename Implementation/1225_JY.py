# BOJ 1225
# 이상한 곱셈
import sys
a, b = sys.stdin.readline().split()
result = 0

for i in a:
    for j in b:
        result += (int(i)*int(j))

print(result)
