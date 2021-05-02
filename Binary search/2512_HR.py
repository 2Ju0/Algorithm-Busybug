# BOJ 2512
# 예산

n = int(input())
request_money = list(map(int, input().split()))
total_money = int(input())
low, high = 1, max(request_money)
max_money = 0
while(low <= high):
    mid = (low+high)//2
    res = 0
    for x in request_money:
       res += min(x, mid)
    if res > total_money:
        high = mid-1
    else:
        low = mid+1
        max_money = mid
print(max_money)
