# BOJ 3079
# 입국심사
import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline()) for _ in range(n)]

    start = min(lst)
    end = max(lst) * k  # 최대로 걸리는 시간
    answer = 0

    while start <= end:
        people = 0
        mid = (start + end) // 2
        for time in lst:
            people += mid // time
        if people < k:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
    print(answer)
