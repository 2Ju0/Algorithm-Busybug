# BOJ 10610
# 30

num = input()
num = sorted(num,reverse = True)
if int("".join(num)) % 30 == 0:
    print("".join(num))
else:
    print(-1)

