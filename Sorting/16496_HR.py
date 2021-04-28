# BOJ 16496
# 큰 수 만들기

n = int(input())
num = list(input().split())
for i in range(len(num)):
    max_index = i
    for j in range(i, len(num)):
        if (int(num[max_index]+num[j]) < int(num[j]+num[max_index])):
            max_index = j
    num[i], num[max_index] = num[max_index], num[i]
if (int("".join(num))) == 0:
    print(0)
else:
    print("".join(num))