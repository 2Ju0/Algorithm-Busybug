# BOJ 10039
# 평균점수

sum = 0

for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    sum += score

print(int(sum / 5))

