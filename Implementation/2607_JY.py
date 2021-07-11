# BOJ 2607
# 비슷한 단어
# 틀림: 도저히 모르겠음 

n = int(input())
standard = input()
standard_alpha = dict()
result = 0

for i in standard:
    if i in standard_alpha:
        standard_alpha[i] += 1
    else:
        standard_alpha[i] = 1

for _ in range(n - 1):
    word = input()
    alpha = dict()
    isSimilar = True
    other_words = 0
    change_words = 0
    modify_words = 0
    # 구성된 알파벳 및 개수를 dict에 저장
    for i in word:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1

    if len(standard) - 1 <= sum(list(alpha.values())) <= len(standard) + 1:
        for key in alpha:
            if key not in standard_alpha:  # 기준 단어에 key 알파벳이 없는 경우
                other_words += alpha[key]
                if other_words >= 2 or (len(standard) == 1 and other_words >= 1):
                    isSimilar = False
                    break
            else:  # 기준 단어에 key 알파벳이 있는 경우
                if standard_alpha[key] == alpha[key]:
                    continue
                if standard_alpha[key] == alpha[key] - 1:
                    change_words += 1
                    if change_words >= 2:
                        isSimilar = False
                        break
                elif standard_alpha[key] == alpha[key] + 1:  # 변경
                    modify_words += 1
                    if modify_words >= 2:
                        isSimilar = False
                        break
                else:
                    isSimilar = False
                    break

    else:
        isSimilar = False

    if isSimilar is True and change_words + other_words <= 1:
        if modify_words <= 1:
            if modify_words <= other_words or modify_words <= change_words or modify_words == 1:
                result += 1
                print(word)
print(result)