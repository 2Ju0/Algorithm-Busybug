# BOJ 1072
# 게임
import sys

x, y = map(int, sys.stdin.readline().split())
z = y * 100 // x  # 100을 나중에 곱해주면 오차 발생

start, end = 1, 1000000000
answer = 0

while start <= end:
    mid = (start + end) // 2
    temp = int((y + mid) / (x + mid) * 100)
    if temp <= z:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
if answer == 0:
    print(-1)
else:
    print(answer)
