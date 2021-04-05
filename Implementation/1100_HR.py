# BOJ 1100
# 하얀 칸

horse = 0
for i in range(8):
    row = input()
    if i %2 == 0:
        for j in range(0, len(row), 2):
            if row[j] == 'F':
                horse += 1
    else:
        for j in range(1, len(row), 2):
            if row[j] == 'F':
                horse += 1
print(horse)
