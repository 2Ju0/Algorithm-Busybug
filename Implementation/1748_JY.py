# BOJ 1748
# 수 이어 쓰기 1

n = input()
length = len(str(n))

result = 0
for i in range(length - 1):
    result += 9 * 10 ** i * (i + 1)

# n 자리수
result += (int(n) - 10 ** (length - 1) + 1) * length
print(result)
