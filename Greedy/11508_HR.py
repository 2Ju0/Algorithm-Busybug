# BOJ 11508
# 2+1 세일

n = int(input())
arr = list(int(input()) for _ in range(n))
money = 0
arr.sort(reverse=True)
for i in range(len(arr)):
    if (i+1) % 3 != 0:
        money += arr[i]
print(money)
