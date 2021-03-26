# BOJ 12605
# 단어순서 뒤집기

n = int(input())
for i in range(n):
    str = input().split()
    print("Case #%d:" % (i+1), end=' ')
    for j in range(len(str)-1, -1, -1):
        print(str[j], end=' ')
    print()
# ======================================
n = int(input())
for i in range(n):
    str = input().split()
    print("Case #%d:" % (i+1), end=' ')
    while(str):
        print(str.pop(),end= ' ')
    print()