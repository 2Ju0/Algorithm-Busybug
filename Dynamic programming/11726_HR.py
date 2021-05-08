# BOJ 11726
# 2 x n 타일링

# 🎇다른 풀이법
n = int(input())
a, b = 1, 1
for i in range(n):
    a, b = (a+b) % 10007, a
print(b)
#=======================
n = int(input())
d = [0] * (n+1)
d[1] = 1
for i in range(2, n+1):
    if i == 2:
        d[i] = 2
    else:
        d[i] = (d[i-2] + d[i-1]) % 10007
print(d[n])
