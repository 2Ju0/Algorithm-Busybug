# BOJ 5635
# 생일

n = int(input())
arr = []
for _ in range(n):
    name, d, m, y = input().split()
    arr.append([name, int(d), int(m), int(y)])
arr.sort(key=lambda arr: (arr[3], arr[2], arr[1]))
print(arr[n-1][0], arr[0][0], sep='\n')
