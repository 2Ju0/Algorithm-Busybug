# BOJ 10773
# 제로
n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))
