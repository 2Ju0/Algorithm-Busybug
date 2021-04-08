# BOJ 5597
# 과제 안 내신 분..?
arr = [0]*30

for _ in range(28):
    arr[int(input())-1] = 1

for _ in range(2):
    print(arr.index(0)+1)
    arr[arr.index(0)] = 1
