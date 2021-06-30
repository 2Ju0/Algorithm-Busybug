# BOJ 1316
# 그룹 단어 체커

cnt = 0
for i in range(int(input())):
    str = input()
    arr = [float('inf')]*(ord('z')-ord('a')+1)
    for j in range(len(str)):
        if arr[ord(str[j])-97] == float('inf'): # 문자 처음 등장
            arr[ord(str[j])-97] = j
        else: # 이전에 등장
            if arr[ord(str[j])-97] == j -1 :
                arr[ord(str[j])-97] = j
            else:
                break
    else:
        cnt +=1
print(cnt)
