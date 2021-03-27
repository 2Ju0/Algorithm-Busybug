# BOJ 13427
# 카드 문자열
from collections import deque

n = int(input())
str_cards = []

for _ in range(n):
    cnt = int(input())
    cards = deque(input().split())
    for _ in range(len(cards)):
        card = cards.popleft()
        if not str_cards:
            str_cards.append(card)
        else:
            if str_cards[0] >= card:
                str_cards.insert(0, card)
            else:
                str_cards.append(card)

    print(''.join(str_cards))
    str_cards = []
