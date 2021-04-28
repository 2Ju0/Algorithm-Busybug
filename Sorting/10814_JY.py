import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    temp = sys.stdin.readline().split(' ')
    temp[0] = int(temp[0])
    temp[1] = temp[1].rstrip('\n')
    temp.append(i)
    lst.append(temp)

lst.sort(key=lambda lst: (lst[0], lst[2]))
for age, name, _ in lst:
    print(age, name)
