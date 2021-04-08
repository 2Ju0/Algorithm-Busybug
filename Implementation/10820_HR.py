# BOJ 10820
# 문자열 분석

while True:
    try:
        str = input()
        lower = upper = digit = blank = 0
        for x in str:
            if x.islower():
                lower += 1
            elif x.isupper():
                upper += 1
            elif x.isdigit():
                digit += 1
            else:
                blank += 1
        print(lower, upper, digit, blank)
    except EOFError:
        break
