# BOJ 4949
# 균형잡힌 세상
import sys
from collections import deque
lst = []

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    lst.append(line)

for str_line in lst:
    check = True
    stack = deque()
    for word in str_line.replace(" ", ""):
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if stack:
                pre_word = stack.pop()
            else:
                check = False
                break
            if pre_word == '[':
                check = False
                break
        elif word == ']':
            if stack:
                pre_word = stack.pop()
            else:
                check = False
                break
            if pre_word == '(':
                check = False
                break
        else:
            continue
    if check == True and not stack:
        print("yes")
    else:
        print("no")
