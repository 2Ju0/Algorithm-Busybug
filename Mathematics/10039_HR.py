# BOJ 10039
# 평균점수

a = []
for i in range(5):
    a.append(int(input()))
total = 0
for x in a:
    if x < 40:
        total += 40
    else:
        total += x
print(int(total//5))
# =======================
total = 0
for i in range(5):
    score = int(input())
    if score < 40:
        total += 40
    else:
        total += score
print(int(total//5))
