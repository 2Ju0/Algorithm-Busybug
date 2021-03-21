import sys

n = int(sys.stdin.readline())
arr = []

for i in range(1, n + 1):
    arr.append(i)
    arr.sort()
    if i % 2 != 0:
        print(arr[i//2])
    else:
        if arr[i//2] < arr[i//2-1]:
            print(arr[i//2])
        else:
            print(arr[i//2-1])
