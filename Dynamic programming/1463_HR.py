# BOJ 1463
# 1로 만들기

n = int(input())
d = [0]*(n+1)
for i in range(2, n+1):
    d[i] = d[i-1] + 1  # 자신 - 1 값이 구해진 방법을 우선 저장
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
print(d[n])
