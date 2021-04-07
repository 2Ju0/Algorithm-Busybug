# BOJ 10820
# 문자열 분석
import sys


while True:
    try:
        a, b, c, d = 0, 0, 0, 0
        line = list(sys.stdin.readline().rstrip('\n'))
        for i in line:
            if i.islower():
                a += 1
            elif i.isupper():
                b += 1
            elif i.isdigit():
                c += 1
            elif i.isspace():
                d += 1
        print("{} {} {} {}".format(a, b, c, d))
    except EOFError:
        break
