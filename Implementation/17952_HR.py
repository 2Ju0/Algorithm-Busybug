# △BOJ 17952
# 과제는 끝나지 않아!

import sys
from collections import deque 
n = int(input())
score = deque()
time = deque()
res = 0
for _ in range(n):
    x = list(map(int,sys.stdin.readline().split()))
    if (x[0] == 1): # 과제 1인 경우만 append
        score.append(x[1]) # 과제 점수
        time.append(x[2]) # 시간
    if time: # time이 empty가 아닌 경우
        time[-1] -=1 # 가장 최근에 시작한 과제부터 시간 -1 감소
        if (time[-1] == 0) : # 과제 완료
            time.pop() # 가장 최근 과제 삭제
            res += score.pop()
print(res)