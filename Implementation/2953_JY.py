# BOJ 2953
# 나는 요리사다
m = -1
num = 0

for i in range(1, 6):
    lst = list(map(int, input().split()))
    if m < sum(lst):
        num = i
        m = sum(lst)
print('{} {}'.format(num, m))
