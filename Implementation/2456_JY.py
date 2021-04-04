# BOJ 2456
# 나는 학급회장이다

n = int(input())
lst = [[0, 0], [0, 0], [0, 0]]

for i in range(n):
    a, b, c = map(int, input().split())
    lst[0][0] += a
    lst[1][0] += b
    lst[2][0] += c

    lst[0][1] += a * a
    lst[1][1] += b * b
    lst[2][1] += c * c

sum_lst1 = [lst[0][0], lst[1][0], lst[2][0]]
sum_lst2 = [lst[0][1], lst[1][1], lst[2][1]]
m1 = max(sum_lst1)
m2 = max(sum_lst2)

if sum_lst1.count(m1) == 1:
    print(sum_lst1.index(m1)+1,  m1)
else:
    if sum_lst2.count(m2) > 1:
        print(0, m1)
    else:
        print(sum_lst2.index(m2)+1,  sum_lst1[sum_lst2.index(m2)])

# len으로 비교할 경우 반례
# 4
# 3 2 1
# 2 3 1
# 1 2 3
# 2 1 3
