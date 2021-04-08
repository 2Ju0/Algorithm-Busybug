# BOJ 10820
# 문자열 분석

import sys

while True:
    a, b, c, d = 0, 0, 0, 0
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break

    for i in line:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            c += 1
        elif i.isspace():
            d += 1
    print(a, b, c, d)
