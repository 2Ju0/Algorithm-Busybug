# BOJ 2910
# 빈도 정렬

from collections import Counter
import sys
n, c = map(int, input().split())
nums = list(map(int, input().split()))
res = []
for i in range(n):
    for j in range(0, i):
        if res[j][1] == nums[i]:
            res.append([nums.count(nums[i]), nums[i], res[j][2]])
            break
    else:
        res.append([nums.count(nums[i]), nums[i], i])
res = sorted(res, key=lambda res: (-res[0], res[2]))
for _, x, _ in res:
    print(x, end=' ')
# ======================================
# 🎇 다른 풀이법 => ?
# input = sys.stdin.readline
# n, c = map(int, input().split())
# arr = list(input().rstrip().split())
# res = Counter(arr)
# res = sorted(res.items(), key=lambda x: x[1], reverse=True)
# answer = ""
# for i in res:
#     for _ in range(i[1]):
#         answer += str(i[0])+" "
# print(answer[:-1])
