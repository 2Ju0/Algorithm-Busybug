# BOJ 1157
# 단어공부
word = list(input().upper())
word_map = dict()

for i in word:
    if i in word_map:
        word_map[i] += 1
    else:
        word_map[i] = 1

word_list = list(word_map.values())
if word_list.count(max(word_list)) > 1:
    print("?")
else:
    # 가장 큰 value를 갖는 key 출력
    print(max(word_map.keys(), key=lambda k: word_map[k]))

# ------------다른 풀이-------------
word = input().upper()
set_word = list(set(word))
arr = []

for i in set_word:
    cnt = word.count(i)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print("?")
else:
    m = arr.index(max(arr))
    print(set_word[m])
