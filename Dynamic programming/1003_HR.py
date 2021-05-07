# BOJ 1003
# 피보나치 함수

def countFibo(n): # 0과 1을 세는 규칙도 피보나치 형태
    zero = [1, 0]
    one = [0, 1]
    for i in range(2, n+1):
        zero.append(zero[i-2]+zero[i-1])
        one.append(one[i-2]+one[i-1])
    return zero, one

t = int(input())
zero, one = countFibo(40)
for _ in range(t):
    x = int(input())
    print(zero[x], one[x])
