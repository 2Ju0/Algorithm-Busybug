# BOJ 2720
# 세탁소 사장 동혁

t = int(input())
coin = [25, 10, 5, 1]
arr = list(int(input()) for _ in range(t))
cnt = 0

for i in arr:
    for j in coin:
        print(i//j, end=' ')
        i %= j
    print()
