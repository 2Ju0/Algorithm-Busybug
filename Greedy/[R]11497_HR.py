# △BOJ 11497
# 통나무 건너뛰기

for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    res = 0
    for j in range(2,n):
        c = a[j] - a[j - 2]
        res = max(c, res)
    print(res)