# BOJ 10162
# 전자레인지

t = int(input())
tlist = [300, 60, 10]
temp = []
for x in tlist:
    temp.append(t // x)
    t %= x
if t != 0:
    print(-1)
else:
    for i in temp:
        print(i, end=' ')
