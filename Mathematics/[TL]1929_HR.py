# BOJ 1929
# 소수 구하기

n, m = map(int, input().split())
for i in range(n, m+1):
    for j in range(2, (i//2)+1):
        if i % j == 0:
            break
    else:
        print(i)
