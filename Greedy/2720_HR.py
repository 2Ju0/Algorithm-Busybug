# BOJ 2720
# 세탁소 사장 동혁

change = [25, 10, 5, 1]
for i in range(int(input())):
    money = int(input())
    for x in change:
        print(money//x, end=' ')
        money %= x
    print()
