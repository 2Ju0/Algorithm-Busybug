# BOJ 16435
# 스네이크버드
n, l = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for fruit in fruits:
    if l >= fruit:
        l += 1
print(l)
