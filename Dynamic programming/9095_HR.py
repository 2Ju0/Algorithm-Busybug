# BOJ 9095
# 1, 2, 3 더하기

def oneTwoThree(n):
    if n == 1:
        return 1  # 1
    if n == 2:
        return 2  # 1+1 , 2
    if n == 3:
        return 4  # 1+1+1, 1+2, 2+1, 3
    return oneTwoThree(n-3) + oneTwoThree(n-2) + oneTwoThree(n-1)

t = int(input())
for _ in range(t):
    print(oneTwoThree(int(input())))
