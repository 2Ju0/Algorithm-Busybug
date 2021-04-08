# BOJ 10992
# 별 찍기 -17

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    if i != 0 and i != n-1:
        for k in range(2*i+1):
            if k == 0 or k == 2*i:
                print("*", end='')
            else:
                print(" ", end='')
    else:
        for k in range(2*i+1):
            print("*", end='')
    print()
