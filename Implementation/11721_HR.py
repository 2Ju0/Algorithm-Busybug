# BOJ 11721
# 열 개씩 끊어 출력하기

str = input()
while str != '':
    print(str[:10])
    str = str[10:]
