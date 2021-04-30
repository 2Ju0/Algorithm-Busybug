# BOJ 2805
# 나무 자르기

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_h = 0
start, end = 0, max(tree)
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in tree:
        if x > mid:
            total += (x-mid)
    if total < m:
        end = mid-1
    else:  # start >= m => 적어도 m 만큼은 가짐
        start = mid + 1
        max_h = mid
print(max_h)
