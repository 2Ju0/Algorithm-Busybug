# BOJ 10809
# 알파벳 찾기

s = input()
arr = list(chr(i) for i in range(97, 123))
for i in arr:
    for x in range(len(s)):
        if i == s[x]:
            print(x, end=' ')
            break
    else:
        print(-1, end=' ')
