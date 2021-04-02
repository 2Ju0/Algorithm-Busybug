# BOJ 8958
# OX퀴즈

n = int(input())

for _ in range(n):
    result = 0
    cnt = 0
    case = input()
    for i in case:
        if i == "O":
            cnt += 1
            result += cnt
        else:
            cnt = 0

    print(result)
