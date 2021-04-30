# BOJ 16401
# 과자 나눠주기

m, n = map(int, input().split())
snack = list(map(int, input().split()))
start, end = 0, max(snack)
max_snack = 0
while (start <= end):
    mid = (start+end) // 2
    if mid == 0:
        break
    src = 0
    for i in snack:
        src += i // mid
    if src >= m:
        start = mid+1
        max_snack = mid
    else:
        end = mid-1
print(max_snack)
