# BOJ 10815
# 숫자 카드

import sys
n = int(sys.stdin.readline())
my_num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_num = list(map(int, sys.stdin.readline().split()))
my_num.sort()

for x in check_num:
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if my_num[mid] == x:
            print(1, end=' ')
            break
        elif my_num[mid] < x:
            start = mid + 1
        elif my_num[mid] > x:
            end = mid - 1
    else:
        print(0, end=' ')
