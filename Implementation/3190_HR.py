# BOJ 3190
# 뱀

from collections import deque
n = int(input())
apple = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    apple[x-1][y-1] = 1
l = int(input())
direction = {}
for _ in range(l):
    x, y = input().split()
    direction[int(x)] = y
x, y = 0, 0
worm = deque([[0, 0]])
turn = 0
case = 1 # 동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while True:
    if turn in direction.keys():  # 오
        if direction[turn] == "D":
            if case == 1: # 동
                case = 4
            elif case == 2: # 서
                case = 3
            elif case == 3: # 남
                case = 1
            else: # 북
                case = 2
        elif direction[turn] == "L":  # 왼
            if case == 1:
                case = 3
            elif case == 2:
                case = 4
            elif case == 3:
                case = 2
            else:
                case = 1
    turn += 1
    if case == 1:
        x += dx[1]
        y += dy[1]
    elif case == 2:
        x += dx[3]
        y += dy[3]
    elif case == 3:
        x += dx[0]
        y += dy[0]
    elif case == 4:
        x += dx[2]
        y += dy[2]
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    else:
        if [x, y] in worm:
            break
        if apple[x][y] == 1:
            apple[x][y] = 0
            worm.append([x, y])
        elif apple[x][y] == 0:
            worm.append([x, y])
            worm.popleft()
print(turn)