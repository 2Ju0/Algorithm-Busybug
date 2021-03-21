# 단어순서 뒤집기
n = int(input())

for i in range(n):
    arr = input().split()
    print("Case #{}: ".format(i+1), end='')
    while(arr):
        print(arr.pop(), end=' ')
    print()
    arr = []
