# BOJ 1225
# 이상한 곱셈

a, b = input().split()
sumA = 0
sumB = 0
for i in a:
    sumA += int(i)
for j in b:
    sumB += int(j)
print(sumA*sumB)
