# BOJ 5567
# 결혼식

n = int(input())
cnt = [0] * (n+1)
people = list()
arr = list()
for i in range(int(input())):
    a, b = map(int, input().split(" "))

    if a == 1 or b == 1:
        if a == 1:
            cnt[b] = 1
            people.append(b)
        else:
            cnt[a] = 1
            people.append(a)
    else:
        arr.append((a, b))
for x in people:
    for a, b in arr:
        if a == x or b == x:
            if a == x:
                cnt[b] = 1
            else:
                cnt[a] = 1
print(cnt.count(1))
