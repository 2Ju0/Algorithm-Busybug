# BOJ 11399
# ATM

n = int(input())
p = list(map(int, input().split()))
p.sort()
total = 0

for i in range(n):
    total += sum(p[0:i+1])
print(total)
