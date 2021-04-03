# BOJ 2839
# 설탕 배달
n = int(input())
sugar = [5, 3]
a = 0
arr = []

for i in range(1, n//3 + 1):
    temp = n
    temp -= 3 * i
    if temp % 5 == 0:
        arr.append(i + (temp//5))

if n % 5 == 0:
    a = n//5

if arr:
    if a == 0:
        print(min(arr))
    else:
        print(min(a, min(arr)))
else:
    if a > 0:
        print(a)
    else:
        print(-1)
