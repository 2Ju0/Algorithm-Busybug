# BOJ 1654
# 랜선 자르기

k, n = map(int, input().split())
have = list(int(input()) for _ in range(k))
s, e = 1, max(have) # s값을 1로 시작하여 모두 1일 경우에도 실행
res = 0
while (s <= e):
    total = 0
    mid = (s+e) // 2
    if mid == 0:
        break
    for x in have:
        total += x//mid
    if total >= n:
        s = mid+1
        res = mid
    else:
        e = mid-1
print(res)
