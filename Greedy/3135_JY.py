# BOJ 3135
# 라디오

a, b = map(int, input().split())
n = int(input())
arr = list(abs(b-int(input())) for _ in range(n))
arr.sort()

d = abs(b-a)
if d <= arr[0]:
    print(d)
else:
    print(1+arr[0])
