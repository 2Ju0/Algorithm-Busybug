# BOJ 13417
# 카드 문자열

case = int(input())
for i in range(case):
    n = int(input())
    arr = list(input().split())
    temp = [arr[0]]
    for j in range(1, n):
        if ord(temp[0]) < ord(arr[j]):
            temp.append(arr[j])
        else:
            temp.insert(0, arr[j])
    print(''.join(temp))
