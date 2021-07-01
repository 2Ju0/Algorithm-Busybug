# BOJ 2941
# 크로아티아 알파벳

str = input()
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for x in alpha:
    if x in str:
       str = str.replace(x," ") # 띄워서 dz= 랑 z= 구별
print(len(str))