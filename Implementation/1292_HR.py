# BOJ 1292
# 쉽게 푸는 문제

a,b = map(int,input().split(" "))
list = list()
for i in range(1,46):
    for j in range(i):
        list.append(i)
print(sum(list[a-1:b]))
