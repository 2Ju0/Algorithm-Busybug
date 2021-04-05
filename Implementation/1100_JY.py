# BOJ 1100
# 하얀 칸

chess = []
for _ in range(8):
    chess.append(list(input()))

cnt = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:  # 행이 짝수일 경우
            if j % 2 == 0:  # 열이 짝수일 경우
                if chess[i][j] == 'F':
                    cnt += 1
        else:  # 행이 홀수일 경우
            if j % 2 != 0:  # 열이 홀수일 경우
                if chess[i][j] == 'F':
                    cnt += 1
print(cnt)

# ------------------------------------
# 어차피 홀+홀 = 짝, 짝+짝 = 짝
chess = []
for _ in range(8):
    chess.append(list(map(str, list(input()))))

cnt = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:  # 하얀칸일 경우
            if chess[i][j] == 'F':  # F있을 경우
                cnt += 1
print(cnt)
