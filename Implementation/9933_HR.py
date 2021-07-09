# BOJ 9933
# 민균이의 비밀번호

n = int(input())
res = ""
arr = list()
for i in range(n):
    str = input()
    arr.append(str)
    if str[::-1] in arr:
        res = str
print(len(res), res[len(res)//2])
