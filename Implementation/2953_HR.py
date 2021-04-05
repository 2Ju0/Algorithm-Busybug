# BOJ 2953
# 나는 요리사다

total = 0
res = 0
for i in range(5):
    s = sum(map(int, input().split()))
    if total < s:
        total = s
        res = i+1
print(res, total)
# ========================================
# 🎇다른 풀이법
a = []
for _ in range(5):
  a.append(sum(list(map(int, input().split()))))
x = a.index(max(a))
print(x+1, a[x])
