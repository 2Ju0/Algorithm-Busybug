# BOJ 1475
# 방 번호

n = list(map(int, input()))
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
cnt = 1

for num in n:
    if (num == 6 or num == 9) and arr[num] == 0:
        if num == 6:
            idx = 9
        else:
            idx = 6
        if arr[idx] >= 1:
            arr[idx] -= 1
        else:
            cnt += 1
            for i in range(10):
                arr[i] += 1
            arr[num] -= 1
    else:
        if arr[num] >= 1:
            arr[num] -= 1
        else:
            cnt += 1
            for i in range(10):
                arr[i] += 1
            arr[num] -= 1

print(cnt)
