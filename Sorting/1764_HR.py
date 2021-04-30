# BOJ 1764
# 듣보잡

n, m = map(int, input().split())
name = list()
for _ in range(n+m):
    name.append(input())
name.sort()
who = list()
i = 0
while i < len(name)-1:
    if name[i] == name[i+1]:
        who.append(name[i])
        i += 2
    else:
        i += 1
print(len(who))
for x in who:
    print(x, sep='\n')
