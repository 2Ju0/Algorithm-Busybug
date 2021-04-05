# BOJ 1475
# 방 번호

n = input()
arr = [0]*10
for i in n:
    i = int(i)
    if arr[i] >= 1:
        if i == 6 and arr[9] < arr[6]:
            arr[9] += 1
        elif i == 9 and arr[6] < arr[9]:
            arr[6] += 1
        else:
            arr[i] += 1
    else:
        arr[i] += 1
print(max(arr))
