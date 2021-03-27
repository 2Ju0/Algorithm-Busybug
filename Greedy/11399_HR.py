# BOJ 10162
# ATM

n = int(input())
time = list(map(int, input().split()))
time.sort()
total = 0
temp = 0
for x in time:
    temp += x
    total += temp
print(total)
