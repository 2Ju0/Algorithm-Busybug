# BOJ 5585
# 거스름돈
n = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coin:
    if n // i > 0:
        cnt += n // i
        n = n % i
        if n == 0:
            break
print(cnt)
