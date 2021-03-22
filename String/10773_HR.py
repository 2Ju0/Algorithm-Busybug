# BOJ 10773
# 제로

n = int(input())
total = 0
arr = []
for i in range(n):
    res = int(input())
    if res == 0:
        arr.pop()
    else:
        arr.append(res)
for x in arr:
    total += x
print(total)
