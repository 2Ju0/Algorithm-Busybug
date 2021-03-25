# BOJ 1157
# 단어 공부

str = input().upper()
temp = [0]*(ord('Z')-ord('A')+1)
result = 0
alpha = 0
flag = True
for x in str:
    temp[ord(x)-65] += 1
for i in range(len(temp)):
    if temp[i] > result:
        result = temp[i]
        alpha = i
        flag = True
    elif temp[i] == result and result != 0:
        flag = False
if flag == True:
    print(chr(65+alpha))
else:
    print("?")
