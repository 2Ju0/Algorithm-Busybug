# BOJ 2577
# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

result = (str(a*b*c))
for i in range(10):
    cnt = 0
    for x in result:
        if x == str(i):
            cnt+=1
    print(cnt)
    