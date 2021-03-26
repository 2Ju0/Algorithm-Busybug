# BOJ 15703
# 주사위 쌓기

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
top_count = 1

for i in range(len(arr)):
    cnt = 0
    # temp = 0
    for j in range(i+1,len(arr)):
        cnt+=1
        print(cnt, end= ' ')
        print(top_count, end= '|')
        if cnt > arr[i]:
            top_count +=1
            # temp = j
            break  
        
    # if temp == len(arr)-1:
    #     break  
print(top_count)
