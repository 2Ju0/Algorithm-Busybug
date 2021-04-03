# BOJ 10809
# 알파벳 찾기

word = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(word.find(chr(i)))
# -------------------------------------
word = input()
lst = [-1]*26

for i in set(word):
    lst[ord(i)-97] = word.index(i)

for i in lst:
    print(i, end=' ')
