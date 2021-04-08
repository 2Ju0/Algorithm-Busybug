# BOJ 8958
# OX퀴즈

for i in range(int(input())):
    str = input()
    total = 0
    res = 0
    for x in str:
        if x == 'O':
            res += 1
            total += res
        else:
            res = 0
    print(total)
