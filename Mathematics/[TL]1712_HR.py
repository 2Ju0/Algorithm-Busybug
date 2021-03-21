# BOJ 1712
# 손익분기점

a, b, c = map(int, input().split())
x = 0
while(a+b*x >= c*x):
    if -a // (b-c) < 0:
        print(-1)
        break
    x += 1
else:
    print(x)
