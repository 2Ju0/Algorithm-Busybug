# BOJ 15703
# 주사위 쌓기
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
pre = 0

while(lst):
    i = lst.pop()
    for _ in range(i):
        if lst:
            num = lst.pop()
            if num == 0:
                break
    cnt += 1
print(cnt)
