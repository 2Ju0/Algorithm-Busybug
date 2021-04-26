import sys
from collections import deque

N = int(sys.stdin.readline())  # 지도의 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 지도
visited = [[False] * N for _ in range(N)]  # 방문 여부 확인
distance = [[-1] * N for _ in range(N)]  # 거리
dx = [-1, 1, 0, 0]  # 북 남 서 동
dy = [0, 0, -1, 1]
sea = deque([])  # 섬 가장자리 좌표, 섬 번호 저장


# 섬 그룹핑 (DFS)
def grouping(board, num):
    q = deque([])
    for i in range(N):
        for j in range(N):
            # 섬이고 방문하지 않았다면
            if board[i][j] == 1 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                board[i][j] = num
                distance[i][j] = 0  # 섬이라서 거리 0 (다리가 아니기 때문)

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            # 섬이라면 넘버링 계속 진행
                            if board[nx][ny] == 1:
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                board[nx][ny] = num
                                distance[nx][ny] = 0

                            # 섬의 동서남북 중 하나가 바다라면(해당 좌표가 가장자리라면)
                            # 섬의 가장자리 좌표와 섬 번호 저장
                            elif board[nx][ny] == 0:
                                sea.append((x, y, num))
                num += 1


# 이동 거리(BFS)
def length(board):
    result = 1e9
    while sea:
        x, y, num = sea.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 바다라면 이동 거리를 계산한다
                if board[nx][ny] == 0:
                    board[nx][ny] = num
                    distance[nx][ny] = distance[x][y] + 1  # 다리길이 + 1
                    sea.append((nx, ny, num))

                # 다른 섬에서 놓은 다리와 만날경우 거리 계산
                elif board[nx][ny] != num:
                    result = min(result, distance[x][y] + distance[nx][ny])
                    break  # 섬과 섬을 잇는 최초의 다리는 가장 짧은 다리이므로 종료
    return result


grouping(board, 1)
print(length(board))
