# BOJ 18238
# ZOAC 2
n = input()
pre = "A"
result = 0

for i in n:
    asc = ord(i)
    left = asc - ord(pre)
    right = ord(pre) - asc

    if left < 0:
        left += 26
    if right < 0:
        right += 26

    result += min(left, right)
    pre = i
print(result)
