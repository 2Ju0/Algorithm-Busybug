# BOJ 2776
# 암기왕

import sys
t = int(input())
for _ in range(t):
    n = int(input())
    note_1 = set(map(int, sys.stdin.readline().split())) # ✨key P => set() 사용 시간단축
    m = int(input())
    note_2 = list(map(int, sys.stdin.readline().split()))
    for x in note_2:
        if x in note_1:
            print(1)
        else:
            print(0)
# =========================================
# 이분탐색 알고리즘 이용 => 시간초과 ?
# import sys
# t = int(input())
# for i in range(t):
#     n = int(input())
#     note_1 = set(map(int, sys.stdin.readline().split()))
#     note_1 = list(note_1)
#     m = int(input())
#     note_2 = list(map(int, sys.stdin.readline().split()))
#     for x in note_2:
#         start, end = 0, len(note_1)-1
#         while (start <= end):
#             mid = (start+end)//2
#             if x == note_1[mid]:
#                 print(1)
#                 break
#             elif x > note_1[mid]:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         else:
#             print(0)