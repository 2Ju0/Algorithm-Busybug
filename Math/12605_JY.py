# 단어순서 뒤집기
n = int(input())

for i in range(n):
    arr = input().split()
    arr.reverse()
    print("Case #" + str(i+1) + ": ", end='')
    for j in arr:
        print(j, end=' ')
    print()
    arr = []
