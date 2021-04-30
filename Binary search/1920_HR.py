# BOJ 1920
# 수 찾기

n = int(input())
a = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
a.sort()
for i in check:
    start, end = 0, n-1
    while start <= end:
        mid = (start+end)//2
        if a[mid] == i:
            print(1)
            break
        elif a[mid] > i:
            end = mid-1
        else:
            start = mid+1
    else:
        print(0)
