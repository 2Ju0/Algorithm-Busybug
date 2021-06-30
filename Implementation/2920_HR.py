# BOJ 2920
# 음계

str = input()
if str == '1 2 3 4 5 6 7 8':
	print("ascending")
elif str == '8 7 6 5 4 3 2 1':
	print("descending")
else:
	print("mixed")
 
# ========== 비추 ===============
# arr = list(map(int, input().split(" ")))
# prev = arr.pop(0)
# asc, des, mix = 0, 0, 0
# if prev == 1:
#     asc = 1
# elif prev == 8:
#     des = 1
# else:
#     mix = 1
# for x in arr:
#     if asc == 1:
#         if prev + 1 == x:
#             prev = x
#         else:
#             asc = 0
#             mix = 1
#             break
#     elif des == 1:
#         if prev - 1 == x:
#             prev = x
#         else:
#             des = 0
#             mix = 1
#             break
# if mix == 1:
#     print("mixed")
# else:
#     if asc == 1:
#         print("ascending")
#     else:
#         print("descending")
