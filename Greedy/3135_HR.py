# BOJ 3135
# 라디오

a, b = map(int, input().split())
n = int(input())
arr = list(int(input()) for _ in range(n))
min = abs(a-b)
for x in range(n):
    if min > abs(arr[x]-b)+1:
        min = abs(arr[x]-b)+1
print(min)
# ====================================
# 🎇 다른 풀이법[참고]
a, b = map(int, input().split())
mn = abs(a-b)
for _ in range(int(input())):
    mn = min(mn, abs(int(input())-b)+1)
print(mn)
