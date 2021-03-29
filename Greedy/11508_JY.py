# BOJ 11508
# 2+1 세일
n = int(input())
arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in range(1, len(arr)+1):
    if i % 3 != 0:
        result += arr[-i]
print(result)
