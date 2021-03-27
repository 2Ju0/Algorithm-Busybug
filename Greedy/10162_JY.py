# BOJ 10162
# 전자레인지

t = int(input())
arr = [300, 60, 10]
result = []

for i in arr:
    result.append(str(t//i))
    t %= i

if t != 0:
    print(-1)
else:
    print(' '.join(result))
