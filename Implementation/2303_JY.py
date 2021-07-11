# BOJ 2303
# 숫자 게임

n = int(input())
people = []
result = 0

for num in range(n):
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                temp = lst[i] + lst[j] + lst[k]
                result = max(result, temp % 10)
    people.append(result)
    result = 0

if people.count(max(people)) > 1:
    people.reverse()
    print(len(people) - people.index(max(people)))
else:
    print(people.index(max(people)) + 1)
