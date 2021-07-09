# BOJ 9933
# 민균이의 비밀번호

n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(input())

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word) // 2])
        break
