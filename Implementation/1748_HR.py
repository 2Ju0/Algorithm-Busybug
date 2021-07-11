# BOJ 1748
# 수 이어 쓰기 1

n = int(input())
jari = len(str(n))
res = 0
for i in range(1, jari):
    res += (9*pow(10, i-1) * i)
res += ((n-pow(10, jari-1)+1)*jari)
print(res)