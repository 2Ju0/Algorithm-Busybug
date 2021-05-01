# BOJ 10816
# 숫자 카드2

# bisect 사용 구현
from bisect import bisect_left, bisect_right
n = int(input())
num = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
num.sort()
for x in check:
    right = bisect_right(num, x)
    left = bisect_left(num, x)
    print(right-left, end=' ')
# ==================================
# 🎇다른 사람 풀이법 => collections.Counter() 이용
import collections
n = int(input())
nums = map(int, input().split())
m = int(input())
mums = map(int, input().split())
cnt = collections.Counter(nums)
for i in mums:
    print(cnt[i], end=' ')
