# BOJ 10814
# 나이순 정렬

n = int(input())
member = []
for i in range(n):
    age, name = list(input().split())
    member.append([age,name,i])
member.sort(key=lambda member: (int(member[0]), member[2])) # member[0] => 첫 번째 인자로 비교
for age, name, order in member:
    print(age, name)
