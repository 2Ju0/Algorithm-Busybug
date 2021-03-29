# BOJ 16435
# 스네이크버드

n, h = map(int, input().split())
arr = list(map(int, input().split()))
len = 0
arr.sort()
for x in arr:
    if h >= x:
        h += 1
        len = h
print(len)
