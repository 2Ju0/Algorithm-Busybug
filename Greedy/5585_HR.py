# BOJ 5585
# 거스름돈

money = int(input())
money = 1000 - money
change = [500, 100, 50, 10, 5, 1]
res = 0
for x in change:
    res += money//x
    money %= x
print(res)
