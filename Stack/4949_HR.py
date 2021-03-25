# BOJ 4949
# 균형잡힌 세상

while True:
    str = list(input())
    stack = []

    if str[0] == ".":
        break
    for x in str:
        if x == " ":
            continue
        if x == "(" or x == "[":
            stack.append(x)
        elif x == ")":
            if len(stack) == 0:
                print("no")
                break
            temp = stack.pop()
            if temp != "(":
                print("no")
                break
        elif x == "]":
            if len(stack) == 0:
                print("no")
                break
            temp = stack.pop()
            if temp != "[":
                print("no")
                break
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")