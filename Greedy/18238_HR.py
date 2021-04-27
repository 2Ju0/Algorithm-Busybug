# BOJ 18238
# ZOAC 2

str = input()
t = min((ord(str[0]) - ord('A')), abs(ord('A') - ord(str[0]) + 26))
for x in range(len(str)-1):
    i = ord(str[x]) - ord(str[x+1])
    j = ord(str[x+1]) - ord(str[x])
    if i < 0:
        i += 26  # 알파벳 총 개수 + i(거리)
    else:
        j += 26
    t += min(abs(i), abs(j))
print(t)
# ===========================================
# 🎇 다른 풀이법
d = {chr(i): i-65 for i in range(65, 90+1)} # {'A':0 , 'B':1, ... 'Z':25} => 딕셔너리
s = input()
c = 0
k = 0
for i in s:
    v = d[i]
    c += min(abs(v-k), k+26-v, 26+v-k)
    k = v
print(c)