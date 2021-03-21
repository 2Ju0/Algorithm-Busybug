# BOJ 1655
# 가운데를 말해요

import heapq
# import time
# start = time.time()  # 시작 시간 저장

n = int(input())
temp = []
for i in range(n):
    h = []
    heapq.heappush(temp,int(input()))
    for j in range(len(temp)):
        h.append(heapq.heappop(temp))
    if len(h) % 2 != 0 and len(h) != 1:
        print(h[len(h)//2])
    else:
        print(h[(len(h)-1)//2])
    temp = h
 
# print("time :", time.time() - start)


