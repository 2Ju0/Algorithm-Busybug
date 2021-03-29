# BOJ 15703
# 주사위 쌓기

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = []
check = True
cnt = 0

for i in lst:
    # print("붙일 수 > " + str(i))
    # print("현재 탑 높이" + str(len(result)))
    if i >= len(result):
        result.append(i)
        # print("붙인 후 탑 > ", end='')
        # print(result)
        if i == 0:
            check = False
            cnt += 1
            result.clear()
            continue
    else:
        # print("else > ", end='')
        check = False
        # print(result)
        cnt += 2
        result.clear()
        continue
if check == True:
    cnt += 1
print(cnt)
