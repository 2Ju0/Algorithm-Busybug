# BOJ 1181
# 단어 정렬

n = int(input())
arr = list(input() for _ in range(n))
arr = list(set(arr))
arr.sort()
arr.sort(key = len)
for x in arr:
    print(x)

# ====================================== 
# n = int(input())
# arr = list(input() for _ in range(n))
# arr.sort()
# new_arr = []
# for x in arr: # 중복 제거
#     if x not in new_arr:
#         new_arr.append(x)
# new_arr.sort(key=lambda new_arr: (len(new_arr))) # 문자열 짧은 순서대로 정렬
# for x in new_arr:
#     print(x)
