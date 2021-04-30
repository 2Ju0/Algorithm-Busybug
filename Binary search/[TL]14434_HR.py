# BOJ 14434
# 놀이기구1

n,m,k,q = map(int,input().split())
height_limit = list(map(int,input().split()))
grow = list(map(int,input().split()))
info = list()
temp = [0]*n
for i in range(q):
    i,j,kk = map(int,input().split())
    info.append([i,j,kk])
for i in range(k):
    cnt = 0
    temp[grow[i]-1]+=1
    for i,j,k in info:
        if (temp[i-1] + temp[j-1] >= height_limit[k-1]):
            cnt+=1
    print(cnt)
    