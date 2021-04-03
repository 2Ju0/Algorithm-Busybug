# BOJ 2839
# 설탕 배달

n = int(input())
res = float('inf')
flag = True
for i in range(1, n//5+1):
    if ((n-(5*i)) % 3 != 0):
        continue
    else:
        res = min(res, i+((n-(5*i))//3))
        flag = False
if flag == False:
    print(res)
else:
    if(n % 3 == 0):
        print(n//3)
    else:
        print(-1)
# ====================================
# 🎇 다른 풀이법

def sugar(kg):
    for y in range((kg//3)+1):
        for x in range((kg//5)+1):
            if ((5*x + 3*y) == kg):
                return x+y
    return -1
kilo = int(input())
print(sugar(kilo))
