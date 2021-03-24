# BOJ 2577
# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
multi = str(a * b * c)
arr = [0] * 10

for i in multi:
    arr[int(i)] += 1

for i in arr:
    print(i)
