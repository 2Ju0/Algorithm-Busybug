# BOJ 5597
# 과제 안 내신 분..?

arr = [0]*30
for i in range(28):
    x = int(input())
    arr[x-1] = 1
res_list = [i for i, value in enumerate(arr) if value == 0]
for x in res_list:
    print(x+1)
