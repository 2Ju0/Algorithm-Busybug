# BOJ 1181
# 단어 정렬
n = int(input())
words = []
for i in range(n):
    words.append(input())
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
print('\n'.join(words))
